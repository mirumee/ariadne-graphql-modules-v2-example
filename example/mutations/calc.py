from enum import StrEnum

from ariadne_graphql_modules import GraphQLInput, GraphQLObject
from graphql import GraphQLResolveInfo


class CalcOperation(StrEnum):
    ADD = "add"
    SUB = "sub"
    MUL = "mul"


class CalcInput(GraphQLInput):
    a: int
    b: int
    op: CalcOperation


class Mutation(GraphQLObject):
    @GraphQLObject.field(name="calc")
    @staticmethod
    def resolve_calc(obj, info: GraphQLResolveInfo, *, input: CalcInput) -> int:
        if input.op == CalcOperation.ADD:
            return input.a + input.b
        if input.op == CalcOperation.SUB:
            return input.a - input.b
        if input.op == CalcOperation.MUL:
            return input.a * input.b

        return 0
