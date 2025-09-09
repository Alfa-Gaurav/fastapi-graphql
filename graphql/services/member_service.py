from typing import List, Dict, Any
from ..types.member_type import Member
from ..inputs.member_inputs import MemberCreateInput, MemberUpdateInput, MemberFilter
from .db import MEMBERS, insert, update, delete, list_items


async def create_member(input: MemberCreateInput) -> Member | None:
	data = {"name": input.name, "email": input.email, "is_active": input.is_active}
	created = await insert(MEMBERS, data)
	return Member(**created)


async def update_member(input: MemberUpdateInput) -> Member | None:
	changes = {"name": input.name, "email": input.email, "is_active": input.is_active}
	updated = await update(MEMBERS, input.id, changes)
	return Member(**updated) if updated else None


async def delete_member(id_: str) -> bool:
	return await delete(MEMBERS, id_)


async def fetch_members(filters: MemberFilter | None) -> List[Member]:
	items: List[Dict[str, Any]] = await list_items(MEMBERS)
	if filters:
		if filters.is_active in (True, False):
			items = [m for m in items if m["is_active"] is filters.is_active]
		if filters.email_contains:
			q = filters.email_contains.lower()
			items = [m for m in items if q in m["email"].lower()]
	return [Member(**m) for m in items]
