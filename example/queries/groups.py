from ariadne_graphql_modules import GraphQLObject
from graphql import GraphQLResolveInfo

from ..database import db
from ..enums.groupfilter import GroupFilter
from ..types.group import GroupType


class Query(GraphQLObject):
    @GraphQLObject.field(args={"filter_": GraphQLObject.argument("filter")})
    @staticmethod
    async def groups(
        obj, info: GraphQLResolveInfo, filter_: GroupFilter = GroupFilter.ALL
    ) -> list[GroupType]:
        if filter_ == GroupFilter.ADMIN:
            return await db.get_all("groups", is_admin=True)

        if filter_ == GroupFilter.MEMBER:
            return await db.get_all("groups", is_admin=False)

        return await db.get_all("groups")

    @GraphQLObject.field()
    @staticmethod
    async def group(obj, info: GraphQLResolveInfo, id: str) -> GroupType | None:
        try:
            id_int = int(id)
        except (TypeError, ValueError):
            return None

        return await db.get_row("groups", id=id_int)
