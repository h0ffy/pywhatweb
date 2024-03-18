import sys
import os
			
class twonkyserver_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/TwonkyMedia UPnP/ }
			{ "text" : '<meta name="description" content="TwonkyMedia Digital Home">' }
			{ "text" : '<td><strong><font color="#294A94" size="2">TwonkyMedia Settings</font></strong></td>' }
			{ "text" : '<html><head><title>TwonkyServer Media Browser</title>' }
			{ "text" : '<html><head><title>TwonkyMedia server media browser</title>' }
			{ "string" : /<div id="copyright" class="copyright">Copyright . 2004-(20[\d]{2}) PacketVideo Corporation\. All rights reserved\.<\/div><\/div><hr>/ }
			{ "string" : /<div id="copyright" class="copyright">Copyright&nbsp;&copy;&nbsp;2004-20(20[\d]{2}) PacketVideo&nbsp;Corporation\. All&nbsp;rights&nbsp;reserved<\/div><\/div><hr>/ }
	]
