import strawberry


@strawberry.type
class Loan:
	id: str
	book_id: str
	member_id: str
	loan_date: str
	return_date: str | None = None
