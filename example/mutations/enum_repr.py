from enum import IntEnum

from ariadne_graphql_modules import GraphQLObject
from graphql import GraphQLResolveInfo

from ..enums.role import RoleEnum


class TestEnum(IntEnum):
    LOREM = 0
    IPSUM = 1
    DOLOR = 2


class Mutation(GraphQLObject):
    @GraphQLObject.field(name="enumRepr")
    @staticmethod
    def resolve_enum_repr(obj, info: GraphQLResolveInfo, *, val: TestEnum) -> str:
        return repr(val)
