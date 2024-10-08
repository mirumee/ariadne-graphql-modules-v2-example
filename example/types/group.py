from typing import TYPE_CHECKING, Annotated

from ariadne_graphql_modules import GraphQLID, GraphQLObject, deferred
from graphql import GraphQLResolveInfo

from ..database import db
from ..interfaces.search_result import SearchResultInterface
from ..models.group import Group

if TYPE_CHECKING:
    from .user import UserType


class GroupType(GraphQLObject, SearchResultInterface):
    id: GraphQLID
    name: str
    is_admin: bool

    @GraphQLObject.field(graphql_type=list[Annotated["UserType", deferred(".user")]])
    @staticmethod
    async def users(obj: Group, info: GraphQLResolveInfo):
        return await db.get_all("users", group_id=obj.id)

    @GraphQLObject.resolver("summary")
    @staticmethod
    async def resolve_summary(obj: Group, info: GraphQLResolveInfo):
        return f"#{obj.id}: {obj.name}"
