import plugins
			
class Pluginpjirc_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<body onload="document.login.nick.focus();" style="margin: 5px;">" },
			{ "text" : "					document.writeln(\'<input name="jsenabled" type="hidden" value="1" \/>\');" },
			{ "regexp" : "/				<form name="login" action="[^"]*index\.php" method="post" onsubmit="return CheckForm\('[^']*index\.php\?page=advanced'\)">/" },
			{ "version" : "/	<td align="left">PJIRC Login Page Version ([\d\.]{1,5})<\/td>/" },
		]
		return(self.rules)
