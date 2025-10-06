import datetime
import json
from typing import Any, Dict

from envs.tool import Tool


class RejectSpace(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], space_id: str, unapproved_by: str) -> str:
        spaces = data.get("spaces", {})
        users = data.get("users", {})

        if space_id not in spaces:
            raise ValueError("Space not found")

        if unapproved_by not in users:
            raise ValueError("User not found")

        space = spaces[space_id]

        space["is_approved"] = False
        space["unapproved_by"] = unapproved_by
        space["unapproved_at"] = datetime.datetime.utcnow().strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        space["updated_at"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        return json.dumps(space)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reject_space",
                "description": "Reject a space",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "space_id": {
                            "type": "string",
                            "description": "The ID of the space to unapprove",
                        },
                        "unapproved_by": {
                            "type": "string",
                            "description": "The ID of the user unapproving the space",
                        },
                    },
                    "required": ["space_id", "unapproved_by"],
                },
            },
        }
