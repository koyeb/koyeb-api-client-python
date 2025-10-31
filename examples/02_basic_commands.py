#!/usr/bin/env python3
"""Basic command execution"""

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
            name="basic-commands",
            wait_ready=True,
            api_token=api_token,
        )

        # Simple command
        result = await sandbox.exec("echo 'Hello World'")
        print(result.stdout.strip())

        # Python command
        result = await sandbox.exec("python3 -c 'print(2 + 2)'")
        print(result.stdout.strip())

        # Multi-line Python script
        result = await sandbox.exec(
            '''python3 -c "
import sys
print(f'Python version: {sys.version.split()[0]}')
print(f'Platform: {sys.platform}')
"'''
        )
        print(result.stdout.strip())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if sandbox:
            await sandbox.delete()


if __name__ == "__main__":
    asyncio.run(main())
