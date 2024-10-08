from typing import Any

from ariadne_graphql_modules import GraphQLInterface

from ..models.group import Group
from ..models.post import Post
from ..models.user import User


class SearchResultInterface(GraphQLInterface):
    summary: str

    @staticmethod
    def resolve_type(obj: Any, *_) -> str:
        if isinstance(obj, Group):
            return "Group"

        if isinstance(obj, Post):
            return "Post"

        if isinstance(obj, User):
            return "User"

        raise TypeError(f"Unsupported type: {type(obj)}")
