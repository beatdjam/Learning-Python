from marshmallow import Schema, fields


class SchemaRouter:
    """Swagger出力サンプル
    ---
    name: Sample
    get:
        description: Sample
        responses:
            200:
                description: All exist_id to be returned
                content:
                    application/json:
                        schema:
                            $ref: "#/components/schemas/SampleSchema"
    """

    @staticmethod
    async def on_get(req, resp):
        resp.media = SampleSchema().dump({"user_id": 1, "user_name": "hogetaro"})


class SampleSchema(Schema):
    user_id = fields.Integer()
    user_name = fields.Str()
