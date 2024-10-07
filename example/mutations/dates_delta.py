from datetime import date

from ariadne_graphql_modules import GraphQLObject
from graphql import GraphQLResolveInfo

from ..scalars.date import DateScalar


class DatesDeltaType(GraphQLObject):
    days: int
    months: int
    years: int


class Mutation(GraphQLObject):
    @GraphQLObject.field(
        name="datesDelta",
        args={
            "a": GraphQLObject.argument(graphql_type=DateScalar),
            "b": GraphQLObject.argument(graphql_type=DateScalar),
        },
    )
    @staticmethod
    def resolve_dates_delta(
        obj, info: GraphQLResolveInfo, *, a: date, b: date
    ) -> DatesDeltaType:
        years = abs(a.year - b.year)
        months = years * 12 + abs(a.month - b.month)
        days = (a - b).days
        return DatesDeltaType(years=years, months=months, days=days)
