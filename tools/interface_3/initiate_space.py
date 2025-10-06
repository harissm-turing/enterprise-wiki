import datetime
import json
from typing import Any, Dict

from envs.tool import Tool


class InitiateSpace(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        name: str,
        key: str,
        space_type: str,
        created_by: str,
        is_approved: bool = False,
    ) -> str:
        spaces = data.get("spaces", {})
        users = data.get("users", {})

        if created_by not in users:
            raise ValueError("User not found")

        if any(space.get("key") == key.upper() for space in spaces.values()):
            raise ValueError(f"Space with key '{key.upper()}' already exists")

        def generate_id(table: Dict[str, Any]) -> int:
            if not table:
                return 1
            return max(int(k) for k in table.keys()) + 1

        now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        space_id = str(generate_id(spaces))
        new_space = {
            "id": int(space_id),
            "name": name,
            "key": key.upper(),
            "type": space_type.lower(),
            "is_approved": is_approved,
            "created_by": created_by,
            "created_at": now,
            "updated_at": now,
        }

        spaces[str(space_id)] = new_space

        return json.dumps(new_space)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "initiate_space",
                "description": "Initiate a new space in the wiki",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of the space",
                        },
                        "key": {
                            "type": "string",
                            "description": "The unique key for the space (will be converted to uppercase)",
                        },
                        "space_type": {
                            "type": "string",
                            "description": "The type of space (e.g., 'department', 'team', 'project')",
                        },
                        "created_by": {
                            "type": "string",
                            "description": "The ID of the user creating the space",
                        },
                        "is_approved": {
                            "type": "boolean",
                            "description": "Whether the space is approved (default: false)",
                        },
                    },
                    "required": ["name", "key", "space_type", "created_by"],
                },
            },
        }
