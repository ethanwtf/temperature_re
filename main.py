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
    tep = random.uniform(36.1, 36.7)
    tep = format(tep, '.1f')
    browser.find_by_xpath('//*[@id="form"]/div[18]/div[1]/div/div[2]/div/div/input').fill(tep)
    time.sleep(5)
    browser.find_by_id('post').click()
    print(datetime.datetime.now())
    print("登记成功")
    time.sleep(10)
    browser.quit()
# Press the green button in the gutter to run the script.

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
    trigger2 = CronTrigger(day_of_week='0-6', hour=13, minute=00, second=00,timezone=timez)
    trigger3 = IntervalTrigger(hours=1,timezone=timez)
    scheduler.add_job(job_func,trigger1)
    scheduler.add_job(job_func, trigger2)
    scheduler.add_job(tick, trigger3)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        os.system("pause")

