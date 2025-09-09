from typing import List, Dict, Any
from ..types.loan_type import Loan
from ..inputs.loan_inputs import BorrowInput, ReturnInput, LoanFilter
from .db import LOANS, BOOKS, MEMBERS, insert, update, list_items, get_by_id, now_iso


async def borrow_book(input: BorrowInput) -> Loan | None:
	book = await get_by_id(BOOKS, input.book_id)
	member = await get_by_id(MEMBERS, input.member_id)
	if not book or not member:
		return None
	if not member.get("is_active", False):
		return None
	if book["available_copies"] <= 0:
		return None
	# decrement availability
	book["available_copies"] -= 1
	loan_data: Dict[str, Any] = {
		"book_id": input.book_id,
		"member_id": input.member_id,
		"loan_date": now_iso(),
		"return_date": None,
	}
	created = await insert(LOANS, loan_data)
	return Loan(**created)


async def return_book(input: ReturnInput) -> Loan | None:
	loan = await get_by_id(LOANS, input.loan_id)
	if not loan or loan.get("return_date"):
		return None
	book = await get_by_id(BOOKS, loan["book_id"]) if loan else None
	if not book:
		return None
	book["available_copies"] += 1
	updated = await update(LOANS, input.loan_id, {"return_date": now_iso()})
	return Loan(**updated) if updated else None


async def fetch_loans(filters: LoanFilter | None) -> List[Loan]:
	items: List[Dict[str, Any]] = await list_items(LOANS)
	if filters:
		if filters.member_id:
			items = [l for l in items if l["member_id"] == filters.member_id]
		if filters.book_id:
			items = [l for l in items if l["book_id"] == filters.book_id]
		if filters.is_returned is True:
			items = [l for l in items if l.get("return_date") is not None]
		elif filters.is_returned is False:
			items = [l for l in items if l.get("return_date") is None]
	return [Loan(**l) for l in items]
