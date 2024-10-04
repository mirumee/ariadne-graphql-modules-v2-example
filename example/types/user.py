from typing import TYPE_CHECKING, Annotated

from ariadne_graphql_modules import GraphQLID, GraphQLObject, deferred
from graphql import GraphQLResolveInfo

from ..database import db
from ..models.group import Group
from ..models.user import User

if TYPE_CHECKING:
    from .group import GroupType


class UserType(GraphQLObject):
    id: GraphQLID
    username: str
    email: str
    group: Annotated["GroupType", deferred(".group")]

    @GraphQLObject.resolver("group")
    @staticmethod
    async def resolve_group(user: User, info: GraphQLResolveInfo) -> Group:
        return await db.get_row("groups", id=user.group_id)
