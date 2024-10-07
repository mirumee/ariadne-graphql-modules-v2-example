from ariadne_graphql_modules import GraphQLID, GraphQLObject
from graphql import GraphQLResolveInfo

from ..database import db
from ..types.user import UserType


class Query(GraphQLObject):
    @GraphQLObject.field()
    @staticmethod
    async def users(obj, info: GraphQLResolveInfo) -> list[UserType]:
        return await db.get_all("users")

    @GraphQLObject.field()
    @staticmethod
    async def user(obj, info: GraphQLResolveInfo, id: GraphQLID) -> UserType | None:
        try:
            id_int = int(id)
        except (TypeError, ValueError):
            return None

        return await db.get_row("users", id=id_int)
