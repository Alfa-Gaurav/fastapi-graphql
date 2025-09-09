import strawberry
from .queries.author_queries import AuthorQueries
from .queries.book_queries import BookQueries
from .queries.member_queries import MemberQueries
from .queries.loan_queries import LoanQueries
from .mutations.author_mutations import AuthorMutations
from .mutations.book_mutations import BookMutations
from .mutations.member_mutations import MemberMutations
from .mutations.loan_mutations import LoanMutations
from .services.db import seed


@strawberry.type
class Query(AuthorQueries, BookQueries, MemberQueries, LoanQueries):
    ...


@strawberry.type
class Mutation(AuthorMutations, BookMutations, MemberMutations, LoanMutations):
    ...


schema = strawberry.Schema(query=Query, mutation=Mutation)

# Seed demo data on import
seed()
