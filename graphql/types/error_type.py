import strawberry


@strawberry.type
class Error:
	field: str
	message: str
