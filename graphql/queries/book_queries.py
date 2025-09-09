import strawberry
from typing import List
from ..types.book_type import Book
from ..inputs.book_inputs import BookFilter
from ..services.book_service import fetch_books
from ..types.error_type import Error


@strawberry.type
class BookQueries:
	@strawberry.field
	async def books(self, filters: BookFilter | None = None) -> List[Book] | Error:
		if filters and filters.is_available not in (True, False, None):
			return Error(field="is_available", message="Invalid filter value")
		return await fetch_books(filters)
