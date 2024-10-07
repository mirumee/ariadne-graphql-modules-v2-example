from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler
from starlette.middleware.cors import CORSMiddleware

from .schema import schema


app = CORSMiddleware(
    GraphQL(
        schema,
        debug=True,
        websocket_handler=GraphQLTransportWSHandler(),
    ),
    allow_origins="*",
)
