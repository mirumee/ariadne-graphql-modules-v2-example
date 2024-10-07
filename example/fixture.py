from typing import Any

from .models.category import Category
from .models.group import Group
from .models.post import Post
from .models.user import User


def get_data() -> dict[str, dict[int, Any]]:
    return {
        "groups": {
            1: Group(
                id=1,
                name="Admins",
                is_admin=True,
            ),
            2: Group(
                id=2,
                name="Members",
                is_admin=False,
            ),
        },
        "users": {
            1: User(
                id=1,
                username="JohnDoe",
                group_id=1,
                role="ADMIN",
            ),
            2: User(
                id=2,
                username="Alice",
                group_id=1,
                role="ADMIN",
            ),
            3: User(
                id=3,
                username="Bob",
                group_id=2,
                role="MEMBER",
            ),
            4: User(
                id=4,
                username="Mia",
                group_id=2,
                role="GUEST",
            ),
        },
        "categories": {
            1: Category(
                id=1,
                name="First category",
                parent_id=None,
            ),
            2: Category(
                id=2,
                name="Second category",
                parent_id=None,
            ),
            3: Category(
                id=3,
                name="Child category",
                parent_id=1,
            ),
            4: Category(
                id=4,
                name="Other child category",
                parent_id=1,
            ),
        },
        "posts": {
            1: Post(
                id=1,
                message="Lorem ipsum",
                category_id=1,
                poster_id=1,
            ),
            2: Post(
                id=2,
                message="Dolor met",
                category_id=2,
                poster_id=2,
            ),
            3: Post(
                id=3,
                message="Sit amet",
                category_id=3,
                poster_id=3,
            ),
            4: Post(
                id=4,
                message="Elit",
                category_id=4,
                poster_id=4,
            ),
        },
    }
