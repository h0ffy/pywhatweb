import sys
import os
			
class canon_printer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "model" : '/<title>Remote UI<Top Page>: (\w+)/i}
			{ "model" : '/<title>Remote UI&lt;Top page&gt;: ([^:]+)/i", "url" : '/frame.cgi"}
			{ "model" : '/<title>Remote UI&lt;Top page&gt;: ([^:]+)/i", "url" : '/frame.cgi?PageFlag=t_frame.tpl"}
			{ "model" : '/<link rel="shortcut icon" type="image\/x-icon" href="G24_favicon\.ico" \/><title>Remote UI \(Top Page\) : [^:^<]* : Canon ([^\s^<]+)<\/title>/ }
			{ "model" : '/<title>Canon ([^\s]+) series Network Configuration \| / }
			{ "url" : '/_top.htm", "text" : '<img src="top_canon.gif" width="123" height="33"' }
			{ "search" : 'headers[server]", "regexp" : '/^Canon Http Server/i }
			{ "search" : 'headers[server]", "version" : '/^Canon Http Server (Ver)?(.*)/i", "offset" : '1 }
			{ "certainty" : '75", "search" : 'headers[server]", "version" : '/^KS_HTTP\/([^\s]+)/ }
			{ "certainty" : '25", "search" : 'headers[server]", "version" : '/^LPC Http Server\/V([^\s]+)/ }
		]

