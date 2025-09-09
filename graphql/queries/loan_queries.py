import strawberry
from typing import List
from ..types.loan_type import Loan
from ..inputs.loan_inputs import LoanFilter
from ..services.loan_service import fetch_loans
from ..types.error_type import Error


@strawberry.type
class LoanQueries:
	@strawberry.field
	async def loans(self, filters: LoanFilter | None = None) -> List[Loan] | Error:
		if filters and filters.is_returned not in (True, False, None):
			return Error(field="is_returned", message="Invalid filter value")
		return await fetch_loans(filters)
