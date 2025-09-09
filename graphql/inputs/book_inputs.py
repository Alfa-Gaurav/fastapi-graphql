import strawberry


@strawberry.input
class BookCreateInput:
	title: str
	isbn: str
	author_id: str
	total_copies: int


@strawberry.input
class BookUpdateInput:
	id: str
	title: str | None = None
	isbn: str | None = None
	author_id: str | None = None
	total_copies: int | None = None
	available_copies: int | None = None


@strawberry.input
class BookFilter:
	title_contains: str | None = None
	is_available: bool | None = None
	author_id: str | None = None
