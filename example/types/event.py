from ariadne_graphql_modules import GraphQLID, GraphQLObject

from ..scalars.datetime import DateTimeScalar


class EventType(GraphQLObject):
    id: GraphQLID
    message: DateTimeScalar

    __aliases__ = {"message": "payload"}
