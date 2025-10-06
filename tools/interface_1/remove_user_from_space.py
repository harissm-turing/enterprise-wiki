import datetime
import json
from typing import Any, Dict

from envs.tool import Tool


class RemoveUserFromSpace(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], space_id: str, user_id: str) -> str:
        spaces = data.get("spaces", {})
        users = data.get("users", {})
        space_users = data.get("space_users", {})

        if space_id not in spaces:
            raise ValueError("Space not found")

        if user_id not in users:
            raise ValueError("User not found")

        space_user_id = None
        space_user = None
        for su_id, su in space_users.items():
            if su.get("space_id") == int(space_id) and su.get("user_id") == int(
                user_id
            ):
                space_user_id = su_id
                space_user = su
                break

        if space_user_id is None:
            raise ValueError(f"User {user_id} is not in space {space_id}")

        removed_space_user = space_users.pop(space_user_id)

        result = {
            **removed_space_user,
            "removed_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_user_from_space",
                "description": "Remove a user from a space",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "space_id": {
                            "type": "string",
                            "description": "The ID of the space",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user",
                        },
                    },
                    "required": ["space_id", "user_id"],
                },
            },
        }
