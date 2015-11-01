
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


access_token = "4085003534-LTCd8yW2PXK0VxatxwEh1cpsXIvQPTmFq6CC2Np"
access_token_secret = "ToJNM8zPLKV3drZFDhrURgVhWEmnrYcB2UO6FRyCjxDPI"
consumer_key = "dXIoHTohrETqdu3vebjqmYq18"
consumer_secret = "eVqxH6Mc6Bvfe0GWMIEVLqoEr3lIjYnDUn2Fc61oxfV6wGW8le"



class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

#Add keywords here
    stream.filter(track=['bridge'])			
