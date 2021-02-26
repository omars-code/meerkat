import falcon
from falcon_marshmallow import EmptyRequestDropper, JSONEnforcer
from injector_provider import InjectorProvider
from registry.services import Container, Registry

from meerkat.configurations.app import settings
from meerkat.configurations.app.middlewares import RequestLoader


def create_app():
    return falcon.API(
        middleware=[JSONEnforcer(), EmptyRequestDropper(), RequestLoader()]
    )


app = create_app()


def create_container():
    container = Container()

    container.set(settings.Props.DI_PROVIDER, InjectorProvider())
    container.set(settings.Props.FALCON, app)
    return container


container = create_container()


def boot():
    service_registry = Registry()

    for service in settings.services:
        service_registry.register(service)

    service_registry.boot(container)


boot()
