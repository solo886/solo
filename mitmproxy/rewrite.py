# @Time :  22:30
# __authou__= 'zhangcheng'
# conding = utf-8
import json
import mitmproxy.http


class Event:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" \
                in flow.request.url and "x=" in flow.request.url:
            base_data = json.loads(flow.response.text)
            base_data["data"]["items"][0]["quote"]["name"] = "张诚"
            base_data["data"]["items"][0]["quote"]["percent"] = "0.01"
            base_data["data"]["items"][1]["quote"]["percent"] = "-0.01"
            base_data["data"]["items"][2]["quote"]["percent"] = "0"
            flow.response.text = json.dumps(base_data)


addons = [
    Event()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p', '8001', '-s', __file__])