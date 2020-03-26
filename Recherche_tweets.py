# -*- coding: utf-8
"""
Created on Thu Feb  6 08:22:49 2020

@author: nepaulr
"""
import sys
"""
Importation de la librairie json
"""
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy


"""
Différentes clés et tokens pour pouvoir utiliser l'API de tweeter pour les developpeurs.
"""
CONSUMER_KEY = 'khAkiuKeT91VP1GJ1MIDwGAXg'
CONSUMER_SECRET = 'YDEDY3z8vvy2Bza3G8gcQVGL2rSDcV735pjq7OTV6IkDt4yPnh'
ACCESS_TOKEN = '443679852-HNV6IH0svDYXK6wXPbtl43uahTNLX4485UezqhFE'
ACCESS_SECRET = 'eWcdOah5I6AlUdGVg77vVCtmTk41H4vazjoPtCHnKiqty'

"""
Connexion à l'API
"""
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


"""
Création de la classe StreamListner pour "ecouter" les tweets et les récupérer
"""
class StreamListener(tweepy.StreamListener):
    num_tweets = 0
    
    """
        Ecriture des tweets sur dans le fichier json
        Paramètre: statut de l'API
        Sortie: fichier json
    """
    def on_status(self, status):
        print(str(self.num_tweets)+" : "+str(status._json))
        self.num_tweets = self.num_tweets+1
        with open('tweet.txt','a') as tf:
            tf.write(str(json.dumps(status._json).encode('utf8')))
        if self.num_tweets == 1:
            sys.exit(0)
        return True
        
    
    def on_error(self, status_code):
        if status_code == 420:
            return False


"""
Lancement de la recherche des Tweets
"""
stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["instagram"] ,languages=["fr"])




