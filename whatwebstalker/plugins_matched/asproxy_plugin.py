import sys
import os
			
class Pluginasproxy_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<!-- Surf the web invisibly using ASProxy power. A Powerfull web proxy is in your hands. -->" },
			{ "text" : "<!--This is ASProxy powered by SalarSoft. -->" },
			{ "text" : "<input type="button" onclick="_Page_SubmitForm()" value="Display" id="btnASProxyDisplayButton" class="Button" />" },
			{ "version" : "/asproxydone="2"(\ style="font-weight:[\s]*bold;[\s]*text-decoration:[\s]*none")?>ASProxy ([^\s^<]+)<\/a>/", "offset" : "1 },
		]

