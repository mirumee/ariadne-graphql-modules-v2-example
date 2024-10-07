from ariadne_graphql_modules import GraphQLObject
from graphql import GraphQLResolveInfo

from ..scalars.date import DateScalar


class DatesDeltaType(GraphQLObject):
    days: int
    months: int
    years: int


class Mutation(GraphQLObject):
    @GraphQLObject.field(name="datesDelta")
    @staticmethod
    def resolve_dates_delta(
        obj, info: GraphQLResolveInfo, *, a: DateScalar, b: DateScalar
    ) -> DatesDeltaType:
        years = abs(a.year - b.year)
        months = years * 12 + abs(a.month - b.month)
        days = (a - b).days
        return DatesDeltaType(years=years, months=months, days=days)
