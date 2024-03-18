import plugins
			
class Pluginavaya_secure_router_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "25", "model" : "/<td class="headtext" nowrap>Router Model: (<font size=2>)?<b>([^\s^<]+)[\s]*(&nbsp;)?<\/b><\//", "offset" : "1 },
			{ "text" : "<td class="greytitle" nowrap><b>About Avaya Secure Router</b></td>" },
			{ "certainty" : "25", "text" : "<td class="headtext" nowrap><font class="yellowbullet">&#149;</font> <a href="javascript:telnetToBox();">Telnet</a></td>" },
			{ "text" : "<font color="white" style="font-size:30px;"><span id="guiname">Avaya Secure Router</span></font>" },
			{ "search" : "headers[server]", "version" : "/^Avaya Http Server v([^\s]+)$/" },
		]
		return(self.rules)

