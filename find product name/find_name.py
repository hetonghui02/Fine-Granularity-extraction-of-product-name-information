import requests
import re
import pandas as pd
import os

goods = '包'
filename = f"{goods}.xlsx"
if not os.path.isfile(filename):
    df = pd.DataFrame(columns=["item_name"])
    df.to_excel(filename,index=False)

df = pd.read_excel(filename)

def getHTMLText(url):
    kv={
        'cookie':'isg=BAkJZAEIiRtfbXXuj7Qkjb9SGjNjVv2IdCLK9Kt9hfAv8isE8qbIWMgwNtbEsZXA; l=fBPIKA0nN-K9QQyzBOfanurza77OSIdYYuPzaNbMi9fP_j5B54X5W1smjA86C31VF6rJR3rEaXhMBeYBcQAonxv9w8VMULkmndLHR35..; tfstk=dhQpf0cDy5hpgQYIapEgzM0g74_LoaCeX95jrLvnVOBOKd0uTeqyyTpOUpxHR645IsWJK7re-GhRgOBJ4WJkFLBlNMALorfFTU85e-40oTOyzUaCG161T68yP-20orfew8aIBtvHvr1yCwI4PSvOs69tyX79dHnFOd3SPN3DvO5cntHEcxvvZDFOP0oyACJGSiVG.; uc1=cookie14=Uoe8gqQIPme4Lg%3D%3D; _m_h5_tk=1d471b004cd10b84148545d2fbca0cc5_1688443690904; _m_h5_tk_enc=a8e4f9103cc1856cdb2049cd1628bb77; _tb_token_=3f8eb586e3879; cookie2=199d5c8d287cb677d14448ab2dc490f7; mt=ci=-1_0; thw=cn; _cc_=WqG3DMC9EA%3D%3D; lgc=tb50458303; sgcookie=E100gCQmiHEXxoYvJ4FFo8ZNdEuwZQeY6MOkZaGXu1rS0SnLUCtcgQcBDKbEdgX5gNLKOUgEIsMdIPUv4DyRpG6RZl5db8JXHsVcgXaWo5QxZDpqE2QCAxuAeO8gafF%2FPwc4w8IssfrcNyLCXPNX7iQt5A%3D%3D; t=d907ef6f6873f6d6a81fbf0c797d8405; tracknick=tb50458303; uc3=nk2=F5RAQpSS0B75aw%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&vt3=F8dCsGO7WCtPYeViLCQ%3D&id2=UNQ3GkDHKtIUgQ%3D%3D; uc4=id4=0%40UgP8J%2BkB%2Buzt86SYTGwtR5YO3dVV&nk4=0%40FY4L7mirMVth8kz%2F531trqF3uF6o; xlly_s=1; cna=moIpHTz+UiICAXLwN6S6F4ug',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Safari/605.1.15'
       }
    try:
        r = requests.get(url, headers=kv,timeout=300)
        # r=requests.get(url,timeout=300)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        pri = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html) #价格
        plt = re.findall(r'\"view_sales\"\:\".*?\"', html)#销量
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)#名称

        for i in range(len(plt)):
            pricc=eval(pri[i].split(':')[1])  #价格
            price = eval(plt[i].split(':')[1])#销量
            title = eval(tlt[i].split(':')[1])#名称
            # numi=eval(num[i].split(':')[1])
            ilt.append([pricc,price, title])
    except:
        print("")


def printGoodsList(ilt):
    item_name = []
    tplt = "{:4}\t{:6}\t{:8}\t{:10}"
    #print(tplt.format("序号","价格", "销量","商品名称"))
    count = 0
    for g in ilt:
        item_name.append(g[2])
        #print(tplt.format(count, g[0], g[1],g[2]))
    df["item_name"] = item_name
    df.to_excel(filename,index=False)

def main():
    depth = 10
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            # print(html)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
    print("已将爬取商品名保存到对应excel文件中")


main()
