import tweepy
from pathlib import Path
import os
import datetime
import time

def main():

    while(True):
        # 日付が変わったか
        if(day_change()):
            # API作成
            api = make_api()
            # 進捗取得
            progress = get_progress()
            if(progress != None):
                progress_txt = "本日の進捗は"+str(progress)+"文字です!"
                api.update_status(progress_txt)
                print(progress_txt)
        # 1時間に一回実行
        time.sleep(3600)


# 日付が変わったか確認
def day_change():
    # 現在時刻取得
    dt_now = datetime.datetime.now()
    # 日付を文字列で抜き出し
    str_today = dt_now.strftime('%Y-%m-%d')

    fday_path = './secret/day.txt'

    # 日付変更フラグ
    day_is_change = 0

    if(os.path.exists(fday_path)):
        fday = open(fday_path, 'r')
        # 機能の日付を取得
        yesterday_date = fday.read().replace('\n','')
        yesterday_datetime = datetime.datetime.strptime(yesterday_date, '%Y-%m-%d')
        fday.close()
        # 機能の日付+1日の0時以降か
        if(dt_now>=yesterday_datetime+datetime.timedelta(days=1)):
            day_is_change = 1

    # 今日の日付を書き込み
    fday = open(fday_path, 'w')
    fday.write(str_today)
    fday.close()
    return day_is_change


def make_api():
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

    return api


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
