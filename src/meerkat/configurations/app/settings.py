from serviceregistry.services import Props as BaseProps

from meerkat.configurations.infrastructure.db import DataBaseService
from meerkat.configurations.infrastructure.di.service import DiService
from meerkat.configurations.infrastructure.environment import EnvironmentService
from meerkat.configurations.infrastructure.logging import LoggingService
from meerkat.configurations.infrastructure.rest.health.registry import HealthService
from meerkat.configurations.infrastructure.rest.post.registry import PostService
from meerkat.configurations.infrastructure.rest.swagger.registry import SwaggerService

services = [
    LoggingService(),
    EnvironmentService(),
    DataBaseService(),
    DiService(),
    PostService(),
    HealthService(),
    SwaggerService(),
]


class Props(BaseProps):
    DI_PROVIDER = 0
    FALCON = 1

    APP_URL = "APP_URL"

    MONGO_HOST = "MONGO_HOST"
    MONGO_PORT = "MONGO_PORT"
    MONGO_DB = "MONGO_DB"
