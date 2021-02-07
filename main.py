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


def job_func():
    wait = random.randrange(0, 1800)
    print(datetime.datetime.now())
    print("等待中")
    print(wait)
    time.sleep(wait)
    ##随机等待一些时间
    print(datetime.datetime.now())
    print("等待完毕")


    browser = Browser("chrome")
    browser.visit('https://workflow.sues.edu.cn/default/work/shgcd/jkxxcj/jkxxcj.jsp')
    browser.find_by_id('username').fill(username)
    browser.find_by_id('password').fill(password)
    browser.find_by_id('passbutton').click()
    print(datetime.datetime.now())
    print("登陆成功")
    time.sleep(10)
    #登陆填报界面
    tep = random.uniform(36.1, 36.7)
    tep = format(tep, '.1f')
    #随机一些温度
    browser.find_by_xpath('//*[@id="form"]/div[18]/div[1]/div/div[2]/div/div/input').fill(tep)
    #找到温度填写的框
    time.sleep(5)
    browser.find_by_id('post').click()
    #找到按钮
    print(datetime.datetime.now())
    print("登记成功")
    time.sleep(10)
    browser.quit()


def test():
    browser = Browser("chrome")
    browser.visit('https://workflow.sues.edu.cn/default/work/shgcd/jkxxcj/jkxxcj.jsp')
    browser.find_by_id('username').fill(username)
    browser.find_by_id('password').fill(password)
    browser.find_by_id('passbutton').click()
    print(datetime.datetime.now())
    print("登陆成功")
    time.sleep(10)
    tep = random.uniform(36.1, 36.7)
    tep = format(tep, '.1f')
    browser.find_by_xpath('//*[@id="form"]/div[18]/div[1]/div/div[2]/div/div/input').fill(tep)
    time.sleep(5)
    browser.quit()

def tick():
    print(datetime.datetime.now())
    print("运行中")

if __name__ == '__main__':
    timez=pytz.timezone('Asia/Shanghai')
    username = input("username:")
    password = input("password:")
    print("系统测试")
    test()
    print("测试成功，系统启动")
    scheduler = BlockingScheduler(timezone=timez)
    trigger1 = CronTrigger(day_of_week='0-6', hour=8, minute=00, second=00,timezone=timez)
    #每天8点响应一下
    trigger2 = CronTrigger(day_of_week='0-6', hour=13, minute=00, second=00,timezone=timez)
    trigger3 = IntervalTrigger(hours=1,timezone=timez)
    #每隔1个小时响应一下
    scheduler.add_job(job_func,trigger1)
    scheduler.add_job(job_func, trigger2)
    scheduler.add_job(tick, trigger3)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


