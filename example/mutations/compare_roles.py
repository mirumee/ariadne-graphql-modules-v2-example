from enum import IntEnum

from ariadne_graphql_modules import GraphQLObject
from graphql import GraphQLResolveInfo

from ..enums.role import RoleEnum


class RoleDiff(IntEnum):
    EQUAL = 0
    A_GREATER = 1
    A_LOWER = 2


class Mutation(GraphQLObject):
    @GraphQLObject.field(name="compareRoles")
    @staticmethod
    def resolve_compare_roles(
        obj, info: GraphQLResolveInfo, *, a: RoleEnum, b: RoleEnum
    ) -> RoleDiff:
        index_a = RoleEnum.__members__.index(a)
        index_b = RoleEnum.__members__.index(b)

        if index_a == index_b:
            return RoleDiff.EQUAL

        if index_a < index_b:
            return RoleDiff.A_GREATER

        return RoleDiff.A_LOWER
