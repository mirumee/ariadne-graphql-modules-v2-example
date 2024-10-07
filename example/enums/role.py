from ariadne_graphql_modules import GraphQLEnum


class RoleEnum(GraphQLEnum):
    __members__ = [
        "ADMIN",
        "MEMBER",
        "GUEST",
    ]
