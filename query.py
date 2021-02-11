import requests
from getcookie import get_cookie
import json
import time
import sys
import datetime
import pickle
import joblib


headers = {
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "content-type": "text/json",
    "origin": "https://workflow.sues.edu.cn",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://workflow.sues.edu.cn/default/work/shgcd/jkxxcj/jkxxcj.jsp",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
    "content-length": "896",
}
error_list = []


def query_record(number, headers, only_today=True):
    # number =   # 学号
    # is_today = False   # 是否只查询当天

    if only_today:
        querySqlId = "com.sudytech.work.shgcd.jkxxcj.jkxxcj.queryToday"
    else:
        querySqlId = "com.sudytech.work.shgcd.jkxxcj.jkxxcj.queryNear"

    url = "https://workflow.sues.edu.cn/default/work/shgcd/jkxxcj/jkxxcj/com.sudytech.portalone.base.db.queryBySqlWithoutPagecond.biz.ext"
    payloads = '{"params":{"empcode":"' + \
        str(number)+'"},"querySqlId":"'+querySqlId+'"}'
    print(payloads)
    r = requests.post(url, headers=headers, data=payloads)
    print(r)

    try:
        data = r.json()["list"]
        print(
            f"查询学号 {number} 成功，共计查询到 {len(data)} 份记录。 仅查询今日={only_today}")
    except Exception as e:
        if "统一身份认证平台" in r.text:
            print("JSESSIONID失效，请重新获取")
        else:
            print("遇到错误: "+str(e))
            print(r.text)
        return

    return data

try:
    headers = joblib.load('h.pkl')
    last_card = query_record(id, headers, False)[0]
except:
    cookie = get_cookie("021116118", "Chen980123")
    JSESSIONID = cookie[0]
    route = cookie[1]
    iPlanetDirectoryPro = cookie[2]
    print({"cookie": "JSESSIONID=" + JSESSIONID + "; route=" + route + "; iPlanetDirectoryPro=" + iPlanetDirectoryPro})
    headers.update(
        {"cookie": "JSESSIONID=" + JSESSIONID + "; route=" + route + "; iPlanetDirectoryPro=" + iPlanetDirectoryPro})
    print(headers)
    last_card = query_record(id, headers, False)

print(last_card)
try:
    joblib.dump(last_card[0],'last_card.pkl')
except Exception as e:
    print(e)


#lc["TJSJ"]=time.strftime("%Y-%m-%d %H:%M", time.localtime())
#lc["TW"]="36.2"
print(lc)
print(json.dumps(lc, ensure_ascii=False))