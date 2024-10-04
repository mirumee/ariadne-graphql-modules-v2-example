from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    email: str
    group_id: int
