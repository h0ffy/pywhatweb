import sys
import os
			
class pegarules_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : 'cookie',"search" : 'headers[set-cookie]","text" : 'Pega-RULES"}
			{ "name" : 'title", "text" : '<title> Welcome to PegaRULES </title>' }
			{ "name" : 'copyright footer',"regexp" : '/<span>[^<]+Copyright[^<]+Pegasystems Inc/m}
			{ "name" : 'shortcut icon',"text" : '<LINK REL="SHORTCUT ICON" HREF="images/pzPegaIcon.ico">'}
			{ "version" : '/td style="text-align: center;"><span id="ProductVersion" class="ProductVersion">Version ([^<]+)<\/span><\/td/ }
			{ "text" : '<!-- B-12380 avoid reuse/repost of username/password -->' }
			{ "text" : '<HEAD><H3>Unable to logon to the PegaRULES system.</H3></HEAD>' }
			{ "regexp" : '/<TR><TD>\s+<FONT face="Helvetica">\s+Your system policy has denied access to the requested URL\.\s+<\/FONT>/ }
	]
