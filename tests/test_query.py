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
    result = await exec_query('{ user(id: "2") { id username role group { name } } }')
    assert result.data == {
        "user": {
            "id": "2",
            "username": "Alice",
            "role": "ADMIN",
            "group": {
                "name": "Admins",
            },
        },
    }


@pytest.mark.asyncio
async def test_query_users(exec_query):
    result = await exec_query("{ users { id username role group { name } } }")
    assert result.data == {
        "users": [
            {
                "id": "1",
                "username": "JohnDoe",
                "role": "ADMIN",
                "group": {
                    "name": "Admins",
                },
            },
            {
                "id": "2",
                "username": "Alice",
                "role": "ADMIN",
                "group": {
                    "name": "Admins",
                },
            },
            {
                "id": "3",
                "username": "Bob",
                "role": "MEMBER",
                "group": {
                    "name": "Members",
                },
            },
            {
                "id": "4",
                "username": "Mia",
                "role": "GUEST",
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


@pytest.mark.asyncio
async def test_query_search(exec_query):
    result = await exec_query(
        """
        query Search {
            search(query: "a") {
                __typename
                summary
                ... on User {
                    id
                    username
                }
                ... on Group {
                    id
                    name
                }
                ... on Post {
                    id
                    content
                }
            }
        }
        """
    )
    assert result.data == {
        "search": [
            {
                "__typename": "Group",
                "summary": "#1: Admins",
                "id": "1",
                "name": "Admins",
            },
            {
                "__typename": "Post",
                "summary": "#3: Sit amet",
                "id": "3",
                "content": "Sit amet",
            },
            {
                "__typename": "User",
                "summary": "#2: Alice",
                "id": "2",
                "username": "Alice",
            },
            {
                "__typename": "User",
                "summary": "#4: Mia",
                "id": "4",
                "username": "Mia",
            },
        ],
    }


@pytest.mark.asyncio
async def test_query_models(exec_query):
    result = await exec_query(
        """
        query Models {
            models {
                __typename
                ... on Category {
                    id
                    name
                }
                ... on User {
                    id
                    username
                }
                ... on Group {
                    id
                    name
                }
                ... on Post {
                    id
                    content
                }
            }
        }
        """
    )
    assert result.data == {
        "models": [
            {
                "__typename": "Category",
                "id": "1",
                "name": "First category",
            },
            {
                "__typename": "Category",
                "id": "2",
                "name": "Second category",
            },
            {
                "__typename": "Category",
                "id": "3",
                "name": "Child category",
            },
            {
                "__typename": "Category",
                "id": "4",
                "name": "Other child category",
            },
            {
                "__typename": "Group",
                "id": "1",
                "name": "Admins",
            },
            {
                "__typename": "Group",
                "id": "2",
                "name": "Members",
            },
            {
                "__typename": "Post",
                "id": "1",
                "content": "Lorem ipsum",
            },
            {
                "__typename": "Post",
                "id": "2",
                "content": "Dolor met",
            },
            {
                "__typename": "Post",
                "id": "3",
                "content": "Sit amet",
            },
            {
                "__typename": "Post",
                "id": "4",
                "content": "Elit",
            },
            {
                "__typename": "User",
                "id": "1",
                "username": "JohnDoe",
            },
            {
                "__typename": "User",
                "id": "2",
                "username": "Alice",
            },
            {
                "__typename": "User",
                "id": "3",
                "username": "Bob",
            },
            {
                "__typename": "User",
                "id": "4",
                "username": "Mia",
            },
        ],
    }
