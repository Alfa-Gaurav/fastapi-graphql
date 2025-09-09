import strawberry
from ..types.loan_type import Loan
from ..inputs.loan_inputs import BorrowInput, ReturnInput
from ..services.loan_service import borrow_book, return_book
from ..types.error_type import Error


@strawberry.type
class LoanMutations:
	@strawberry.mutation
	async def borrow(self, input: BorrowInput) -> Loan | Error:
		if not input.book_id:
			return Error(field="book_id", message="book_id is required")
		if not input.member_id:
			return Error(field="member_id", message="member_id is required")
		loan = await borrow_book(input)
		return loan if loan else Error(field="general", message="Cannot borrow book")

	@strawberry.mutation
	async def return_(self, input: ReturnInput) -> Loan | Error:
		if not input.loan_id:
			return Error(field="loan_id", message="loan_id is required")
		loan = await return_book(input)
		return loan if loan else Error(field="loan_id", message="Invalid loan or already returned")
