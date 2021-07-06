from serviceregistry.services import BootableService, Container

from meerkat.configurations.app import settings
from meerkat.configurations.infrastructure.rest.post.definitions import PostConfigurator
from meerkat.entrypoints.rest.post.resources import Post, PostCollection


class PostService(BootableService):
    def boot(self, container: Container):
        provider = container.get(settings.Props.DI_PROVIDER)
        provider.add_configurator(PostConfigurator)

    def post_boot(self, container):
        falcon = container.get(settings.Props.FALCON)
        provider = container.get(settings.Props.DI_PROVIDER)

        injector = provider.get_injector()

        falcon.add_route("/v1/posts", injector.get(PostCollection))
        falcon.add_route("/v1/posts/{id}/publish", injector.get(Post))
