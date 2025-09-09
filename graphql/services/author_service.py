from typing import List, Dict, Any
from ..types.author_type import Author
from ..inputs.author_inputs import AuthorCreateInput, AuthorUpdateInput, AuthorFilter
from .db import AUTHORS, insert, update, delete, list_items


async def create_author(input: AuthorCreateInput) -> Author | None:
	data = {"name": input.name, "bio": input.bio}
	created = await insert(AUTHORS, data)
	return Author(**created)


async def update_author(input: AuthorUpdateInput) -> Author | None:
	updated = await update(AUTHORS, input.id, {"name": input.name, "bio": input.bio})
	return Author(**updated) if updated else None


async def delete_author(id_: str) -> bool:
	return await delete(AUTHORS, id_)


async def fetch_authors(filters: AuthorFilter | None) -> List[Author]:
	items: List[Dict[str, Any]] = await list_items(AUTHORS)
	if filters and filters.name_contains:
		q = filters.name_contains.lower()
		items = [a for a in items if q in a["name"].lower()]
	return [Author(**a) for a in items]
