#!/usr/bin/env Python
import sys
import ast
import urllib2

response = urllib2.urlopen('https://lancer.streamup.com/api/channels/gakinotsukai/playlists')
playlist = ast.literal_eval(response.read())

print playlist

play = {"hls":"http"};

print playlist['hls']
