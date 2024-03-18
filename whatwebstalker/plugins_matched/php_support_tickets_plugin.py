import sys
import os
			
class php_support_tickets_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<a href="http:\/\/www\.phpsupporttickets\.com" target="_blank" title="php support tickets">PHP Support Tickets v([^\s^<]+)<\/a><br \/><br \/>/ }
			{ "text" : '<title>PHP Support Tickets :: Login</title>' }
			{ "certainty" : '75", "text" : '<meta name="copyright"   content="Triangle Solutions Ltd" />' }
			{ "regexp" : '/<!--<td class="boxborder list-menu" width="10%"><a href="javascript:popwindow\('help\.php#userpage','top=150,left=300,width=400,height=400,buttons=no,scrollbars=YES,location=no,menubar=no,resizable=no,status=no,directories=no,toolbar=no'\)" title="Help popup">Help<\/a><\/td>-->/ }
	]

