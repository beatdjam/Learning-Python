class Sample:
    @staticmethod
    async def on_get(req, resp):
        resp.text = f"GET, Sample!!"

    @staticmethod
    async def on_post(req, resp):
        resp.text = f"POST, Sample!!"

    @staticmethod
    async def on_request(req, resp):
        resp.text = f"Any, Sample!!"