from splinter import Browser
import apscheduler
import os
import random
import time
import datetime
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler

from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
import pandas as pd

def job_func(username,password):
    browser = Browser("chrome")
    browser.visit('https://web-vpn.sues.edu.cn/')
    browser.find_by_id('username').fill(username)
    browser.find_by_id('password').fill(password)
    browser.find_by_id('passbutton').click()
    print(datetime.datetime.now())
    print("登陆成功")
    time.sleep(10)
    # 登陆填报界面
    browser.find_by_text('健康信息填报').click()
    time.sleep(10)
    browser.windows.current = browser.windows[1]
    time.sleep(10)
    tep = random.uniform(36.1, 36.7)
    tep = format(tep, '.1f')
    # 随机一些温度
    browser.find_by_xpath('//*[@id="form"]/div[18]/div[1]/div/div[2]/div/div/input').fill(tep)
    # 找到温度填写的框
    time.sleep(5)
    browser.find_by_id('post').click()
    # 找到按钮
    time.sleep(5)
    result = browser.find_by_xpath("//*[@id=\"layui-layer1\"]/div[2]").text
    browser.quit()
    return result




def tick():
    print(datetime.datetime.now())
    print("运行中")


def job():
    data = pd.read_excel('account.xlsx', dtype={'username': str})
    username = data["username"]
    password = data["password"]
    for x in range(len(username)):
        wait = random.randrange(0, 100)
        print(datetime.datetime.now())
        print("等待中")
        print(wait)
        time.sleep(wait)
        ##随机等待一些时间
        print(datetime.datetime.now())
        print("等待完毕")
        print("为" + username[x] + "登记中")
        trytime = 0
        while (True):
            trytime = trytime + 1
            flag = False
            result = ""
            try:
                result = job_func(username[x], password[x])
            except:
                print("出现异常错误")
            if (result == "健康填报成功"):
                flag = True

            if (flag == True):
                print(datetime.datetime.now())
                print(username[x] + "登记成功")
                break
            else:
                print(username[x] + "登记失败")
                print("尝试次数：" + str(trytime))
                time.sleep(10)

            if (trytime >= 5):
                print(username[x] + "登记失败,更换账户")
                break

def TEST():
    data = pd.read_excel('account.xlsx',dtype = { 'username' : str })
    username = data["username"]
    password = data["password"]
    for x in range(len(username)):
        wait = random.randrange(0, 100)
        print(datetime.datetime.now())
        print("等待中")
        print(wait)
        time.sleep(wait)
        ##随机等待一些时间
        print(datetime.datetime.now())
        print("等待完毕")
        print("为"+username[x]+"登记中")
        trytime=0
        while(True):
            trytime=trytime+1
            flag=False
            result=""
            try:
                result=job_func(username[x],password[x])
            except:
                print("出现异常错误")
            if (result == "健康填报成功"):
                flag=True

            if (flag == True):
                print(datetime.datetime.now())
                print(username[x] + "登记成功")
                break
            else:
                print(username[x]+ "登记失败")
                print("尝试次数：" + str(trytime))
                time.sleep(10)

            if (trytime >= 5):
                print(username[x]+ "登记失败,更换账户")
                break




if __name__ == '__main__':
    TEST()
    timez=pytz.timezone('Asia/Shanghai')
    print("系统测试")
    print("测试成功，系统启动")
    scheduler = BlockingScheduler(timezone=timez)
    trigger1 = CronTrigger(day_of_week='0-6', hour=8, minute=00, second=00,timezone=timez)
    #每天8点响应一下
    trigger2 = CronTrigger(day_of_week='0-6', hour=13, minute=00, second=00,timezone=timez)
    trigger3 = IntervalTrigger(hours=1,timezone=timez)
    #每隔1个小时响应一下
    scheduler.add_job(job,trigger1)
    scheduler.add_job(job, trigger2)
    scheduler.add_job(tick, trigger3)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


