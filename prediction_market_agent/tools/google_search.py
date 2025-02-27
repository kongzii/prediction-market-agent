import serpapi
import typing as t

from prediction_market_agent import utils


def google_search(query: str) -> t.List[str]:
    params = {"q": query, "api_key": utils.get_keys().serp, "num": 4}
    search = serpapi.GoogleSearch(params)
    urls = [result["link"] for result in search.get_dict()["organic_results"]]
    return urls


google_search_schema = {
    "type": "function",
    "function": {
        "name": "google_search",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The google search query.",
                }
            },
            "required": ["query"],
        },
        "description": "Google search to return search results from a query.",
    },
}


class GoogleSearchTool:
    def __init__(self):
        self.fn = google_search
        self.schema = google_search_schema
