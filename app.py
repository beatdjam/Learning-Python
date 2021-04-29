# Declare a Web Service
import responder

from router.SampleRouter import Sample
from router.SchemaRouter import SchemaRouter, SampleSchema

api = responder.API(
    openapi='3.0.0',
    docs_route='/docs',
)


# Hello World!
@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"


# Accept Route Arguments
@api.route("/hello/{who}")
def hello_to(req, resp, *, who):
    resp.text = f"hello, {who}!"


# Returning JSON / YAML
# resp.mediaに値を詰めるとJSONにシリアライズして返却する
# clientがyamlを要求してきた場合(Accept : application/x-yamlなど)はyamlを返す
@api.route("/hello/{who}/json")
def hello_to(req, resp, *, who):
    resp.media = {"hello": who}


# Rendering a Template
# テンプレートのhtmlはtemplates配下に入れる
# テンプレートの文字列は {{ variable }} の形で指定する
@api.route("/hello/{who}/html")
def hello_html(req, resp, *, who):
    resp.html = api.template('hello.html', who=who)


# Setting Response Status Code
@api.route("/416")
def teapot(req, resp):
    resp.status_code = api.status_codes.HTTP_416


# Setting Response Headers
@api.route("/pizza")
def pizza_pizza(req, resp):
    resp.headers['X-Pizza'] = '42'


# Receiving Data & Background Tasks
# process_dataをバックグラウンドで実行しながら即時レスポンスする
@api.route("/incoming")
async def receive_incoming(req, resp):
    @api.background.task
    def process_data(data):
        f = open('./{}'.format(data['file']['filename']), 'w')
        f.write(data['file']['content'].decode('utf-8'))
        f.close()

    data = await req.media(format='files')
    process_data(data)

    resp.media = {'success': True}


# on_{HTTP Method}で対応するHTTP Methodの処理が定義できる
# on_requestを定義した場合、未定義のものはすべてそこに振り分けられる
@api.route("/class/{who}")
class Class:
    @staticmethod
    async def on_get(req, resp, *, who):
        resp.text = f"GET, {who}!"

    @staticmethod
    async def on_post(req, resp, *, who):
        resp.text = f"POST, {who}!"

    @staticmethod
    async def on_request(req, resp, *, who):
        resp.text = f"Any, {who}!"


# クエリパラメータの取得
@api.route('/param')
def param_sample(req, resp):
    print(req.params)


# 別ファイルのClassでルーティング
api.add_route("/sample", Sample)
api.add_route('/schema', SchemaRouter)

api.schema("SampleSchema")(SampleSchema)

# Run the Server
if __name__ == '__main__':
    api.run()
    # address、 portを設定する場合
    # api.run(address='0.0.0.0', port=5042)
