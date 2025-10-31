# coding: utf-8

"""
Async Koyeb Sandbox - Python SDK for creating and managing Koyeb sandboxes asynchronously
"""

import asyncio
import time
from typing import Dict, List, Optional

from koyeb.api.models.create_app import CreateApp
from koyeb.api.models.deployment_port import DeploymentPort

from .utils import (
    build_env_vars,
    create_deployment_definition,
    create_docker_source,
    get_api_client,
    is_sandbox_healthy,
)


class Sandbox:
    """
    Async sandbox for running code on Koyeb infrastructure.
    Provides async creation and deletion functionality with proper health polling.
    """

    def __init__(
        self,
        sandbox_id: str,
        app_id: str,
        service_id: str,
        instance_id: str,
        name: Optional[str] = None,
        api_token: Optional[str] = None,
    ):
        self.sandbox_id = sandbox_id
        self.app_id = app_id
        self.service_id = service_id
        self.instance_id = instance_id
        self.name = name
        self.api_token = api_token
        self._created_at = time.time()

    @classmethod
    async def create(
        cls,
        image: str = "docker.io/library/ubuntu:latest",
        name: str = "quick-sandbox",
        wait_ready: bool = True,
        instance_type: str = "nano",
        ports: Optional[List[DeploymentPort]] = None,
        env: Optional[Dict[str, str]] = None,
        regions: Optional[List[str]] = None,
        api_token: Optional[str] = None,
        timeout: int = 300,
    ) -> "Sandbox":
        """
            Create a new sandbox instance with async support.

            Args:
                image: Docker image to use (default: ubuntu:latest)
                name: Name of the sandbox
                wait_ready: Wait for sandbox to be ready (default: True)
                instance_type: Instance type (default: nano)
                ports: List of ports to expose
                env: Environment variables
                regions: List of regions to deploy to (default: ["na"])
                api_token: Koyeb API token (if None, will try to get from KOYEB_API_TOKEN env var)
                timeout: Timeout for sandbox creation in seconds

        Returns:
                Sandbox: A new Sandbox instance
        """
        if api_token is None:
            import os

            api_token = os.getenv("KOYEB_API_TOKEN")
            if not api_token:
                raise ValueError(
                    "API token is required. Set KOYEB_API_TOKEN environment variable or pass api_token parameter"
                )

        loop = asyncio.get_running_loop()
        sandbox = await loop.run_in_executor(
            None,
            lambda: cls._create_sync(
                name=name,
                image=image,
                instance_type=instance_type,
                ports=ports,
                env=env,
                regions=regions,
                api_token=api_token,
                timeout=timeout,
            ),
        )

        if wait_ready:
            await sandbox.wait_ready(timeout=timeout)

        return sandbox

    @classmethod
    def _create_sync(
        cls,
        name: str,
        image: str = "docker.io/library/ubuntu:latest",
        instance_type: str = "nano",
        ports: Optional[List[DeploymentPort]] = None,
        env: Optional[Dict[str, str]] = None,
        regions: Optional[List[str]] = None,
        api_token: Optional[str] = None,
        timeout: int = 300,
    ) -> "Sandbox":
        """Synchronous creation method"""
        apps_api, services_api, _ = get_api_client(api_token)

        app_name = f"sandbox-app-{name}-{int(time.time())}"
        app_response = apps_api.create_app(app=CreateApp(name=app_name))
        app_id = app_response.app.id

        env_vars = build_env_vars(env)
        docker_source = create_docker_source(image, ["sleep", "infinity"])
        deployment_definition = create_deployment_definition(
            name=f"sandbox-service-{name}",
            docker_source=docker_source,
            env_vars=env_vars,
            instance_type=instance_type,
            ports=ports,
            regions=regions,
        )

        from koyeb.api.models.create_service import CreateService

        create_service = CreateService(app_id=app_id, definition=deployment_definition)
        service_response = services_api.create_service(service=create_service)
        service_id = service_response.service.id
        deployment_id = service_response.service.latest_deployment_id

        from koyeb.api.api.deployments_api import DeploymentsApi

        deployments_api = DeploymentsApi(services_api.api_client)

        max_wait = min(timeout // 2, 60) if timeout > 60 else timeout
        wait_interval = 0.5
        start_time = time.time()

        while time.time() - start_time < max_wait:
            try:
                scaling_response = deployments_api.get_deployment_scaling(
                    id=deployment_id
                )

                if scaling_response.replicas and scaling_response.replicas[0].instances:
                    instance_id = scaling_response.replicas[0].instances[0].id
                    break
                else:
                    print(
                        f"Waiting for instances to be created... (elapsed: {time.time() - start_time:.1f}s)"
                    )
                    time.sleep(wait_interval)
            except Exception as e:
                print(f"Error getting deployment scaling: {e}")
                time.sleep(wait_interval)
        else:
            raise Exception(
                f"No instances found in deployment after {max_wait} seconds"
            )

        sandbox = cls(
            sandbox_id=name,
            app_id=app_id,
            service_id=service_id,
            instance_id=instance_id,
            name=name,
            api_token=api_token,
        )
        return sandbox

    async def wait_ready(self, timeout: int = 60, poll_interval: float = 2.0) -> bool:
        """
        Wait for sandbox to become ready with proper async polling.

        Args:
            timeout: Maximum time to wait in seconds
            poll_interval: Time between health checks in seconds

        Returns:
            bool: True if sandbox became ready, False if timeout
        """
        start_time = time.time()

        while time.time() - start_time < timeout:
            loop = asyncio.get_running_loop()
            is_healthy = await loop.run_in_executor(
                None, is_sandbox_healthy, self.instance_id, self.api_token
            )

            if is_healthy:
                return True

            await asyncio.sleep(poll_interval)

        return False

    async def delete(self) -> None:
        """Delete the sandbox instance asynchronously."""
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self._delete_sync)

    def _delete_sync(self) -> None:
        """Synchronous deletion method"""
        apps_api, services_api, _ = get_api_client(self.api_token)
        services_api.delete_service(self.service_id)
        apps_api.delete_app(self.app_id)

    async def status(self) -> str:
        """Get current sandbox status asynchronously"""
        from .utils import get_sandbox_status

        loop = asyncio.get_running_loop()
        status = await loop.run_in_executor(
            None, get_sandbox_status, self.instance_id, self.api_token
        )
        return status.value

    async def is_healthy(self) -> bool:
        """Check if sandbox is healthy and ready for operations asynchronously"""
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            None, is_sandbox_healthy, self.instance_id, self.api_token
        )

    @property
    def filesystem(self):
        """Get filesystem operations interface"""
        from .filesystem import SandboxFilesystem

        return SandboxFilesystem(self)

    @property
    def exec(self):
        """Get command execution interface"""
        from .exec import SandboxExecutor

        return SandboxExecutor(self)
