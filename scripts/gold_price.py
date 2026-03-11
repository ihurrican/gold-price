# -*- coding: utf-8 -*-
import requests
from datetime import datetime, timezone
import json
import time
import argparse
import sys
import io
from __init__ import __version__
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
__version__ = __version__

header = {
    'authority': 'api.jijinhao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'referer': 'https://quote.cngold.org/gjs/yhzhj.html'
}


# API接口
data_url = "https://api.jijinhao.com/quoteCenter/"

# 查询数据编码
data = []   
data.append({"code":"JO_9753","showName": "国内黄金"})
data.append({"code":"JO_9754","showName": "国内白银"})
data.append({"code":"JO_74","showName": "国内铂金"})
data.append({"code":"JO_92233","showName": "国际黄金"})
data.append({"code":"JO_92232","showName": "国际白银"})
data.append({"code":"JO_92229","showName": "国际铂金"})

def time_to_date(time):
    timestamp = time / 1000 + 24 * 60 * 60
    return datetime.fromtimestamp(timestamp, timezone.utc).strftime('%Y-%m-%d')

# 获取当天金价数据(黄金、白银、铂金等)，数据来源金投网
def get_gold_price():
    # 金价数据
    result_data = []
    codes_str = ""
    for item in data:
        codes_str += item["code"] + ","
    # 获取毫秒级时间戳
    timestamp_ms = int(time.time() * 1000)
    res = requests.get(data_url + "realTime.htm?codes="+codes_str + "&_=" + str(time),headers = header)
    quote_json_str = res.content.decode("utf-8")
    comma_index = quote_json_str.find('{')
    if comma_index > -1:
        quote_json_str = quote_json_str[comma_index:]
    quote_json = json.loads(quote_json_str)
    
    for item in data:
        code = item["code"]
        res_json = quote_json[code]
        result_data.append({
            "编号": res_json["code"], 
            "名字": item["showName"], 
            "时间": time_to_date(res_json["time"]), 
            "单位": res_json["unit"],
            "最新价": res_json["q63"],
            "买入价": res_json["q5"],
            "卖出价": res_json["q6"],
            "涨跌额": round(res_json["q70"], 2),
            "涨跌幅": round(res_json["q80"], 2),
            "开盘价": res_json["q1"],
            "最高价": res_json["q3"],
            "最低价": res_json["q4"],
            "昨收价": res_json["q2"],
        })
    return result_data

# 获取贵金属历史数据(黄金、白银、铂金等)，数据来源金投网
# code: 编码，如JO_92233国际黄金价格
# style: 数据类型，1为5分线数据，2为1小时线数据，3为日线数据，4为周线数据，5为月线数据
def get_gold_price_history(code, style):
    showName = ""
    for item in data:
        if item["code"] == code:
            print("正在获取'" + item["showName"] + "'的历史数据...")
            showName = item["showName"]
    # 贵金属历史数据
    result_history_data = {}
# 获取毫秒级时间戳
    timestamp_ms = int(time.time() * 1000)
    res = requests.get(data_url + "history.htm?code="+code + "&style="+style+"&pageSize=300&_=" + str(time),headers = header)
    quote_json_str = res.content.decode("utf-8")
    comma_index = quote_json_str.find('{')
    if comma_index > -1:
        quote_json_str = quote_json_str[comma_index:]
    quote_json = json.loads(quote_json_str)
    print(quote_json)
    result_history_data["编号"] = quote_json["code"]
    result_history_data["单位"] = quote_json["unit"]
    result_history_data["名字"] = showName
    result_history_data["data"] = []
    for item in quote_json["data"]:
        #print(item)
        dt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item["time"] / 1000))

        result_history_data["data"].append({
            "开盘价": item["q1"],
            "昨收价": item["q2"],
            "最高价": item["q3"],
            "最低价": item["q4"],
            "时间": dt,
        })
    
    return result_history_data


def build_parser() -> argparse.ArgumentParser:
    parser = None

    # 定义一个ArgumentParser实例:
    parser = argparse.ArgumentParser(
        prog='gold_price', # 程序名
        description=f"gold_price 贵金属查询服务查询黄金、白银、铂金最新价格 (v{__version__})", # 描述
    )
    code_des = ""
    code_ary = []
    for item in data:
        code_des += item["code"] + item["showName"] + ","
        code_ary.append(item["showName"])

    # 添加参数:
    parser.add_argument('--name', default=None,
        choices=code_ary,
        help="贵金属名称："+code_des)
    
    parser.add_argument('--style', default="1",
        choices=["1", "2", "3", "4", "5"],
        help="数据类型，1为5分线数据，2为1小时线数据，3为日线数据，4为周线数据，5为月线数据")
    

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    # 解析参数:
    args = parser.parse_args()
    name = args.name
    style = args.style
    if name is None:
        result_data = get_gold_price()
        print(json.dumps(result_data, ensure_ascii=False, indent=4))
    else:
        code = ""
        for item in data:
            if item["showName"] == name:
                code = item["code"]
        result_history_data = get_gold_price_history(code, style)
        print(json.dumps(result_history_data, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    main()
