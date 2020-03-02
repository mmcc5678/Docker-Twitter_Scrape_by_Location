


#consumer key, consumer secret, access token, access secret.
ckey="XXX"
csecret="XXX"
atoken="XXX"
asecret="XXX"


# In[ ]:


class listener(StreamListener):

    def on_status(self, tweet):
        print (tweet.text)

    def on_data(self, data):

        try:
            #Send the tweets to the server localhost and put them in the db "Twitter"
            from pymongo import MongoClient
            client = MongoClient('192.168.3.65:32768',
                                 username='DB-USER',
                                 password='DB-PASSWORD')
            db = client.Twitter
            
            # Decode the JSON from Twitter
            datajson = json.loads(data) 
            
            # Insert it into the colleection "Canada"
            test_id = db.Canada.insert_one(datajson) 
            
            #grab the 'text' data from the Tweet to use for display
            text = datajson['text']
 
            #print out a message to the screen with the tweet's text
            print(str(text))

        except BaseException as e:
            print ('Error, on data: ',str(e))

    def on_error(self, status):
        print  ("Error Msg: %s" % str(status))
        time.sleep(5)
        return

    def on_limit(self, track):
        """Called when a limitation notice arrvies"""
        print ("!!! Limitation notice received: %s" % str(track))
        return

    def on_timeout(self):
        print('Timeout...', file=sys.stderr)
        time.sleep(10)
        return True

    def on_disconnect(self, notice):
        print ("Disconnect: %s" % str(notice))
        return


# In[ ]:


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


# In[ ]:


twitterStream = Stream(auth, listener())
# Canada's Bounding Box from: https://gist.github.com/graydon/11198540
twitterStream.filter(locations=(-140.99778, 41.6751050889, -52.6480987209, 83.23324),
                          async=True)

