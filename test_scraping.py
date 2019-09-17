# coding: UTF-8
# インポート
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def href_list():
    # HTMLを取得
    html = requests.get(base_url + url, proxies=proxies)
    # HTMLパース用のオブジェクトを作成します。
    soup = BeautifulSoup(html.text,"html.parser")

    # 次ページのulrのHTMLタグ
    next_page = soup.find_all('a', class_='next')


    # hrefに/patch/patch-とつくaタグを取得する
    srh = soup.find_all('a', href=re.compile("/patch/patch-"))


    print(next_page[0].get('href'))
    if bool(next_page) == False:
        break
    # hrefの情報だけをリストにまとめる
    ul = []
    for a in srh:
        ul.append(base_url + a.attrs['href'])
    # ul(リスト)の中にある重複を削除して新たにurllist(リスト)を作成
    urllist = list(set(ul))

    # urllistを出力(確認用)
    for i in urllist:
        print(i)



# プロキシの設定
proxies = {
"http":"http://U645051:tomoyori0817@127.0.0.1:8080",
"https":"http://U645051:tomoyori0817@127.0.0.1:8080"
}

# urlを取得
base_url = 'https://jp.leagueoflegends.com'
url = '/ja/news/game-updates/patch/'


# hrefのリストメソッド実行
href_list()



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
