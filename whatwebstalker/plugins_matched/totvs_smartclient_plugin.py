import sys
import os
			
class totvs_smartclient_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<object\s+classid="clsid:[a-f\d\-]+"\s+codebase="TotvsSmartClientax\.cab#version=([^"]+)"/ },
			{ "string" : /<param name="StartProgram" value="([^"]+)"> <<= Programa/ },
			{ "string" : /<param name="Environment" value="([^"]+)"> <<= Ambiente/ },
			{ "search" : 'headers[TotvsSmartClient]", "regexp" : '/^TotvsSmartClient$/ },
		]

