from ariadne_graphql_modules import GraphQLObject, make_executable_schema
from graphql import GraphQLResolveInfo

from .database import db
from .enums.groupfilter import GroupFilter
from .types.group import GroupType
from .types.user import UserType


class Query(GraphQLObject):
    hello: str

    @GraphQLObject.resolver("hello")
    @staticmethod
    def resolve_hello(obj, info: GraphQLResolveInfo) -> str:
        return "Hello world!"

    @GraphQLObject.field(args={"filter_": GraphQLObject.argument("filter")})
    async def groups(obj, info: GraphQLResolveInfo, filter_: GroupFilter) -> list[GroupType]:
        if filter_ == GroupFilter.ADMIN:
            return await db.get_all("groups", is_admin=True)

        if filter_ == GroupFilter.MEMBER:
            return await db.get_all("groups", is_admin=False)
        
        return await db.get_all("groups")

    @GraphQLObject.field()
    async def group(obj, info: GraphQLResolveInfo, id: str) -> GroupType | None:
        try:
            id_int = int(id)
        except (TypeError, ValueError):
            return None

        return await db.get_row("groups", id=id_int)

    @GraphQLObject.field()
    async def users(obj, info: GraphQLResolveInfo) -> list[UserType]:
        return await db.get_all("users")


schema = make_executable_schema(Query, convert_names_case=True)
