# @Time :  22:30
# __authou__= 'zhangcheng'
# conding = utf-8
import mitmproxy.http
from mitmproxy import http

class Event:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" \
                in flow.request.url and "x=" in flow.request.url:
            with open("data.json", encoding="utf-8") as f:
                flow.response = http.HTTPResponse.make(
                    # 状态码
                    200,
                    f.read()
                )


addons = [
    Event()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p', '8001', '-s', __file__])