from ariadne_graphql_modules import GraphQLObject
from graphql import GraphQLResolveInfo

from ..database import db
from ..types.user import UserType


class Query(GraphQLObject):
    @GraphQLObject.field()
    @staticmethod
    async def users(obj, info: GraphQLResolveInfo) -> list[UserType]:
        return await db.get_all("users")
