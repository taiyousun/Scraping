# coding: UTF-8
# インポート
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import time
import pprint
import json
import sys
from pylint.test.functional.invalid_name import aaa


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


def header_print():
    headList = ['キャラ名', 'タイプ', '性別', 'SPD', '', 'Lv4', 'Lv9', 'Lv15', 'Lv22', 'Lv30']
    with open('list.txt', 'a', newline='\n') as f:
        f.write(','.join(headList))
        f.write('\n')


def magicListGet(bsObj2):

    try:

        # 魔法技のCSSセレクタから情報取得
        # 魔法の表を取得
        magicList = []
        magic = bsObj2.select_one("#rendered-body > div.table-type-2 > div > div:nth-child(5) > table > tbody")
        magicList.append(magic.select_one('tr:nth-child(2) > td:nth-child(2)').string)  # Lv4
        magicList.append(magic.select_one('tr:nth-child(4) > td:nth-child(2)').string)  # Lv9
        magicList.append(magic.select_one('tr:nth-child(6) > td:nth-child(2)').string)  # Lv15
        magicList.append(magic.select_one('tr:nth-child(8) > td:nth-child(2)').string)  # Lv22
        magicList.append(magic.select_one('tr:nth-child(10) > td:nth-child(2)').string)  # Lv30

    except Exception as e:
        print('魔法:',e)
        pass

    return(magicList)


def uniqueListGet(bsObj2):

    uniqueList = []

    unique = bsObj2.select_one('#rendered-body > div.table-type-2 > div > div:nth-child(2) > table > tbody')
    try:
        # 技１つ目
        found1 = unique.select_one('tr:nth-child(2)')
        # 技があるなら取得する。
        if found1 is not None:
            uniqueList.append(unique.select_one('tr:nth-child(2) > td:nth-child(2)').string)  # 技名
            uniqueList.append(unique.select_one('tr:nth-child(2) > td:nth-child(4)').string)  # SP
            uniqueList.append(unique.select_one('tr:nth-child(2) > td:nth-child(5)').string)  # 火力
            uniqueList.append(unique.select_one('tr:nth-child(2) > td:nth-child(6)').string)  # 範囲
            uniqueList.append(unique.select_one('tr:nth-child(2) > td:nth-child(7)').string)  # 依存
            uniqueList.append(unique.select_one('tr:nth-child(2) > td:nth-child(8)').string)  # 効果
        else:
            for i in range(6):
                uniqueList.append(' ')

    except Exception as e:
        print('技1:',e)
        pass

    try:
        # 技２つ目
        found2 = unique.select_one('tr:nth-child(4)')
        # 技があるなら取得する。
        if found2 is not None:
            uniqueList.append(unique.select_one('tr:nth-child(4) > td:nth-child(2)').string)  # 技名
            uniqueList.append(unique.select_one('tr:nth-child(4) > td:nth-child(4)').string)  # SP
            uniqueList.append(unique.select_one('tr:nth-child(4) > td:nth-child(5)').string)  # 火力
            uniqueList.append(unique.select_one('tr:nth-child(4) > td:nth-child(6)').string)  # 範囲
            uniqueList.append(unique.select_one('tr:nth-child(4) > td:nth-child(7)').string)  # 依存
            uniqueList.append(unique.select_one('tr:nth-child(4) > td:nth-child(8)').string)  # 効果
        else:
            for i in range(6):
                uniqueList.append(' ')

    except Exception as e:
        print('技2:',e)
        pass

    try:
        # 技３つ目
        found3 = unique.select_one('tr:nth-child(6)')
        # 技があるなら取得する。
        if found3 is not None:
            uniqueList.append(unique.select_one('tr:nth-child(6) > td:nth-child(2)').string)  # 技名
            uniqueList.append(unique.select_one('tr:nth-child(6) > td:nth-child(4)').string)  # SP
            uniqueList.append(unique.select_one('tr:nth-child(6) > td:nth-child(5)').string)  # 火力
            uniqueList.append(unique.select_one('tr:nth-child(6) > td:nth-child(6)').string)  # 範囲
            uniqueList.append(unique.select_one('tr:nth-child(6) > td:nth-child(7)').string)  # 依存
            uniqueList.append(unique.select_one('tr:nth-child(6) > td:nth-child(8)').string)  # 効果
        else:
            for i in range(6):
                uniqueList.append(' ')

    except Exception as e:
        print('技3:',e)
        pass

    try:
        # 技４つ目

        found4 = unique.select_one('tr:nth-child(8)')
        # 技があるなら取得する。
        if found4 is not None:
            uniqueList.append(unique.select_one('tr:nth-child(8) > td:nth-child(2)').string)  # 技名
            uniqueList.append(unique.select_one('tr:nth-child(8) > td:nth-child(4)').string)  # SP
            uniqueList.append(unique.select_one('tr:nth-child(8) > td:nth-child(5)').string)  # 火力
            uniqueList.append(unique.select_one('tr:nth-child(8) > td:nth-child(6)').string)  # 範囲
            uniqueList.append(unique.select_one('tr:nth-child(8) > td:nth-child(7)').string)  # 依存
            uniqueList.append(unique.select_one('tr:nth-child(8) > td:nth-child(8)').string)  # 効果
        else:
            for i in range(6):
                uniqueList.append(' ')
    except Exception as e:
        print('技4:',e)
        pass

    return(uniqueList)


