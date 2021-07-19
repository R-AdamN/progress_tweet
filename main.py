import tweepy
from pathlib import Path

def main():
    # テキストファイルからキー類読み込み
    fkeys = open('./secret/keys2.txt', 'r')
    keys = fkeys.readlines()
    consumer_key = keys[0].replace('\n','')
    consumer_secret_key = keys[1].replace('\n','')
    access_token= keys[2].replace('\n','')
    access_token_secret = keys[3].replace('\n','')
    fkeys.close()

    # オブジェクト生成
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)


    # パス読み込み
    fpath = open('./secret/path.txt', 'r')
    path = fpath.read().replace('\n','')
    fpath.close()

    # ファイル開き
    p = Path(path)
    files = p.glob("*.txt")

    # 文字数カウント
    sum_word_count = 0
    for file in files:
        with file.open() as f:
            sum_word_count += len(f.read())

    return

if __name__ == '__main__':
    main()
