import plugins
			
class Pluginatvise_webmi_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "regexp" : "/^atvise$/" },
			{ "text" : "<td><noscript>N/A</noscript><script type="text/javascript"><!--" },
			{ "url" : "/visu.htm", "text" : "<li class="btn"><a class="button" style="left:93%;" href="javascript:void(0)" target="mainframe" id="alarmlistbutton"><img height="30" width="47" src="buttonc.gif" alt=" /></a></li>" },
		]
		return(self.rules)
