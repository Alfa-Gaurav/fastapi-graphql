import strawberry
from typing import List
from ..types.member_type import Member
from ..inputs.member_inputs import MemberFilter
from ..services.member_service import fetch_members
from ..types.error_type import Error


@strawberry.type
class MemberQueries:
	@strawberry.field
	async def members(self, filters: MemberFilter | None = None) -> List[Member] | Error:
		if filters and filters.is_active not in (True, False, None):
			return Error(field="is_active", message="Invalid filter value")
		return await fetch_members(filters)
