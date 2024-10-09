import pytest


@pytest.mark.asyncio
async def test_query_calc_mutation(exec_query):
    result = await exec_query(
        """
        mutation {
            calc(input: {a: 4, b: 3, op: MUL})
        }
        """
    )
    assert result.data == {"calc": 12}


@pytest.mark.asyncio
async def test_query_compare_roles_mutation(exec_query):
    result = await exec_query(
        """
        mutation {
            compareRoles(a: ADMIN, b: MEMBER)
        }
        """
    )
    assert result.data == {"compareRoles": "A_GREATER"}


@pytest.mark.asyncio
async def test_query_dates_delta_mutation(exec_query):
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
