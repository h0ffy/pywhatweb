import plugins
			
class Pluginnovell_netware_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "</HEAD><BODY><font size=+2><p>Unauthorized!</font><font size=+1><p>Please login using a full NDS name and context (example: .user.engineering.acme_corp.)</font></BODY></HTML>" },
			{ "regexp" : "/<TITLE>NetWare Server [^<]+<\/TITLE><LINK REL=stylesheet TYPE=text\/css HREF=\/SYS\/LOGIN\/portal\.css>/" },
			{ "text" : "<APPLET CODE=NWSHealth.class NAME="NWServerHealth" CODEBASE=/SYS/Login width=38 height=99>" },
			{ "url" : "/", "version" : "/<br>&nbsp;&nbsp;<font color=teal size=-1><B>Novell (NetWare|Small Business Suite) ([^<]+)<\/B><\/font><br>/", "offset" : "1 },
			{ "url" : "/", "module" : /&nbsp;&nbsp;<font color=teal size=-1><b>(Server Version [\d\.]+ revision [A-Z]),[\s]+([A-Z][a-z]+ [\d]{1,2}", "[\d]{4}|[\d]{1,4} [A-Z][a-z]+ [\d]{1,4})<\/B><\/font><br>/" },
			{ "url" : "/", "module" : /&nbsp;&nbsp;<font color=teal size=-1><b>NetWare (Management Portal Version [^,]+),[\s]+([A-Z][a-z]+ [\d]{1,2}", "[\d]{4}|[\d]{1,4} [A-Z][a-z]+ [\d]{1,4})<\/B><\/font><br>/" },
			{ "url" : "/TOP.HTML", "text" : "<TABLE WIDTH="100%"><TR><TD ALIGN=LEFT VALIGN=TOP><APPLET CODE="NWSHealth.class" NAME="NWServerHealth" CODEBASE="/SYS/Login" width=33 height=52>" },
			{ "url" : "/TOP.HTML", "version" : "/<TD ALIGN=RIGHT VALIGN=TOP><font color="#524a18" size=-1><B>Novell NetWare ([^<]+)<\/B>/" },
			{ "url" : "/TOP.HTML", "module" : /<font color="#524a18" size=-1><b>(Server Version [\d\.]+ revision [A-Z]),[\s]+([A-Z][a-z]+ [\d]{1,2}", "[\d]{4}|[\d]{1,4} [A-Z][a-z]+ [\d]{1,4})<\/B><\/font><BR>/" },
			{ "url" : "/TOP.HTML", "module" : /<font color="#524a18" size=-1><b>NetWare (Management Portal Version [\d\.]+ revision [A-Z]),[\s]+([A-Z][a-z]+ [\d]{1,2}", "[\d]{4}|[\d]{1,4} [A-Z][a-z]+ [\d]{1,4})<\/B><\/font><BR>/" },
		]
		return(self.rules)
