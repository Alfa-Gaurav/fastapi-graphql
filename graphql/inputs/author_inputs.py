import strawberry


@strawberry.input
class AuthorCreateInput:
	name: str
	bio: str | None = None


@strawberry.input
class AuthorUpdateInput:
	id: str
	name: str | None = None
	bio: str | None = None


@strawberry.input
class AuthorFilter:
	name_contains: str | None = None
