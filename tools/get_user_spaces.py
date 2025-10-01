import json
from typing import Any, Dict
from envs.tool import Tool

class GetUserSpaces(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        spaces = data.get("spaces", {})
        users = data.get("users", {})
        space_users = data.get("space_users", {})
        
        if user_id not in users:
            raise ValueError("User not found")
        
        space_ids = []
        for su_id, space_user in space_users.items():
            if space_user.get("user_id") == int(user_id):
                space_ids.append(str(space_user.get("space_id")))
        
        result = []
        for space_id in space_ids:
            if space_id in spaces:
                result.append(spaces[space_id])
        
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_spaces",
                "description": "Get all spaces a user is in",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user"
                        }
                    },
                    "required": ["user_id"]
                }
            }
        }
