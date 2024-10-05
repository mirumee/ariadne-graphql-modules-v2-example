from ariadne_graphql_modules import make_executable_schema

from .queries import queries


schema = make_executable_schema(queries, convert_names_case=True)
