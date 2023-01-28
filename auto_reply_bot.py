import time
import tweepy 
import random

api_key="much"
api_secret="credentials"
bearer_token="such"
access_token="wow"
access_token_secret="xd"
repertorio = ["Então, tá certo isso aí não. Eu concordo com a Amanda.", "Nem li mas a Amanda tá certa.", "Tem um equívoco no que você disse.", "Não tá certo isso o que você disse.", "It's wrong, actually.", "Então, não tá certo isso que você disse."]

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
bot = client.get_user(username="", user_auth=True).data.id

start_id=1
init_mentions = client.get_users_mentions(bot, user_auth=True).data
if init_mentions != None:
    start_id = init_mentions[0].id

while True:
    mentions = client.get_users_mentions(bot, since_id=start_id, user_auth=True).data

    if mentions != None:
        for mention in mentions:
            try:
                client.create_tweet(in_reply_to_tweet_id=mention.id, text=repertorio[random.randint(0, len(repertorio)-1)])
                print("Just tweeted!")
                start_id = mention.id
            except Exception as error:
                print(error)

    time.sleep(5)