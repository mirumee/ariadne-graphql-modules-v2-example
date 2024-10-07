import pytest


@pytest.mark.asyncio
async def test_query_hello_field(exec_query):
    result = await exec_query(
        """
        mutation {
            datesDelta(a: "2022-10-21", b: "2012-07-14") {
                years months days
            }
        }
        """
    )
    assert result.data == {
        "datesDelta": {
            "years": 10,
            "months": 123,
            "days": 3751,
        },
    }
