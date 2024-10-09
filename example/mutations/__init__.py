from typing import Any

from . import (
    calc,
    compare_roles,
    dates_delta,
)

mutations: list[Any] = [
    calc.Mutation,
    compare_roles.Mutation,
    dates_delta.Mutation,
]
