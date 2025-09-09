import strawberry


@strawberry.type
class Book:
	id: str
	title: str
	isbn: str
	author_id: str
	total_copies: int
	available_copies: int
