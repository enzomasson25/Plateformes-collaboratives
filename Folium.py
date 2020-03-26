# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:13:49 2020

@author: nepaulr
"""
import folium
import webbrowser
import json

"""
    Création de la fonction map qui s'occupe de récuperer les tweets depuis le fichier json
    Sortie: Ouverture d'une page web avec les différents tweets postés.
"""
def map():
    with open('tweet.json') as tweetBank:
        data = json.load(tweetBank)
        tweets  = data.get("foo")
        m = folium.Map(zoom_start=15, tiles = 'OpenStreetMap')
    for tweet in tweets:
        text = tweet["text"]
        id_user = str(tweet["user"]["id"])
        lon = tweet["coordinates"]["coordinates"][0]
        lat = tweet["coordinates"]["coordinates"][1]
        print(str(id_user) + " " +text + " " + str(lon) + " " + str(lat) + "\n")
        Coordinates=[lat, lon]
        tooltip = 'Click me!'
        folium.Marker(Coordinates, popup='<i>' + id_user + '\n' + text + '</i>', tooltip=tooltip, icon=folium.Icon(icon='info-sign',color='blue')).add_to(m)
        folium.Circle(radius=100, location=Coordinates, popup='The Waterfront', color='green',fill=True, fill_color='red').add_to(m)    
        m.save('index.html')
        webbrowser.open('index.html')
    

map()