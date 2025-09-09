from __future__ import annotations
from typing import Dict, Any, List
from datetime import datetime

# In-memory collections
AUTHORS: Dict[str, Dict[str, Any]] = {}
BOOKS: Dict[str, Dict[str, Any]] = {}
MEMBERS: Dict[str, Dict[str, Any]] = {}
LOANS: Dict[str, Dict[str, Any]] = {}

# Id generator
_counter = 0

def _next_id() -> str:
	global _counter
	_counter += 1
	return str(_counter)


def now_iso() -> str:
	return datetime.utcnow().isoformat()


# CRUD helpers
async def insert(collection: Dict[str, Dict[str, Any]], data: Dict[str, Any]) -> Dict[str, Any]:
	item = {**data}
	item.setdefault("id", _next_id())
	collection[item["id"]] = item
	return item


async def update(collection: Dict[str, Dict[str, Any]], id_: str, changes: Dict[str, Any]) -> Dict[str, Any] | None:
	item = collection.get(id_)
	if not item:
		return None
	item.update({k: v for k, v in changes.items() if v is not None})
	collection[id_] = item
	return item


async def delete(collection: Dict[str, Dict[str, Any]], id_: str) -> bool:
	return collection.pop(id_, None) is not None


async def get_by_id(collection: Dict[str, Dict[str, Any]], id_: str) -> Dict[str, Any] | None:
	return collection.get(id_)


async def list_items(collection: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
	return list(collection.values())


# Seeding

def seed() -> None:
	if AUTHORS or BOOKS or MEMBERS:
		return
	# Authors
	a1 = {
		"id": _next_id(),
		"name": "George Orwell",
		"bio": "English novelist and critic",
	}
	a2 = {
		"id": _next_id(),
		"name": "Harper Lee",
		"bio": None,
	}
	AUTHORS[a1["id"]] = a1
	AUTHORS[a2["id"]] = a2
	# Books
	b1 = {
		"id": _next_id(),
		"title": "1984",
		"isbn": "9780451524935",
		"author_id": a1["id"],
		"total_copies": 3,
		"available_copies": 3,
	}
	b2 = {
		"id": _next_id(),
		"title": "To Kill a Mockingbird",
		"isbn": "9780061120084",
		"author_id": a2["id"],
		"total_copies": 2,
		"available_copies": 2,
	}
	BOOKS[b1["id"]] = b1
	BOOKS[b2["id"]] = b2
	# Members
	m1 = {"id": _next_id(), "name": "Alice", "email": "alice@example.com", "is_active": True}
	m2 = {"id": _next_id(), "name": "Bob", "email": "bob@example.com", "is_active": True}
	MEMBERS[m1["id"]] = m1
	MEMBERS[m2["id"]] = m2
