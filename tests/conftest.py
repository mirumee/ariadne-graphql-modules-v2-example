import pytest
from graphql import graphql

from example.schema import schema


@pytest.fixture
def exec_query():
    async def exec_query_(
        document: str,
        variables: dict | None = None,
        operation: str | None = None,
    ):
        return await graphql(
            schema,
            document,
            variable_values=variables,
            operation_name=operation,
        )

    return exec_query_
