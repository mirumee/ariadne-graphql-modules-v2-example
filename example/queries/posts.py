from typing import Optional

from ariadne_graphql_modules import GraphQLID, GraphQLObject
from graphql import GraphQLResolveInfo

from ..database import db
from ..models.post import Post
from ..types.post import PostType


class Query(GraphQLObject):
    @GraphQLObject.field(graphql_type=list[PostType])
    @staticmethod
    async def posts(obj, info: GraphQLResolveInfo) -> list[Post]:
        return await db.get_all("posts")

    @GraphQLObject.field(graphql_type=Optional[PostType])
    @staticmethod
    async def post(obj, info: GraphQLResolveInfo, id: GraphQLID) -> Post | None:
        try:
            id_int = int(id)
        except (TypeError, ValueError):
            return None

        return await db.get_row("posts", id=id_int)
