from meerkat.domain.common.value_objects import Body, Id, Title
from meerkat.domain.post.entities.exceptions import PublishingFailedException


class Post:
    id: Id
    title: Title
    body: Body
    published: bool = False

    @staticmethod
    def create(id: Id, title: Title, body: Body):
        instance = Post()
        instance.id = id
        instance.title = title
        instance.body = body

        return instance

    def publish(self):
        if not self.title.is_valid():
            raise PublishingFailedException("title is invalid")

        if not self.id.is_valid():
            raise PublishingFailedException("Id is invalid")

        self.published = True

    def is_published(self) -> bool:
        return self.published


"""
todo slugify title
"""
