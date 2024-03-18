import sys
import os
			
class site_meter_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "account" : '/<script [^>]*src=["']http:\/\/[^>]+sitemeter\.com\/js\/counter\.js\?site=([^"^'^>]+)[^>]*>/i }
			{ "account" : '/<img [^>]*src=["']http:\/\/[^>]+sitemeter\.com\/meter\.asp\?site=([^"^'^>]+)[^>]*>/i }
			{ "certainty" : '25", "text" : '<!-- Site Meter -->" }
			{ "regexp" : '/<!-- Copyright \(c\)20[\d]{2} Site Meter -->/ }
	]

