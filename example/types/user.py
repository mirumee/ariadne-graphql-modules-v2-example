from typing import TYPE_CHECKING, Annotated

from ariadne_graphql_modules import GraphQLID, GraphQLObject, deferred
from graphql import GraphQLResolveInfo

from ..database import db
from ..interfaces.search_result import SearchResultInterface
from ..enums.role import RoleEnum
from ..models.group import Group
from ..models.post import Post
from ..models.user import User
from .post import PostType

if TYPE_CHECKING:
    from .group import GroupType


class UserType(GraphQLObject, SearchResultInterface):
    id: GraphQLID
    username: str
    group: Annotated["GroupType", deferred(".group")]
    role: RoleEnum
    posts: list[PostType]

    @GraphQLObject.resolver("group")
    @staticmethod
    async def resolve_group(user: User, info: GraphQLResolveInfo) -> Group:
        return await db.get_row("groups", id=user.group_id)

    @GraphQLObject.resolver("posts")
    @staticmethod
    async def resolve_posts(user: User, info: GraphQLResolveInfo) -> list[Post]:
        return await db.get_all("posts", poster_id=user.id)

    @GraphQLObject.resolver("summary")
    @staticmethod
    async def resolve_summary(obj: User, info: GraphQLResolveInfo):
        return f"#{obj.id}: {obj.username}"
