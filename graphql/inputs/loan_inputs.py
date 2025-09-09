import strawberry


@strawberry.input
class BorrowInput:
	book_id: str
	member_id: str


@strawberry.input
class ReturnInput:
	loan_id: str


@strawberry.input
class LoanFilter:
	member_id: str | None = None
	book_id: str | None = None
	is_returned: bool | None = None
