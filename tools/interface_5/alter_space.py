import datetime
import json
from typing import Any, Dict, Optional

from envs.tool import Tool


class AlterSpace(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        space_id: str,
        updated_by: str,
        name: Optional[str] = None,
        key: Optional[str] = None,
        space_type: Optional[str] = None,
        is_approved: Optional[bool] = None,
    ) -> str:
        spaces = data.get("spaces", {})
        users = data.get("users", {})

        if space_id not in spaces:
            raise ValueError("Space not found")

        if updated_by not in users:
            raise ValueError("User not found")

        space = spaces[space_id]

        if name is not None:
            space["name"] = name

        if key is not None:
            if any(
                s.get("key") == key.upper() and s_id != space_id
                for s_id, s in spaces.items()
            ):
                raise ValueError(f"Space with key '{key.upper()}' already exists")
            space["key"] = key.upper()

        if space_type is not None:
            space["type"] = space_type.lower()

        if is_approved is not None:
            space["is_approved"] = is_approved

        space["updated_at"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        space["updated_by"] = updated_by

        return json.dumps(space)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "alter_space",
                "description": "Alter an existing space in the wiki",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "space_id": {
                            "type": "string",
                            "description": "The ID of the space to update",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "The ID of the user updating the space",
                        },
                        "name": {
                            "type": "string",
                            "description": "The new name of the space (optional)",
                        },
                        "key": {
                            "type": "string",
                            "description": "The new unique key for the space (optional, will be converted to uppercase)",
                        },
                        "space_type": {
                            "type": "string",
                            "description": "The new type of space (optional, e.g., 'department', 'team', 'project')",
                        },
                        "is_approved": {
                            "type": "boolean",
                            "description": "Whether the space is approved (optional)",
                        },
                    },
                    "required": ["space_id", "updated_by"],
                },
            },
        }
