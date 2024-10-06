from ariadne_graphql_modules import GraphQLObject
from graphql import GraphQLResolveInfo

from ..database import db
from ..types.category import CategoryType


class Query(GraphQLObject):
    @GraphQLObject.field()
    @staticmethod
    async def categories(obj, info: GraphQLResolveInfo) -> list[CategoryType]:
        return await db.get_all("categories", parent_id=None)

    @GraphQLObject.field()
    @staticmethod
    async def category(obj, info: GraphQLResolveInfo, id: str) -> CategoryType | None:
        try:
            id_int = int(id)
        except (TypeError, ValueError):
            return None

        return await db.get_row("categories", id=id_int)
