from ariadne_graphql_modules import GraphQLObject
from graphql import GraphQLResolveInfo


class Query(GraphQLObject):
    hello: str

    @GraphQLObject.resolver("hello")
    @staticmethod
    def resolve_hello(obj, info: GraphQLResolveInfo) -> str:
        return "Hello world!"
