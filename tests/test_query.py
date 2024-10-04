import pytest


@pytest.mark.asyncio
async def test_query_hello_field(exec_query):
    result = await exec_query("{ hello }")
    assert result.data == {"hello": "Hello world!"}
