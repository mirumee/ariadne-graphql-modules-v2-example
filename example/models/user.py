from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    group_id: int
    role: str
