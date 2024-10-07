from datetime import date, datetime
from typing import Union, cast

from ariadne_graphql_modules import GraphQLScalar


class DateScalar(GraphQLScalar):
    @classmethod
    def serialize(cls, value: Union["DateScalar", date]) -> str:
        if isinstance(value, cls):
            value = cast(date, value.unwrap())

        return value.strftime("%Y-%m-%d")

    @classmethod
    def parse_value(cls, value: str) -> date:
        return datetime.strptime(value, "%Y-%m-%d").date()
