# ariadne-graphql-modules-v2-example

An example GraphQL API implemented with Ariadne GraphQL Modules v2.

This API aims to use most features from GraphQL Modules v2. It can also be used as a reference for other developers.


# Problems found

## `list[SchemaType]` type in `make_executable_schema`

`list` is [invariant in mypy](https://mypy.readthedocs.io/en/stable/common_issues.html#variance). A list of `type[GraphQLObject]`, like one from the `example.queries.__init__` produces an error because `list[type[GraphQLObject]]` is incompatible with `list[type[GraphQLType]]`.

Replacing `list` with `Iterable` may be enough to fix this.


## Resolvers need to be decorated with `@classmethod` or `@staticmethod` to keep linters happy

Linters will scream that resolver method decorated with `@ObectType.resolver` is missing `self` first attribute.

This may require mypy plugin to fix, but its good idea to look how Graphene and Strawberry are solving this.


## Missing dedicated `Mutation` type

We could have a mutation type like this:

```python
class ConcatMutation(GraphQLMutation):
    __graphql_name__: str = "concat"

    def mutate(info: GraphQLResolveInfo, *, arg1: str, arg2: str) -> str:
        return arg1 + arg2
```

This would be more intuitive way to define mutations than current approach of having `MutationType(GraphQLObject)` with multiple methods.


## Object type docs don't document interface usage for objects with schema

According to interface docs, this is valid:

```python
class PostType(GraphQLObject, SearchResultInterface):
    __schema__ = gql(
        """
        type Post {
            id: ID!
            content: String!
            category: Category
            poster: User
        }
        """
    )
```

But it will fail to validate with following error:

```
ValueError: Class 'PostType' defines '__schema__' attribute with declaration for an invalid GraphQL type. ('ObjectTypeDefinitionNode' != 'InterfaceTypeDefinitionNode')
```

This points to `SearchResultInterface` validation logic overriding `GraphQLObject`.

Docs also need to be updated to show example for `GraphQLObject` with interface.

Interface's docs are also mentioning `subscription` in its parts which needs to be edited out.

Interface's docs should also have example of usage with `GraphQLObject`, even if only as "See the `GraphQLObject` docs for usage example." link somewhere in it.


## Interfaces need to be explicitly passed to `make_executable_schema`

Given GraphQL object definition:

```python
class PostType(GraphQLObject, SearchResultInterface):
    ...
```

`make_executable_schema` will fail with:

```
TypeError: Unknown type 'SearchResultInterface'.
```

`GraphQLObject`'s model creation could see if parent types include subclasses of `GraphQLInterface` and include them.


## `GraphQLUnion` docs should have example of union type implementing `resolve_type`

We do this already for `GraphQLInterface`, it would help if `GraphQLUnion` also did it.
