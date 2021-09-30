import falcon

import json

from marshmallow import Schema, fields


# schema
class HealthSchema(Schema):
    status: fields.Str = fields.Str(required=True)
    message: fields.Str = fields.Str(required=True)


class HealthCheck:
    def on_get(self, req, resp):
        """A cute furry animal endpoint.
        ---
        description: Get a random pet
        responses:
            200:
                description: A pet to be returned
                schema: PetSchema
        """
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({"status": resp.status, "message": "healthy"})
