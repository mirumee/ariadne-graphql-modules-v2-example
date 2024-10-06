from ariadne_graphql_modules import GraphQLObject
from ariadne import gql
from graphql import GraphQLResolveInfo

from ..database import db
from ..models.category import Category


class CategoryType(GraphQLObject):
    __schema__ = gql(
        """
        type Category {
            id: ID!
            name: String!
            parent: Category
            children: [Category!]!
        }
        """
    )

    @GraphQLObject.resolver("parent", "CategoryType")
    @staticmethod
    async def resolve_parent(
        obj: Category, info: GraphQLResolveInfo
    ) -> Category | None:
        if not obj.parent_id:
            return None

        return await db.get_row("categories", id=obj.parent_id)

    @GraphQLObject.resolver("children", list["CategoryType"])
    @staticmethod
    async def resolve_children(
        obj: Category, info: GraphQLResolveInfo
    ) -> list[Category]:
        return await db.get_all("categories", parent_id=obj.id)
