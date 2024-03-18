import sys
import os
			
class cype_mscms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '25", "regexp" : '/<title>[^\(^<]+ \(Powered by Cype\)<\/title>/ }
			{ "text" : '<meta name="author" content="cypedev.com" />' }
			{ "text" : '<li><i>All images and other contents related to <a href='http://maplestory.com/' target='_blank'>MapleStory</a>&trade; are owned by <a href='http://nexon.net/' target='_blank'>Nexon Corporation</a></i><br /></li>" }
			{ "version" : '/<li>Powered By Cype MSCMS ([\d\.]+) &copy; 20[\d]{2} <a href="http:\/\/www.imurad.net" target="_blank">CypeDEV\/iMurad.net<\/a><br \/><\/li>/ }
			{ "version" : '/<li>Powered By Cype MSCMS ([\d\.]+) &copy; 20[\d]{2} <a href="http:\/\/www.cypedev.com" target="_blank">Cype Developments<\/a><br \/><\/li>/ }
	]

