import json
from typing import Any, Dict

from envs.tool import Tool


class RetrieveSpaceById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], space_id: str) -> str:
        spaces = data.get("spaces", {})

        if space_id not in spaces:
            raise ValueError(f"Space with ID '{space_id}' not found")

        return json.dumps(spaces[space_id])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "retrieve_space_by_id",
                "description": "Retrieve a space by its ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "space_id": {
                            "type": "string",
                            "description": "The ID of the space to retrieve",
                        }
                    },
                    "required": ["space_id"],
                },
            },
        }
