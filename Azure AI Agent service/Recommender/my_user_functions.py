from typing import Any, Callable, Set, Dict, List, Optional

from ai_search import search
from reasoning import insights_extractor

# Define the user functions

def get_search_results_from_agent(query: str) -> str:
    """Answer the question related to energy saving suggestions and tips.
    :param query (str): The question.
    :return: query result.
    :rtype: str
    :return: str.
    :rtype: str
    """
    
    return search(query)


def insights_from_agent(query: str) -> str:
    """Extract the insights from the user's historical electricity consumption data and also future consumption patterns.
    :return: Insights
    :rtype: str
    :return: str.
    :rtype:str
    """
    
    return insights_extractor(query)

user_functions: Set[Callable[..., Any]] = {
    get_search_results_from_agent,
    insights_from_agent
    
}