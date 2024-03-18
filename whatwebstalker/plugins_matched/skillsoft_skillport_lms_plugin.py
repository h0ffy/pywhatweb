import plugins
			
class Pluginskillsoft_skillport_lms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<table id="loginwrapper">\s*<tr><td width="10%"><\/td>\s*<td width="80%"  align="left" class="v">v ([^\s]+)<\/td>/" },
			{ "text" : "<a href="javascript:void(0);showContextSpecificHelp(\'/skillportfe/help/en_US/learnerHelp/23386.htm\');"" },
			{ "string" : /<table border="0" width="100%" id="logobanner">\s+<tr width="100%">\s+<td  width="82%">\s+<img src="https?:\/\/customer\.skillport\.com\/spcustom\/([^\/]+)\/[^"]+" alt="([^"]+) ?Logo"/", "offset" : "0 },
			{ "string" : /<table border="0" width="100%" id="logobanner">\s+<tr width="100%">\s+<td  width="82%">\s+<img src="https?:\/\/customer\.skillport\.com\/spcustom\/([^\/]+)\/[^"]+" alt="([^"]+) ?Logo"/", "offset" : "1 },
			{ "regexp" : "/<div id="poweredbylogo">\s+<img src ="\/skillportfe\/resources\/default\/images\/poweredby\.gif" \/>/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/SP[5-7]\dFE=\d+\.\d+\.\d+/" },
			{ "search" : "headers[x-sp-fe]", "string" : /^(.+)$/" },
		]
		return(self.rules)

