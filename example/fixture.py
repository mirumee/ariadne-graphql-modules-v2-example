from typing import Any

from .models.group import Group
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
