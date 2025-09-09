import strawberry
from ..types.book_type import Book
from ..inputs.book_inputs import BookCreateInput, BookUpdateInput
from ..services.book_service import create_book, update_book, delete_book as delete_book_service
from ..types.error_type import Error


@strawberry.type
class BookMutations:
	@strawberry.mutation
	async def create_book(self, input: BookCreateInput) -> Book | Error:
		if not input.title or not input.title.strip():
			return Error(field="title", message="Title is required")
		if not input.isbn or not input.isbn.strip():
			return Error(field="isbn", message="ISBN is required")
		if input.total_copies <= 0:
			return Error(field="total_copies", message="Must be > 0")
		book = await create_book(input)
		return book if book else Error(field="general", message="Could not create book")

	@strawberry.mutation
	async def update_book(self, input: BookUpdateInput) -> Book | Error:
		if not input.id:
			return Error(field="id", message="Id is required")
		if input.total_copies is not None and input.total_copies <= 0:
			return Error(field="total_copies", message="Must be > 0")
		book = await update_book(input)
		return book if book else Error(field="id", message="Book not found")

	@strawberry.mutation
	async def delete_book(self, id: str) -> bool:
		return await delete_book_service(id)
