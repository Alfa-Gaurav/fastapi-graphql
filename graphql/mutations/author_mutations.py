import strawberry
from ..types.author_type import Author
from ..inputs.author_inputs import AuthorCreateInput, AuthorUpdateInput
from ..services.author_service import create_author, update_author, delete_author as delete_author_service
from ..types.error_type import Error


@strawberry.type
class AuthorMutations:
	@strawberry.mutation
	async def create_author(self, input: AuthorCreateInput) -> Author | Error:
		if not input.name or not input.name.strip():
			return Error(field="name", message="Name is required")
		author = await create_author(input)
		return author if author else Error(field="general", message="Could not create author")

	@strawberry.mutation
	async def update_author(self, input: AuthorUpdateInput) -> Author | Error:
		if not input.id:
			return Error(field="id", message="Id is required")
		author = await update_author(input)
		return author if author else Error(field="id", message="Author not found")

	@strawberry.mutation
	async def delete_author(self, id: str) -> bool:
		return await delete_author_service(id)
