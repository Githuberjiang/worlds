import time  # 时间戳
import json  # 返回json 处理
import requests  # 请求 url
import hashlib  # md5 加密

word = "hello"
# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
url = "http://fanyi.youdao.com"
# http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule
# 有道翻译的　API
t = str(int(time.time() * 1000))  # 当前时间戳
s = "sr_3(QOHT)L2dx#uuGR@r"  # 一段用来加密的字符串
sign_ = "fanyideskweb" + word + t + s

m = hashlib.md5()  # 根据数据串的内容进行 md5 加密
m.update((sign_).encode('utf-8'))
# print(m.hexdigest())
word_key = {  # key 这个字典为 POST 给有道词典服务器的内容
    'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': t,
    'sign': m.hexdigest(),
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': 'false'
}
response = requests.post(url, data=word_key)  # 发送请求
print(response)
print(response.text)
a = response.text

# 判断服务器是否相应成功