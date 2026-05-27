from domain.models import ArticleResponse, SearchRequest
from domain.services.article_service import search
from fastapi import APIRouter

router = APIRouter()


# REF-011-HTTP-METHOD, REF-011-RESOURCE-NAMING, REF-011-SYNCHRONICITY, REF-011-DATA-DESERIALIZATION
# REF-011-INPUT-VALIDATION, REF-011-RESPONSE-VALIDATION
@router.post("articles", response_model=ArticleResponse)
async def search_articles(data: SearchRequest) -> ArticleResponse:
    # REF-008-SPHINX-DOCSTRING
    """
    Performs semantic search

    :param data: The search request payload containing keywords.
    :type data: SearchRequest

    :returns: The response containing the list of articles matching the semantic search criteria.
    :rtype: ArticleResponse
    """
    result: ArticleResponse = await search(data)

    return result
    # return "Hello"
