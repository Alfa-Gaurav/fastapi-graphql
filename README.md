# FastAPI + Strawberry GraphQL: Library Management System

## Quickstart

```bash
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

GraphQL endpoint: `http://localhost:8000/graphql`

## Sample Queries

List books (with simple filters):
```graphql
query {
  books(filters: { titleContains: "1984", isAvailable: true }) {
    ... on Error { field message }
    ... on Book { id title isbn authorId totalCopies }
  }
}
```

Borrow and return a book:
```graphql
mutation {
  borrow(input: { bookId: "1", memberId: "1" }) {
    ... on Error { field message }
    ... on Loan { id bookId memberId loanDate returnDate }
  }
}
```

```graphql
mutation {
  return(input: { loanId: "1" }) {
    ... on Error { field message }
    ... on Loan { id returnDate }
  }
}
```

## Notes
- In-memory storage with basic seeding for demo.
- Async resolvers with thin validation per repository conventions.
