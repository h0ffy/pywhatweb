import plugins
			
class Pluginintoto_router_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "model" : "/<td class="headtext" nowrap>Router Model: (<font size=2>)?<b>([^\s^<]+)[\s]*(&nbsp;)?<\/b><\//", "offset" : "1 },
			{ "text" : "<td class="greytitle" nowrap><b>About Device Manager </b></td> " },
			{ "certainty" : "25", "text" : "<td class="headtext" nowrap><font class="yellowbullet">&#149;</font> <a href="javascript:telnetToBox();">Telnet</a></td>" },
			{ "regexp" : "/<body bgcolor=#E6E6E6 leftmargin=0 topmargin=0 marginheight=0 marginwidth=0 style="padding: [\d]{1,2}px" onload="javascript:usrnameFocus\(\);javascript:isValidBrowser\(\);/" },
			{ "search" : "headers[server]", "version" : "/^Intoto Http Server v([^\s]+)$/" },
		]
		return(self.rules)

