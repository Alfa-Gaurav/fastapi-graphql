import strawberry
from typing import List
from ..types.author_type import Author
from ..inputs.author_inputs import AuthorFilter
from ..services.author_service import fetch_authors
from ..types.error_type import Error


@strawberry.type
class AuthorQueries:
	@strawberry.field
	async def authors(self, filters: AuthorFilter | None = None) -> List[Author] | Error:
		if filters and filters.name_contains is not None and not isinstance(filters.name_contains, str):
			return Error(field="name_contains", message="Invalid filter value")
		return await fetch_authors(filters)
