"""
    RFC を英語の勉強がてら読むので補助プログラムを書く。
        1. ランダムに RFC をダウンロードする
        2. 用語を抜き出してタグ付けを自動化
"""
import random
import sys
from typing import Any, List, Tuple

import requests
from bs4 import BeautifulSoup


def random_RFC() -> Tuple[Any, str]:
    """
    RFC をダウンロードする
    """
    no = random.randint(1, 9000)
    uri = "https://www.rfc-editor.org/rfc/rfc" + str(no) + ".html"
    res = requests.get(uri)
    return (res, uri)


def entag(content: str, glossary: list) -> List[str]:
    """
    リストに基づきタグを返す
    args:
        content: html
        glossary: 単語集
    return:
        tag: glossary の中で content に含まれる単語のリスト
    """
    pass
    # return tag


if __name__ == "__main__":
    """
    最初に "Abstract" と記載してある行から 15 行抜き出す。

    Why:
        アブストラクトが <pre>～</pre> で記載されている場合があり、直接に取得できないため

    Problem:
        - プログラムが想定通りに動かない。
            - buffer 数より残り行数が少ないとき
            - Abstract より先 "Abstract" という単語がでたとき
    """
    buffer: int = 15
    res, uri = random_RFC()
    html = BeautifulSoup(res.text, features="html.parser")
    print(uri)
    abstract_locations: list = [
        e for e, i in enumerate(html.text.split("\n")) if "Abstract" in i
    ]
    assert len(abstract_locations) > 0, "abstract_locations <= 0 です"
    if len(html.text.split("\n")) < abstract_locations[0] + buffer:
        sys.exit()

    maybe_abstract: list = html.text.split("\n")[
        abstract_locations[0] : abstract_locations[0] + buffer
    ]

    for i in maybe_abstract:
        print(i)

        if len(i) == 0:
            print("\n", end="")
