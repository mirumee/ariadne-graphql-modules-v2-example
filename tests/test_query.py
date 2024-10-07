import pytest


@pytest.mark.asyncio
async def test_query_hello_field(exec_query):
    result = await exec_query("{ hello }")
    assert result.data == {"hello": "Hello world!"}


@pytest.mark.asyncio
async def test_query_groups_field(exec_query):
    result = await exec_query("{ groups(filter: ALL) { id name } }")
    assert result.data == {
        "groups": [
            {
                "id": "1",
                "name": "Admins",
            },
            {
                "id": "2",
                "name": "Members",
            },
        ],
    }


@pytest.mark.asyncio
async def test_query_groups_field_all_arg(exec_query):
    result = await exec_query("{ groups(filter: ALL) { id name } }")
    assert result.data == {
        "groups": [
            {
                "id": "1",
                "name": "Admins",
            },
            {
                "id": "2",
                "name": "Members",
            },
        ],
    }


@pytest.mark.asyncio
async def test_query_groups_field_admin_arg(exec_query):
    result = await exec_query("{ groups(filter: ADMIN) { id name } }")
    assert result.data == {
        "groups": [
            {
                "id": "1",
                "name": "Admins",
            },
        ],
    }


@pytest.mark.asyncio
async def test_query_groups_field_member_arg(exec_query):
    result = await exec_query("{ groups(filter: MEMBER) { id name } }")
    assert result.data == {
        "groups": [
            {
                "id": "2",
                "name": "Members",
            },
        ],
    }


@pytest.mark.asyncio
async def test_query_user(exec_query):
    result = await exec_query('{ user(id: "2") { id username group { name } } }')
    assert result.data == {
        "user": {
            "id": "2",
            "username": "Alice",
            "group": {
                "name": "Admins",
            },
        },
    }


@pytest.mark.asyncio
async def test_query_users(exec_query):
    result = await exec_query("{ users { id username group { name } } }")
    assert result.data == {
        "users": [
            {
                "id": "1",
                "username": "JohnDoe",
                "group": {
                    "name": "Admins",
                },
            },
            {
                "id": "2",
                "username": "Alice",
                "group": {
                    "name": "Admins",
                },
            },
            {
                "id": "3",
                "username": "Bob",
                "group": {
                    "name": "Members",
                },
            },
            {
                "id": "4",
                "username": "Mia",
                "group": {
                    "name": "Members",
                },
            },
        ],
    }


@pytest.mark.asyncio
async def test_query_categories_field(exec_query):
    result = await exec_query(
        "{ categories { id name children { id name } posts { id content } } }"
    )
    assert result.data == {
        "categories": [
            {
                "id": "1",
                "name": "First category",
                "children": [
                    {
                        "id": "3",
                        "name": "Child category",
                    },
                    {
                        "id": "4",
                        "name": "Other child category",
                    },
                ],
                "posts": [
                    {
                        "id": "1",
                        "content": "Lorem ipsum",
                    },
                ],
            },
            {
                "id": "2",
                "name": "Second category",
                "children": [],
                "posts": [
                    {
                        "id": "2",
                        "content": "Dolor met",
                    },
                ],
            },
        ],
    }


@pytest.mark.asyncio
async def test_query_category_field(exec_query):
    result = await exec_query(
        '{ category(id: "1") { id name children { id name } posts { id content } } }'
    )
    assert result.data == {
        "category": {
            "id": "1",
            "name": "First category",
            "children": [
                {
                    "id": "3",
                    "name": "Child category",
                },
                {
                    "id": "4",
                    "name": "Other child category",
                },
            ],
            "posts": [
                {
                    "id": "1",
                    "content": "Lorem ipsum",
                },
            ],
        },
    }
