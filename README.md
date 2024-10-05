# ariadne-graphql-modules-v2-example

An example GraphQL API implemented with Ariadne GraphQL Modules v2.

This API aims to use ALL features from GraphQL Modules v2. It can also be used as a reference for other developers.


# Problems found

## `list[SchemaType]` type in `make_executable_schema`

`list` is [invariant in mypy](https://mypy.readthedocs.io/en/stable/common_issues.html#variance). A list of `type[GraphQLObject]`, like one from the `example.queries.__init__` produces an error because `list[type[GraphQLObject]]` is incompatible with `list[type[GraphQLType]]`.


## Resolvers need to be `@classmethod` or `@staticmethod` to keep linters happy.

Linters will scream that resolver method decorated with `@ObectType.resolver` is missing `self` first attribute.

