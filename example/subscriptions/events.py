import random
from asyncio import sleep
from typing import AsyncGenerator
from datetime import datetime

from ariadne_graphql_modules import GraphQLSubscription
from graphql import GraphQLResolveInfo

from ..types.event import EventType


class Subscription(GraphQLSubscription):
    event: EventType

    @GraphQLSubscription.source("event")
    @staticmethod
    async def source_event(obj, info: GraphQLResolveInfo) -> AsyncGenerator[int, None]:
        i = 0

        while True:
            i += 1
            yield i
            await sleep(float(random.randint(1, 50)) / 10)

    @GraphQLSubscription.resolver("event")
    @staticmethod
    async def resolve_event(obj: int, info: GraphQLResolveInfo) -> dict:
        return {"id": obj, "payload": datetime.now()}
