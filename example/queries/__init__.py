from typing import Any

from . import calendar, categories, groups, hello, posts, users

queries: Any = [
    calendar.Query,
    categories.Query,
    groups.Query,
    hello.Query,
    posts.Query,
    users.Query,
]
