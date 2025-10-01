import json
from typing import Any, Dict
from envs.tool import Tool

class GetSpaceUsers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], space_id: str) -> str:
        spaces = data.get("spaces", {})
        space_users = data.get("space_users", {})
        
        if space_id not in spaces:
            raise ValueError("Space not found")
        
        result = []
        for su_id, space_user in space_users.items():
            if space_user.get("space_id") == int(space_id):
                result.append(space_user)
        
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_space_users",
                "description": "Get all users in a space",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "space_id": {
                            "type": "string",
                            "description": "The ID of the space"
                        }
                    },
                    "required": ["space_id"]
                }
            }
        }
