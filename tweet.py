import tweepy

auth = tweepy.OAuthHandler("")
auth.set_access_token("")

api = tweepy.API(auth)

user = api.get_user("_Kurokodairu_")
print("@_Kurokodairu_ has " + str(user.followers_count) + " Followers.")

search = api.search("Capitalized File Names... :/ ")

print(search[0].user.name)
print(search[0].text)


