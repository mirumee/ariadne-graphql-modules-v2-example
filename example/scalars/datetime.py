from datetime import datetime
from typing import Union, cast

from ariadne_graphql_modules import GraphQLScalar


class DateTimeScalar(GraphQLScalar):
    @classmethod
    def serialize(cls, value: Union["DateTimeScalar", datetime]) -> str:
        if isinstance(value, DateTimeScalar):
            value = cast(datetime, value.unwrap())

        return value.isoformat()

    @classmethod
    def parse_value(cls, value: str) -> datetime:
        return datetime.fromisoformat(value)
