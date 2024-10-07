from typing import Any

from . import compare_roles
from . import dates_delta

mutations: list[Any] = [
    compare_roles.Mutation,
    dates_delta.Mutation,
]