def statusListGet(bsObj2):

    charaList = []

    try:
        #chara = bsObj2.select_one('#rendered-body > div:nth-child(3) > div:nth-child(2) > table > tbody')

        charaList.append(bsObj2.select_one('#page-main-title').string)  # キャラ名

        #charaList.append(chara.select_one('tr:nth-child(1) > td:nth-child(2)').string)  # 種族
        #charaList.append(chara.select_one('tr:nth-child(1) > td:nth-child(4)').string)  # 性別

    except Exception as e:
        try:
            chara = bsObj2.select_one('#rendered-body > div.tableWidthAuto\29 \23 style\28 class\3d tableWidthAuto > div:nth-child(2) > table > tbody')
            charaList.append(chara.select_one('tr:nth-child(1) > td:nth-child(2)').string)  # 種族
            charaList.append(chara.select_one('tr:nth-child(1) > td:nth-child(4)').string)  # 性別
            return(charaList)

        except Exception as e1:
            pass

        print('キャラ情報:',e)
        pass
    return(charaList)

    try:
        # パラメータ情報
        parm = bsObj2.select_one('#rendered-body > div:nth-child(3) > div:nth-child(6) > table > tbody')

        # Lv1時
        charaList.append(parm.select_one('tr:nth-child(2) > td:nth-child(2)').string)  # HP
        charaList.append(parm.select_one('tr:nth-child(3) > td:nth-child(2)').string)  # ATK
        charaList.append(parm.select_one('tr:nth-child(4) > td:nth-child(2)').string)  # DEF
        charaList.append(parm.select_one('tr:nth-child(5) > td:nth-child(2)').string)  # INT
        charaList.append(parm.select_one('tr:nth-child(6) > td:nth-child(2)').string)  # RES
        charaList.append(parm.select_one('tr:nth-child(7) > td:nth-child(2)').string)  # SPD

        # Lv9999時
        charaList.append(parm.select_one('tr:nth-child(2) > td:nth-child(2)').string)  # HP
        charaList.append(parm.select_one('tr:nth-child(3) > td:nth-child(2)').string)  # ATK
        charaList.append(parm.select_one('tr:nth-child(4) > td:nth-child(2)').string)  # DEF
        charaList.append(parm.select_one('tr:nth-child(5) > td:nth-child(2)').string)  # INT
        charaList.append(parm.select_one('tr:nth-child(6) > td:nth-child(2)').string)  # RES
        charaList.append(parm.select_one('tr:nth-child(7) > td:nth-child(2)').string)  # SPD
    except Exception as e:

        print('パラメータ:',e)
        pass
    return(charaList)


def magic_print(bsObj2, charaName):

    # 魔法技のCSSセレクタから情報取得
    magic = bsObj2.select_one("#rendered-body > div.table-type-2 > div > div:nth-child(5) > table > tbody")
    magicHead = bsObj2.select_one("#rendered-body > div.table-type-2 > div > div:nth-child(5) > table > tbody > tr:nth-child(1)")

    # ファイルをオープン
    with open('list.txt', 'a') as f:
        # 魔法技のヘッダーを作成
        str_ = 'キャラ名'
        mghdList = []
        for mghd in magicHead:
            str_ = str_ + ',' + mghd.get_text()
        f.write(str_)

        # 改行
        f.write('\n')

        cnt = 0

        # 魔法技を一つずつ区切る
        for mm in magic:
            cnt += 1

            # 奇数なら値を取得する。
            if cnt % 2 == 0:

                # リストを空に
                charadit = []

                # リストの先頭にキャラ名を格納
                charadit.append(charaName)

                # 技情報を詳細に区切る
                for m in mm:

                    # 技詳細情報をリストに取得
                    charadit.append(m.get_text())

                # 取得したファイルを書き込み
                f.write(','.join(charadit))

            else:
                pass


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

    # 新規ファイル作成
    with open('list.txt', 'w'):pass

    # ヘッダー作成
    header_print()

    # キャラのhref情報を基にリンクが終わるまでキャラ情報を取得する。

    outList = []
    cnt = 1
    for link in links:
        # データ取得の待機時間
        time.sleep(2)
        print('--------------------------------------------------')
        # リンクを繋げて正しいリンクにする。
        charaLink = wikiTop + link

        # 情報を取得する。
        html2 = requests.get(charaLink, proxies=proxies)
        bsObj2 = BeautifulSoup(html2.text, "html.parser")

        print(bsObj2.select_one('#page-main-title').get_text())

        # パラメータ取得
        print('パラメータ取得開始')
        outList.extend(statusListGet(bsObj2))

        # 固有技取得
        print('固定技取得開始')
        outList.extend(uniqueListGet(bsObj2))

        # 魔法技取得
        print('魔法技取得開始')
        outList.extend(magicListGet(bsObj2))

        # 出力ファイルを開いて行追加
        with open('list.txt', 'a', newline='\n') as f:
            f.write(','.join(outList))
            f.write('\n')

        outList = []
        cnt = cnt + 1
    print('--------------------------------------------------')

# プロキシの設定
proxies = {
"http":"http://U645051:sousuke0125@127.0.0.1:8080",
"https":"http://U645051:sousuke0125@127.0.0.1:8080"
}

# urlを取得
wikiTop = "https://wiki.dengekionline.com"

# hrefのリストメソッド実行
# href_list()
disgia_print()

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
