from functools import wraps
from typing import Callable

from domain.models import ArticleResponse, SearchRequest


# REF-006-DECORATOR-DESIGN-PATTERN
def search_timing(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs) -> float:
        # timing start
        func(*args, **kwargs)
        # timing end

        # return duration
        return 5

    return wrapper


@search_timing
async def search(data: SearchRequest) -> ArticleResponse:
    # semantic_result =
    # open api result =
    # weather result =

    return ArticleResponse(title="", intro="", body="", request_duration={})
