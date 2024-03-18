import sys
import os
			
class Pluginvideosmate_organizer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "</div> <!-- /content-in -->" },
			{ "text" : "<!-- script Downloaded from http://videosmate.com -->" },
			{ "string" : /<!--Copyright (20[\d]{2}),Videosmate Organizer[\s]+Downloaded from http:\/\/videosmate\.com/" },
			{ "version" : "/<!-- LICENSED Version  Videosmate ORGANIZER", "Ver\.([^\s]+) -->/" },
			{ "version" : "/<a href=http:\/\/videosmate\.com><font color=#ffffff>Powered&nbsp;by&nbsp;Videosmate&nbsp;Organizer&nbsp;Version&nbsp;([^\s^&]+)&nbsp;Copyright&nbsp;&copy;&nbsp;(20[\d]{2})<\/a>/" },
			{ "string" : /<a href=http:\/\/videosmate\.com><font color=#ffffff>Powered&nbsp;by&nbsp;Videosmate&nbsp;Organizer&nbsp;Version&nbsp;([^\s^&]+)&nbsp;Copyright&nbsp;&copy;&nbsp;(20[\d]{2})<\/a>/", "offset" : "1 },
		]

