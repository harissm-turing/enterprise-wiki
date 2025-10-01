import json
import datetime
from typing import Any, Dict
from envs.tool import Tool

class ApproveSpace(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], space_id: str, approved_by: str) -> str:
        spaces = data.get("spaces", {})
        users = data.get("users", {})
        
        if space_id not in spaces:
            raise ValueError("Space not found")
        
        if approved_by not in users:
            raise ValueError("User not found")
        
        space = spaces[space_id]
        
        space["is_approved"] = True
        space["approved_by"] = approved_by
        space["approved_at"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        space["updated_at"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        
        return json.dumps(space)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "approve_space",
                "description": "Approve a space",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "space_id": {
                            "type": "string",
                            "description": "The ID of the space to approve"
                        },
                        "approved_by": {
                            "type": "string",
                            "description": "The ID of the user approving the space"
                        }
                    },
                    "required": ["space_id", "approved_by"]
                }
            }
        }
