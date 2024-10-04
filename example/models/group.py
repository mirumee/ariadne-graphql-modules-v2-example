from dataclasses import dataclass


@dataclass
class Group:
    id: int
    name: str
    is_admin: bool
