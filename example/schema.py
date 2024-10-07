from ariadne_graphql_modules import make_executable_schema

from .queries import queries
from .subscriptions import subscriptions


schema = make_executable_schema(
    queries,
    subscriptions,
    convert_names_case=True,
)
