from typing import Any

from ariadne_graphql_modules import GraphQLObject
from graphql import GraphQLResolveInfo

from ..database import db
from ..interfaces.search_result import SearchResultInterface


class Query(GraphQLObject):
    @GraphQLObject.field(graphql_type=list[SearchResultInterface])
    @staticmethod
    async def search(obj, info: GraphQLResolveInfo, *, query: str) -> list[Any]:
        query = query.strip()
        if not query:
            return []

        results: list = []

        for group in await db.get_all("groups"):
            if query in group.name.lower():
                results.append(group)

        for post in await db.get_all("posts"):
            if query in post.message.lower():
                results.append(post)

        for user in await db.get_all("users"):
            if query in user.username.lower():
                results.append(user)

        return results
