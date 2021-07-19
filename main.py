import tweepy
from pathlib import Path
import os

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

    progress = get_progress()
    if(progress != None):
        print(progress)



def get_progress():
    # パス読み込み
    fpath = open('./secret/path.txt', 'r')
    path = fpath.read().replace('\n','')
    fpath.close()

    # パス開き
    p = Path(path)
    files = p.glob("*.txt")

    # 文字数カウント
    sum_word_count = 0
    for file in files:
        with file.open() as f:
            sum_word_count += len(f.read())

    ## 昨日までの進捗取得
    # パス読み込み
    yesterday_progress_path = './secret/yesterday_progress.txt'
    progress = None
    if(os.path.exists(yesterday_progress_path)):
        fyesterday_progress = open(yesterday_progress_path, 'r')
        yesterday_progress = int(fyesterday_progress.read().replace('\n',''))
        fyesterday_progress.close()
        progress = yesterday_progress - sum_word_count


    # 今日の進捗記録
    ftoday_progress_path = open(yesterday_progress_path, 'w')
    ftoday_progress_path.write(str(sum_word_count))
    ftoday_progress_path.close()
    return progress

if __name__ == '__main__':
    main()
