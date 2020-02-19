# coding: UTF-8
# インポート
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import time
import pprint
import json


def href_list():
    # HTMLを取得
    html = requests.get(base_url + url, proxies=proxies)
    # HTMLパース用のオブジェクトを作成します。
    soup = BeautifulSoup(html.text, "html.parser")

    # 次ページのulrのHTMLタグ
    next_page = soup.find_all('a', class_='next')

    # hrefに/patch/patch-とつくaタグを取得する
    srh = soup.find_all('a', href=re.compile("/patch/patch-"))

    print(next_page[0].get('href'))

    # if bool(next_page) == False:
        # break
    # hrefの情報だけをリストにまとめる
    ul = []
    for a in srh:
        ul.append(base_url + a.attrs['href'])
    # ul(リスト)の中にある重複を削除して新たにurllist(リスト)を作成
    urllist = list(set(ul))

    # urllistを出力(確認用)
    for i in urllist:
        print(i)

def magic_print():
    outlink = []
    for link in links:


def disgia_print():

    # キャラ一覧のHTMLを取得
    wikiCharaList = "/disgaea-app/%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC%E4%B8%80%E8%A6%A7"
    html = requests.get(wikiTop + wikiCharaList, proxies=proxies)

    # HTMLパース用のオブジェクトを作成します。
    bsObj = BeautifulSoup(html.text, "html.parser")

    # キャラ一覧のテーブル情報を取得
    elems = bsObj.select('#list h4 a')
    table = bsObj.findAll("div", {"class":"sortable"})[0]
    # テーブル情報内のhrefに下記リンクと一致する文字列があるものを取得
    srh = table.findAll('a', href=re.compile("/disgaea-app/"))

    # リンクの情報のみ取得し、リンクの重複を削除する。
    dupliLink = []
    for sh in srh:
        dupliLink.append(sh.get('href'))
    links = sorted(set(dupliLink), key=dupliLink.index)

    # 出力ファイルをオープン
    f = open('list.txt','w')

    # キャラのhref情報を基にリンクが終わるまでキャラ情報を取得する。
    outlink = []
    for link in links:
        # データ取得の待機時間
        time.sleep(2)

        # リンクを繋げて正しいリンクにする。
        charaLink = wikiTop + link
        html2 = requests.get(charaLink, proxies=proxies)
        bsObj2 = BeautifulSoup(html2.text, "html.parser")
        # キャラ名を取得
        title1 = bsObj2.find("h1").string
        # outlink.append(title1)

        # キャラ名出力
        print("title = ", title1)

        # キャラ固有技を取得
        unique = bsObj2.select_one("#rendered-body > div.table-type-2 > div > div:nth-child(2) > table")
        uniqueHead = bsObj2.select_one("#rendered-body > div.table-type-2 > div > div:nth-child(2) > table > tbody > tr:nth-child(1)")

        # 魔法技のCSSセレクタから情報取得
        magic = bsObj2.select_one("#rendered-body > div.table-type-2 > div > div:nth-child(5) > table > tbody")
        magicHead = bsObj2.select_one("#rendered-body > div.table-type-2 > div > div:nth-child(5) > table > tbody > tr:nth-child(1)")

        # 魔法技のヘッダーを作成
        mgHeadList = []
        mgHeadList.append("キャラ名")
        for mghd in magicHead:
            mgHeadList.append(mghd.get_text())

        f.write('aa')
        f.close
        # 魔法技の情報を取得
        mglist = []
        # 魔法技を一つずつ区切る
        for mm in magic:
            mlist = []
            mlist.append(title1)
            # 魔法の詳細情報を一つずつ区切る
            for aa in mm:
                # 詳細情報をリストに追加
                mlist.append(aa.get_text())

            dictaa = dict(zip(mgHeadList, mlist))

            mglist.append(dictaa)

        outlink.append(mglist)

    pprint.pprint(outlink)


#         # 魔法技一つ目を取得
#         aaa = magic.select_one("tbody > tr:nth-child(1)")
#         for aa in aaa:
#             pprint.pprint(aa.get_text())

#     for row in rows:
#         aa = row.get('href')
#         csvRow = []
#         for cell in row.findAll(['td', 'th']):
#             csvRow.append(cell.get_text())
#         print(csvRow)


# プロキシの設定
proxies = {
"http":"http://U645051:sousuke0125@127.0.0.1:8080",
"https":"http://U645051:sousuke0125@127.0.0.1:8080"
}

# urlを取得
wikiTop = "https://wiki.dengekionline.com"


# hrefのリストメソッド実行
# href_list()
#disgia_print()

'''
#④「span」要素全て抽出します。
span = soup.find_all("span")

#⑤「span」要素をループします。
for tag in span:
    try:
        #⑥「span」要素から「class」をpopしていきます。
        string_ = tag.get("class").pop(0)
        #⑦摘出したclassの文字列にm-miH01C_rateが設定されているかチェックします。
        if string_ in "m-miH01C_rate":
            #⑧tagの文字列(日経平均株価)を取得します。
            nikkei_heikin = tag.string
            #⑨ループ処理を中断します。
            break
    except:
        #⑥'「span」要素から「class」をpopできなかった場合何もしません。
        pass

#⓾取得した日経平均株価を出力します。
print(nikkei_heikin)
'''
