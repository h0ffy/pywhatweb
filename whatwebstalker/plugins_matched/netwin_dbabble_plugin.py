import plugins
			
class Pluginnetwin_dbabble_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/^DBabble ([^Server]+)Server Version ([^\ ]+) /", "offset" : "1 },
			{ "version" : "/^DBabble ([^Server]+)Server Version ([^\(]+)\(/" },
			{ "text" : "<title>DBabble login</title>" },
			{ "text" : "<LINK REL = "stylesheet" TYPE = "text/css" HREF = "/cgi/dbabble.cgi?cmd_get_js2=dbabble.css">" },
			{ "text" : "<LINK REL = "stylesheet" TYPE = "text/css" HREF = "/dbabble?cmd_get_js2=dbabble.css">" },
			{ "text" : "<script language="JavaScript" src="/cgi/dbabble.cgi?cmd_get_js2=dbabble.js"></script>" },
			{ "text" : "<script language="JavaScript" src="/dbabble?cmd_get_js2=dbabble.js"></script>" },
			{ "text" : "if (window.top!=window && window.location!="/cgi/dbabble.cgi") {" },
			{ "text" : "if (window.top!=window && window.location!="/dbabble") {" },
			{ "text" : "document.writeln("<b>Warning - DBabble requires a web browser that Supports JavaScript 1.1 or higher.</b><br>");" },
			{ "text" : "<form style="margin:0" name="loginform" method="POST" target="_top" action="/cgi/dbabble.cgi"" },
			{ "text" : "<form style="margin:0" name="loginform" method="POST" target="_top" action="/dbabble"" },
			{ "text" : "<a target=\'helpwin\' href="/help/English/Standard/contents.htm">DBabble Online Help</a><br>" },
			{ "text" : "You can use DBabble securely but slower through your web browser at <a href="http" },
		]
		return(self.rules)

