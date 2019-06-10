import tweepy

auth = tweepy.OAuthHandler("QI8vmScHdMpvQSey7KlGjnmyd", "D3xUJ1EONJIZv0Yqun8kYETASQVWCIHvVJpsbTElc941yR5C0A")
auth.set_access_token("1004970613289734144-f3l5vdXPSDIHIo3PWUtJ2BM1Modb86", "KBetHUImvnOXO012rnNgtcwbpyEhDxv2sJT528DB5HSam")

api = tweepy.API(auth)

#user = api.get_user("_Kurokodairu_")
#print("@_Kurokodairu_ has " + str(user.followers_count) + " Followers.")

search = api.search("Capitalized File Names... :/ ")

print(search[0].text)
print(search[0].user.name)
