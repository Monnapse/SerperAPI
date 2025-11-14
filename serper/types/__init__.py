from typing import List, Optional, Dict
from pydantic import BaseModel


class SearchParameters(BaseModel):
    q: str
    type: str
    engine: str


class KnowledgeGraph(BaseModel):
    title: Optional[str] = None
    imageUrl: Optional[str] = None
    description: Optional[str] = None
    descriptionSource: Optional[str] = None
    descriptionLink: Optional[str] = None
    attributes: Dict[str, str]


class SiteLink(BaseModel):
    title: str
    link: str


class OrganicResult(BaseModel):
    title: str
    link: str
    snippet: Optional[str] = None
    sitelinks: Optional[List[SiteLink]] = None
    position: Optional[int] = None
    date: Optional[str] = None


class PeopleAlsoAskItem(BaseModel):
    question: str
    snippet: str
    title: str
    link: str


class RelatedSearch(BaseModel):
    query: str


class SearchResponse(BaseModel):
    searchParameters: SearchParameters
    knowledgeGraph: Optional[KnowledgeGraph] = None
    organic: List[OrganicResult]
    peopleAlsoAsk: Optional[List[PeopleAlsoAskItem]] = None
    relatedSearches: Optional[List[RelatedSearch]] = None
    credits: int