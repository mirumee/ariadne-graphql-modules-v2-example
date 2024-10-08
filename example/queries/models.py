from typing import Any

from ariadne_graphql_modules import GraphQLObject
from graphql import GraphQLResolveInfo

from ..database import db
from ..unions.model import Model


class Query(GraphQLObject):
    @GraphQLObject.field(graphql_type=list[Model])
    @staticmethod
    async def models(obj, info: GraphQLResolveInfo) -> list[Any]:
        results: list = []

        results += await db.get_all("categories")
        results += await db.get_all("groups")
        results += await db.get_all("posts")
        results += await db.get_all("users")

        return results
