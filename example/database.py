from typing import Any

from .fixture import get_data


class DataBase:
    _data: dict[str, dict[int, Any]]
    _id: int

    def __init__(self, data: dict[str, dict[int, Any]], counter: int = 0):
        self._data = data
        self._id = counter

    async def get_row(self, table: str, **kwargs) -> Any:
        assert kwargs, "use kwargs to filter"

        for row in self._data[table].values():
            for attr, value in kwargs.items():
                if getattr(row, attr) != value:
                    continue

                return row

        return None

    async def get_all(self, table: str, **kwargs) -> list[Any]:
        if not kwargs:
            return list(self._data[table].values())

        results: list[Any] = []
        for row in self._data[table].values():
            for attr, value in kwargs.items():
                if getattr(row, attr) != value:
                    continue

                results.append(row)

        return results

    async def insert(self, table: str, obj: Any):
        assert obj.id is None, "obj.id attr must be None"

        self._id += 1
        obj.id = self._id

        self._data[table][obj.id] = obj

    async def update(self, table: str, obj: Any):
        self._data[table][obj.id] = obj

    async def delete(self, table: str, id: int):
        self._data[table].pop(id, None)


db = DataBase(get_data(), 1000)
