import tweepy

def main():
    fkeys = open('./secret/keys2.txt', 'r')
    keys = fkeys.readlines()
    consumer_key = keys[0]
    consumer_secret = keys[1]
    access_token= keys[2]
    access_token_secret = keys[3]
    return

if __name__ == '__main__':
    main()
