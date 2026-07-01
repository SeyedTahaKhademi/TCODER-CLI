from pathlib import Path
from typing import Any, Dict, Optional
from tcoder.tools.base import BaseTool
from tcoder.core.exceptions import FileSystemError


class ReadFileTool(BaseTool):
    """Tool to read the contents of a file."""

    name = "read_file"
    description = "Read the contents of a file from the filesystem."
    parameters = {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "Path to the file to read",
            },
        },
        "required": ["file_path"],
    }

    async def run(self, file_path: str, **kwargs: Any) -> Dict[str, Any]:
        try:
            path = Path(file_path).expanduser().resolve()
            with open(path, "r") as f:
                content = f.read()
            return {"success": True, "content": content, "file_path": file_path}
        except Exception as e:
            raise FileSystemError(f"Failed to read file: {e}")


class WriteFileTool(BaseTool):
    """Tool to write content to a file."""

    name = "write_file"
    description = "Write content to a file, overwriting if it exists."
    parameters = {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "Path to the file to write",
            },
            "content": {
                "type": "string",
                "description": "Content to write to the file",
            },
        },
        "required": ["file_path", "content"],
    }

    async def run(self, file_path: str, content: str, **kwargs: Any) -> Dict[str, Any]:
        try:
            path = Path(file_path).expanduser().resolve()
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w") as f:
                f.write(content)
            return {"success": True, "message": "File written successfully"}
        except Exception as e:
            raise FileSystemError(f"Failed to write file: {e}")
