from typing import Any

from .models.category import Category
from .models.group import Group
from .models.user import User


def get_data() -> dict[str, dict[int, Any]]:
    return {
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
                email="johndoe@example.com",
                group_id=1,
            ),
            2: User(
                id=2,
                username="Alice",
                email="alice@example.com",
                group_id=1,
            ),
            3: User(
                id=3,
                username="Bob",
                email="b0b@example.com",
                group_id=2,
            ),
            4: User(
                id=4,
                username="Mia",
                email="mia@example.com",
                group_id=2,
            ),
        },
    }
