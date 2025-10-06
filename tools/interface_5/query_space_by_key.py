import json
from typing import Any, Dict

from envs.tool import Tool


class QuerySpaceByKey(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], key: str) -> str:
        spaces = data.get("spaces", {})

        key = key.upper()
        for space_id, space in spaces.items():
            if space.get("key") == key:
                return json.dumps(space)

        raise ValueError(f"Space with key '{key}' not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "query_space_by_key",
                "description": "Query a space by its key",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "key": {
                            "type": "string",
                            "description": "The key of the space to retrieve",
                        }
                    },
                    "required": ["key"],
                },
            },
        }
