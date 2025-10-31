#!/usr/bin/env python3
"""File manipulation operations"""

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
            name="file-manip",
            wait_ready=True,
            api_token=api_token,
        )

        fs = sandbox.filesystem

        # Setup
        await fs.write_file("/tmp/file1.txt", "Content of file 1")
        await fs.write_file("/tmp/file2.txt", "Content of file 2")
        await fs.mkdir("/tmp/test_dir", recursive=True)

        # Rename file
        await fs.rename_file("/tmp/file1.txt", "/tmp/renamed_file.txt")
        print(f"Renamed: {await fs.exists('/tmp/renamed_file.txt')}")

        # Move file
        await fs.move_file("/tmp/file2.txt", "/tmp/test_dir/moved_file.txt")
        print(f"Moved: {await fs.exists('/tmp/test_dir/moved_file.txt')}")

        # Copy file (read + write)
        original_content = await fs.read_file("/tmp/renamed_file.txt")
        await fs.write_file("/tmp/test_dir/copied_file.txt", original_content.content)
        print(f"Copied: {await fs.exists('/tmp/test_dir/copied_file.txt')}")

        # Delete file
        await fs.rm("/tmp/renamed_file.txt")
        print(f"Deleted: {not await fs.exists('/tmp/renamed_file.txt')}")

        # Delete directory
        await fs.rm("/tmp/test_dir", recursive=True)
        print(f"Directory deleted: {not await fs.exists('/tmp/test_dir')}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if sandbox:
            await sandbox.delete()


if __name__ == "__main__":
    asyncio.run(main())
