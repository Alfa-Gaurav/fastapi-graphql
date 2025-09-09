import strawberry
from ..types.member_type import Member
from ..inputs.member_inputs import MemberCreateInput, MemberUpdateInput
from ..services.member_service import create_member, update_member, delete_member as delete_member_service
from ..types.error_type import Error


@strawberry.type
class MemberMutations:
	@strawberry.mutation
	async def create_member(self, input: MemberCreateInput) -> Member | Error:
		if not input.name or not input.name.strip():
			return Error(field="name", message="Name is required")
		if not input.email or "@" not in input.email:
			return Error(field="email", message="Invalid email format")
		member = await create_member(input)
		return member if member else Error(field="general", message="Could not create member")

	@strawberry.mutation
	async def update_member(self, input: MemberUpdateInput) -> Member | Error:
		if not input.id:
			return Error(field="id", message="Id is required")
		if input.email is not None and "@" not in input.email:
			return Error(field="email", message="Invalid email format")
		member = await update_member(input)
		return member if member else Error(field="id", message="Member not found")

	@strawberry.mutation
	async def delete_member(self, id: str) -> bool:
		return await delete_member_service(id)
