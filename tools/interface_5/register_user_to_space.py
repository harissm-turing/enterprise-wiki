import datetime
import json
from typing import Any, Dict

from envs.tool import Tool


class RegisterUserToSpace(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], space_id: str, user_id: str, role: str) -> str:
        spaces = data.get("spaces", {})
        users = data.get("users", {})
        space_users = data.get("space_users", {})

        if space_id not in spaces:
            raise ValueError("Space not found")

        if user_id not in users:
            raise ValueError("User not found")

        for su_id, space_user in space_users.items():
            if space_user.get("space_id") == int(space_id) and space_user.get(
                "user_id"
            ) == int(user_id):
                raise ValueError(f"User {user_id} is already in space {space_id}")

        def generate_id(table: Dict[str, Any]) -> int:
            if not table:
                return 1
            return max(int(k) for k in table.keys()) + 1

        now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        space_user_id = str(generate_id(space_users))
        space_user = {
            "id": int(space_user_id),
            "space_id": int(space_id),
            "user_id": int(user_id),
            "role": role,
            "created_at": now,
            "updated_at": now,
        }

        space_users[space_user_id] = space_user

        return json.dumps(space_user)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "register_user_to_space",
                "description": "Register a user to a space with a specific role",
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
                        "role": {
                            "type": "string",
                            "description": "The role of the user in the space (e.g., 'admin', 'editor', 'viewer')",
                        },
                    },
                    "required": ["space_id", "user_id", "role"],
                },
            },
        }
