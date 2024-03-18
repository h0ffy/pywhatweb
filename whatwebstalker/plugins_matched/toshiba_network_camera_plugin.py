import plugins
			
class Plugintoshiba_network_camera_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>TOSHIBA Network Camera - User Login</title>" },
			{ "text" : "    <td height="32"><img src="toshiba.gif" width="68" height="12"><font class="netcam"><strong>&nbsp;&nbsp;Network Camera</strong></font></td>" },
		]
		return(self.rules)
