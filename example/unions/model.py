from typing import Any

from ariadne_graphql_modules import GraphQLUnion

from ..models.category import Category
from ..models.group import Group
from ..models.post import Post
from ..models.user import User
from ..types.category import CategoryType
from ..types.group import GroupType
from ..types.post import PostType
from ..types.user import UserType


class Model(GraphQLUnion):
    __types__ = (CategoryType, GroupType, PostType, UserType)

    @staticmethod
    def resolve_type(obj: Any, *_) -> str:
        if isinstance(obj, Category):
            return "Category"

        if isinstance(obj, Group):
            return "Group"

        if isinstance(obj, Post):
            return "Post"

        if isinstance(obj, User):
            return "User"

        raise TypeError(f"Unsupported type: {type(obj)}")
