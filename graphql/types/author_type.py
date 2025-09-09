import strawberry


@strawberry.type
class Author:
	id: str
	name: str
	bio: str | None = None
