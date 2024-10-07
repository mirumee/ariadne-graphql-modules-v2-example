from dataclasses import dataclass


@dataclass
class Post:
    id: int
    message: str
    category_id: int | None
    poster_id: int | None
