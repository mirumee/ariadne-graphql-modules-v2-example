from datetime import datetime

from ariadne_graphql_modules import GraphQLObject
from graphql import GraphQLResolveInfo

from ..database import db
from ..scalars.date import DateScalar
from ..scalars.datetime import DateTimeScalar


class Query(GraphQLObject):
    @GraphQLObject.field()
    @staticmethod
    async def date(obj, info: GraphQLResolveInfo) -> DateScalar:
        return DateScalar(datetime.now().date())

    @GraphQLObject.field()
    @staticmethod
    async def datetime(obj, info: GraphQLResolveInfo) -> DateTimeScalar:
        return DateTimeScalar(datetime.now())
