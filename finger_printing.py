import json
import random

USER_AGENT_LIST = [
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Vivaldi/6.1.3035.100",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Vivaldi/6.1.3035.100",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:114.0) Gecko/20100101 Firefox/114.0",
  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0"
]

HTTP_REFERERS = [
    "https://www.baidu.com/",
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.sogou.com/",
    "https://www.so.com/",
    "https://m.sm.cn/",
    "https://yandex.com/",
    "https://www.toutiao.com/",
    "https://www.zhihu.com",
    "https://www.taobao.com"
]

def get_random_user_agent() -> (str):
    index = random.randrange(0, len(USER_AGENT_LIST) - 1)
    return USER_AGENT_LIST[index]

def get_random_referer() -> (str):
    index = random.randrange(0, len(HTTP_REFERERS) - 1)
    return HTTP_REFERERS[index]
