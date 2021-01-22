#! -*- coding: utf-8 -*-
"""
Create type_time: 2021-1-15
Info: 定期向企业微信推送消息
"""
import requests, json
import datetime
import time

wx_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=9d43dad9-73a8-4a42-8f40-5499387001cf"  # 测试机器人1号
send_message = "咳咳，干饭人干饭魂，小康干饭时间到了 @曾永康 "


def get_current_time():
    """获取当前时间，当前时分秒"""
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hour = datetime.datetime.now().strftime("%H")
    mm = datetime.datetime.now().strftime("%M")
    ss = datetime.datetime.now().strftime("%S")
    return now_time, hour, mm, ss


def sleep_time(hour, m, sec):
    """返回总共秒数"""
    return hour * 3600 + m * 60 + sec


def send_msg(content):
    """艾特全部，并发送指定信息"""
    data = json.dumps({"msgtype": "text", "text": {"content": content, "mentioned_list": [" "]}})
    r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))
    print(r.json)


def every_time_send_msg(interval_h=0, interval_m=1, interval_s=0, special_h="00", special_m="00", mode="special"):
    """每天指定时间发送指定消息"""
    settime = ["1152","1822","2052"]

    # 死循环
    while 1 == 1:
        # 获取当前时间和当前时分秒
        c_now, c_h, c_m, c_s = get_current_time()

        ctime = str(c_h)+str(c_m)

        if ctime in settime:
            print("正在发送...")
            print("当前时间：", c_now, c_h, c_m, c_s)
            send_msg(send_message)
        time.sleep(59)

if __name__ == '__main__':
    every_time_send_msg()