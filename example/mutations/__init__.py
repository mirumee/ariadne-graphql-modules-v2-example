from typing import Any

from . import (
    calc,
    compare_roles,
    dates_delta,
    enum_repr,
)

mutations: list[Any] = [
    calc.Mutation,
    compare_roles.Mutation,
    dates_delta.Mutation,
    enum_repr.Mutation,
]
