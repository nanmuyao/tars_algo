#!/usr/bin/env python
import uuid
import time
import urllib
import asyncio
import websockets
import json
import hmac
import base64
import hashlib
import gzip
import traceback

from collections import OrderedDict

def generate_signature(host, method, params, request_path, secret_key):
    """Generate signature of huobi future.
    
    Args:
        host: api domain url.PS: colo user should set this host as 'api.hbdm.com',not colo domain.
        method: request method.
        params: request params.
        request_path: "/notification"
        secret_key: api secret_key

    Returns:
        singature string.

    """
    host_url = urllib.parse.urlparse(host).hostname.lower()
    sorted_params = sorted(params.items(), key=lambda d: d[0], reverse=False)
    encode_params = urllib.parse.urlencode(sorted_params)
    payload = [method, host_url, request_path, encode_params]
    payload = "\n".join(payload)
    payload = payload.encode(encoding="UTF8")
    secret_key = secret_key.encode(encoding="utf8")
    digest = hmac.new(secret_key, payload, digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest)
    signature = signature.decode()
    return signature

async def subscribe(url, access_key, secret_key, subs, callback=None, auth=False):
    """ Huobi Future subscribe websockets.

    Args:
        url: the url to be signatured.
        access_key: API access_key.
        secret_key: API secret_key.
        subs: the data list to subscribe.
        callback: the callback function to handle the ws data received. 
        auth: True: Need to be signatured. False: No need to be signatured.

    """
    async with websockets.connect(url) as websocket:
        if auth:
            timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
            data = {
                "AccessKeyId": access_key,
                "SignatureMethod": "HmacSHA256",
                "SignatureVersion": "2",
                "Timestamp": timestamp
            }
            sign = generate_signature(url,"GET", data, "/notification", secret_key)
            data["op"] = "auth"
            data["type"] = "api"
            data["Signature"] = sign
            msg_str = json.dumps(data)
            await websocket.send(msg_str)
            print(f"send: {msg_str}")
        for sub in subs:
            sub_str = json.dumps(sub)
            await websocket.send(sub_str)
            print(f"send: {sub_str}")
        while True:
            rsp = await websocket.recv()
            data = json.loads(gzip.decompress(rsp).decode())
            #print(f"recevie<--: {data}")
            if "op" in data and data.get("op") == "ping":
                pong_msg = {"op": "pong", "ts": data.get("ts")}
                await websocket.send(json.dumps(pong_msg))
                print(f"send: {pong_msg}")
                continue
            if "ping" in data: 
                pong_msg = {"pong": data.get("ping")}
                await websocket.send(json.dumps(pong_msg))
                print(f"send: {pong_msg}")
                continue
            rsp = await callback(data)


class ChPipeline:
    def __init__(self):
        pass



