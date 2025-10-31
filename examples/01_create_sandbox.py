#!/usr/bin/env python3
"""Create and manage a sandbox"""

import asyncio
import os

from koyeb import Sandbox


async def main():
    api_token = os.getenv("KOYEB_API_TOKEN")
    if not api_token:
        print("Error: KOYEB_API_TOKEN not set")
        return

    sandbox = None
    try:
        sandbox = await Sandbox.create(
            image="python:3.11",
            name="example-sandbox",
            wait_ready=True,
            api_token=api_token,
        )

        # Check status
        status = await sandbox.status()
        is_healthy = await sandbox.is_healthy()
        print(f"Status: {status}, Healthy: {is_healthy}")

        # Test command
        result = await sandbox.exec("echo 'Sandbox is ready!'")
        print(result.stdout.strip())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if sandbox:
            await sandbox.delete()


if __name__ == "__main__":
    asyncio.run(main())
