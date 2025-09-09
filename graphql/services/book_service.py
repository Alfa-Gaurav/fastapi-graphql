from typing import List, Dict, Any
from ..types.book_type import Book
from ..inputs.book_inputs import BookCreateInput, BookUpdateInput, BookFilter
from .db import BOOKS, insert, update, delete, list_items


async def create_book(input: BookCreateInput) -> Book | None:
	data = {
		"title": input.title,
		"isbn": input.isbn,
		"author_id": input.author_id,
		"total_copies": input.total_copies,
		"available_copies": input.total_copies,
	}
	created = await insert(BOOKS, data)
	return Book(**created)


async def update_book(input: BookUpdateInput) -> Book | None:
	changes = {
		"title": input.title,
		"isbn": input.isbn,
		"author_id": input.author_id,
		"total_copies": input.total_copies,
		"available_copies": input.available_copies,
	}
	updated = await update(BOOKS, input.id, changes)
	return Book(**updated) if updated else None


async def delete_book(id_: str) -> bool:
	return await delete(BOOKS, id_)


async def fetch_books(filters: BookFilter | None) -> List[Book]:
	items: List[Dict[str, Any]] = await list_items(BOOKS)
	if filters:
		if filters.title_contains:
			q = filters.title_contains.lower()
			items = [b for b in items if q in b["title"].lower()]
		if filters.author_id:
			items = [b for b in items if b["author_id"] == filters.author_id]
		if filters.is_available is True:
			items = [b for b in items if b["available_copies"] > 0]
		elif filters.is_available is False:
			items = [b for b in items if b["available_copies"] <= 0]
	return [Book(**b) for b in items]
