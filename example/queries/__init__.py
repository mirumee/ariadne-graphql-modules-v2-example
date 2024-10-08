from typing import Any

from . import calendar, categories, groups, hello, models, posts, search, users

queries: Any = [
    calendar.Query,
    categories.Query,
    groups.Query,
    hello.Query,
    models.Query,
    posts.Query,
    search.Query,
    users.Query,
]
