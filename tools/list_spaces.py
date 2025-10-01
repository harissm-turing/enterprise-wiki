import json
from typing import Any, Dict, Optional
from envs.tool import Tool

class ListSpaces(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], space_type: Optional[str] = None, 
               is_approved: Optional[bool] = None, limit: Optional[int] = None) -> str:
        spaces = data.get("spaces", {})
        
        result = list(spaces.values())
        
        if space_type is not None:
            space_type = space_type.lower()
            result = [space for space in result if space.get("type") == space_type]
        
        if is_approved is not None:
            result = [space for space in result if space.get("is_approved") == is_approved]
        
        if limit is not None and limit > 0:
            result = result[:limit]
        
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_spaces",
                "description": "List spaces, optionally filtered by type or approval status",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "space_type": {
                            "type": "string",
                            "description": "Filter by space type (optional)"
                        },
                        "is_approved": {
                            "type": "boolean",
                            "description": "Filter by approval status (optional)"
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of spaces to return (optional)"
                        }
                    }
                }
            }
        }
