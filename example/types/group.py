from typing import TYPE_CHECKING, Annotated

from ariadne_graphql_modules import GraphQLID, GraphQLObject, deferred
from graphql import GraphQLResolveInfo

from ..database import db
from ..models.group import Group

if TYPE_CHECKING:
    from .user import UserType


class GroupType(GraphQLObject):
    id: GraphQLID
    name: str
    is_admin: bool

    @GraphQLObject.field(graphql_type=list[Annotated["UserType", deferred(".user")]])
    @staticmethod
    async def users(obj: Group, info: GraphQLResolveInfo):
        return await db.get_all("users", group_id=obj.id)
