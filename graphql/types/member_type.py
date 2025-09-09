import strawberry


@strawberry.type
class Member:
	id: str
	name: str
	email: str
	is_active: bool = True