class ChETHUSDT1min(ChPipeline):
    def __init__(self):
        self.klines = []
        self.price = []
        self.klines = OrderedDict()
        self.max_close = 0
        self.min_close = 0

    def ding(self, msg):
        from dingtalkchatbot.chatbot import DingtalkChatbot
        # WebHook地址
        webhook =  'https://oapi.dingtalk.com/robot/send?access_token=d3b925bbeeed4a0c58bcf38cea6e2c0d98b4876feab1ec860ed9ed662f7e41a1'
        secret = 'SEC1a47be1311e8fa8e97cdc6dbc2d17110814a3d56df6478ed46ad9a7844d574fb'
        # 初始化机器人小丁
        xiaoding = DingtalkChatbot(webhook)  # 方式一：通常初始化方式
        xiaoding = DingtalkChatbot(webhook, secret=secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）
        # xiaoding = DingtalkChatbot(webhook, pc_slide=True)  # 方式三：设置消息链接在PC端侧边栏打开（v1.5以上新功能）
        # Text消息@所有人
        res = xiaoding.send_text(msg)
        print(res)

    def append_data(self, kline, **kwargs):
        ts = kline.get('ts')
        close = kline.get('tick', {}).get('close')
        if not ts or not close:
            # filter data
            return
        self.klines[ts] = close
        print(f"klines {self.klines}")
        self.strategy()

    def strategy(self):
        # 3 分钟
        prices = self.klines.values()
        max_close = max(prices)
        min_close = min(prices)
        if (max_close - min_close) > 10:
            if not self.max_close and not self.min_close:
                print(f"max_close {max_close} min_close {min_close}")
                self.ding(f"3 min max_close:{max_close} - min_close:{min_close} diff:{max_close - min_close}")
            else:
                if self.max_close != max_close and self.min_close != min_close:
                    print(f"max_close {max_close} min_close {min_close}")
                    self.ding(f"3 min max_close:{max_close} - min_close:{min_close} diff:{max_close - min_close}")
            self.max_close = max_close
            self.min_close = min_close

        tss = self.klines.keys()
        max_ts = int(max(tss) / 1000)
        min_ts = int(min(tss) / 1000)
        ts_distance = 3 * 60
        if (max_ts - min_ts) > ts_distance:
            # 清理kline
            new_klines = OrderedDict()
            pivot_ts = max_ts - ts_distance
            for ts, close in self.klines.items():
                if int(ts / 1000) > pivot_ts:
                    new_klines[ts] = close
            self.klines = new_klines

        print(f"strategy: {self.klines}")

ch = ChETHUSDT1min()
# close = 0

# while True:
#     ts = int(time.time() * 1000)
#     close=close + 1
#     tick = {
#             'id': 1617549180, 
#             'mrid': 22382413742, 
#             'open': 2084.95, 
#             'close': close, 
#             'high': 2084.95, 
#             'low': 2084.95, 
#             'amount': 0, 
#             'vol': 0, 
#             'trade_turnover': 0, 
#             'count': 0
#         }
#     kline = {
#         'ch': 'market.ETH-USDT.kline.1min', 
#         'ts': ts, 
#         'tick': tick
#         }
#     ch.append_data(kline)
#     ch.strategy()
#     import time
#     time.sleep(3)

async def handle_ws_data(*args, **kwargs):
    """ callback function
    Args:
        args: values
        kwargs: key-values.
    """
    print("callback param", *args)
    print(**kwargs)
    ch.append_data(*args, **kwargs)
    # ChPipeline(*args, **kwargs)


# https://huobiapi.github.io/docs/usdt_swap/v1/cn/#websocket
if __name__ == "__main__":
    ####  input your access_key and secret_key below:
    access_key  = ""
    secret_key  = ""

    # 如果api.hbdm.com无法访问，可以使用api.btcgateway.pro来做调试，AWS服务器用户推荐使用api.hbdm.vn；
    market_url = 'wss://api.hbdm.com/linear-swap-ws'
 #   Q14: Will the quarter contract of the delivery contract be converted to the next week contract, will it be notified or changged by WS?
#If a quarterly contract such as BTC_CQ is converted to the next week contract BTC_NW, WS will not automatically notify you, you need to change the subscription to BTC_NW.
    market_subs = [
                {
                    "sub": "market.ETH-USDT.kline.1min",
                    "id": str(uuid.uuid1())
                },
                # {
                #     "sub": "market.ETH-USDT.depth.step6",
                #     "id": str(uuid.uuid1())
                # },
                # {
                #     "sub": "market.ETH-USDT.detail",
                #     "id": str(uuid.uuid1())
                # }
            ]

    #order_subs = [
    #            {
    #                "op": "sub",
    #                "cid": str(uuid.uuid1()),
    #                "topic": "orders.EOS"
    #            },
    #            {
    #                "op": "sub",
    #                "cid": str(uuid.uuid1()),
    #                "topic": "positions.EOS"
    #            },
    #            {
    #                "op": "sub",
    #                "cid": str(uuid.uuid1()),
    #                "topic": "accounts.EOS"
    #            }

    #        ]
    order_subs = []

    while True: 
        try:
            asyncio.get_event_loop().run_until_complete(
                subscribe(
                    market_url, access_key,  secret_key, market_subs, handle_ws_data, auth=False
                )
            )
            #asyncio.get_event_loop().run_until_complete(subscribe(order_url, access_key,  secret_key, order_subs, handle_ws_data, auth=True))
        #except (websockets.exceptions.ConnectionClosed):
        except Exception as e:
            traceback.print_exc()
            print('websocket connection error. reconnect rightnow')
