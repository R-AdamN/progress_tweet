import tweepy

def main():
    # テキストファイルからキー類読み込み
    fkeys = open('./secret/keys2.txt', 'r')
    keys = fkeys.readlines()
    consumer_key = keys[0].replace('\n','')
    consumer_secret_key = keys[1].replace('\n','')
    access_token= keys[2].replace('\n','')
    access_token_secret = keys[3].replace('\n','')

    # オブジェクト生成
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)

    

    return

if __name__ == '__main__':
    main()
