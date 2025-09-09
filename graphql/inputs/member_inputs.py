import strawberry


@strawberry.input
class MemberCreateInput:
	name: str
	email: str
	is_active: bool = True


@strawberry.input
class MemberUpdateInput:
	id: str
	name: str | None = None
	email: str | None = None
	is_active: bool | None = None


@strawberry.input
class MemberFilter:
	is_active: bool | None = None
	email_contains: str | None = None
