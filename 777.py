import time  # 时间戳
import json  # 返回json 处理
import requests  # 请求 url
import hashlib  # md5 加密

import xlrd
import xlutils
from xlutils import copy

books = xlrd.open_workbook('ch.xls')
new_book = copy.copy(books)
sheetr = new_book.get_sheet(0)
new_book.save("ch.xls")
c = ""


def translate(word):
    # url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
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
    # print(response)
    # 判断服务器是否相应成功
    if (response.status_code == 200):
        print(response.text)
        return response.text

    else:
        print("有道 API 调用失败")
        return None


def get_word_result(word):
    # print(word)
    word_result = json.loads(word)
    global c
    # 通过　json.loads 把返回的结果加载成 json 格式
    # print(word_result)
    print("输入的词为：" + word_result["translateResult"][0][0]['src'])
    print("翻译结果为：" + word_result["translateResult"][0][0]['tgt'])
    c = word_result["translateResult"][0][0]['tgt']


def main():
    print("欢迎使用，本程序调用有道词典 API 进行翻译\n自动检测输入语言-->中文\n中文-->英文")
    book = xlrd.open_workbook("ch.xls")
    sheet = book.sheet_by_index(0)
    for i in range(sheet.nrows):
        word = sheet.cell(i, 1).value.strip("\n")
        word_ = translate(word)
        get_word_result(word_)
        sheetr.write(i, 2, c)
    new_book.save("ch.xls")


if __name__ == '__main__':
    main()
