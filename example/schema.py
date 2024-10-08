from ariadne_graphql_modules import make_executable_schema

from .interfaces.search_result import SearchResultInterface
from .mutations import mutations
from .queries import queries
from .subscriptions import subscriptions


schema = make_executable_schema(
    queries,
    mutations,
    subscriptions,
    SearchResultInterface,
    convert_names_case=True,
)
