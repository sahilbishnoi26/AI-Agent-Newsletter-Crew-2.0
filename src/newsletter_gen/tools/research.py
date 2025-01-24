from crewai.tools import BaseTool
from exa_py import Exa
import os
from datetime import datetime, timedelta


class SearchAndContents(BaseTool):
    name: str = "Search and Contents Tool"
    description: str = (
        "Searches the web based on a search query for the latest results. Results are only from the last week. "
        "Uses the Exa API. This also returns the contents of the search results."
    )

    def _run(self, search_query: str) -> str:
        """
        Search the web and get contents for the latest results using the Exa API.
        """
        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        one_week_ago = datetime.now() - timedelta(days=7)
        date_cutoff = one_week_ago.strftime("%Y-%m-%d")

        search_results = exa.search_and_contents(
            query=search_query,
            use_autoprompt=True,
            start_published_date=date_cutoff,
            text={"include_html_tags": False, "max_characters": 8000},
        )

        return search_results


class FindSimilar(BaseTool):
    name: str = "Find Similar Tool"
    description: str = (
        "Searches for similar articles to a given article using the Exa API. Takes in a URL of the article."
    )

    def _run(self, article_url: str) -> str:
        """
        Find similar articles using the Exa API.
        """
        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        one_week_ago = datetime.now() - timedelta(days=7)
        date_cutoff = one_week_ago.strftime("%Y-%m-%d")

        search_results = exa.find_similar(
            url=article_url,
            start_published_date=date_cutoff,
        )

        return search_results


class GetContents(BaseTool):
    name: str = "Get Contents Tool"
    description: str = (
        "Gets the contents of a specific article using the Exa API. "
        "Takes in the ID of the article as a string, like this: 'https://www.cnbc.com/2024/04/18/my-news-story'."
    )

    def _run(self, article_id: str) -> str:
        """
        Get the contents of a specific article using the Exa API.
        """
        if not isinstance(article_id, str):
            raise ValueError("article_id must be a string representing a single article ID or URL.")

        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        # Wrap the article_id in a list to match the API's expected input
        contents = exa.get_contents([article_id])
        return contents
