import sys
import os
			
class Pluginclipbucket_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "string" : /<meta name="copyright" content="ClipBucket - PHPBucket ClipBucket 2007 - (20[\d]{2})" \/>/" },
			{ "text" : "<meta name="author" content="Arslan Hassan - http://clip-bucket.com/arslan-hassan" />" },
			{ "text" : "<!-- ClipBucket v2 -->", "version" : "2.x" },
			{ "version" : "/<!-- ClipBucket version ([\d\.]+) -->/" },
			{ "text" : "<!-- Setting Template Variables -->" },
			{ "text" : "<!-- Forged by ClipBucket -->" },
			{ "text" : "<!-- Forged by ClipBucket ends -->" },
			{ "text" : "<!-- Please do not remove this unless you have license -->" },
			{ "text" : "Forged by <a href="http://clip-bucket.com/">ClipBucket</a>" },
			{ "search" : "headers[set-cookie]", "regexp" : "/pageredir=https?%3A%2F%2F/", "certainty" : "25 },
		]

