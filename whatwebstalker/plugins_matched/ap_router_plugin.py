import plugins
			
class Pluginap_router_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<frame marginwidth="5" marginheight="5" src="menu_empty.html" name="menu" noresize scrolling="auto" frameborder="0">" },
			{ "url" : "/status.asp", "firmware" : "/<td width=49% bgcolor="#EEEEEE"><strong>Vers&atilde;o do Firmware<\/strong><\/td>[\s]+<td width=51% bgcolor="#EEEEEE">[\s]+v([^\s]+)[\s]+<\/td>[\s]+<\/tr>/" },
			{ "url" : "/status.asp", "string" : /<td width=49% bgcolor="#EEEEEE"><strong>MAC da Wireless<\/strong><\/td>[\s]+<td width=51% bgcolor="#EEEEEE">[\s]+([a-f\d:]{17})[\s]+<\/td>[\s]+<\/tr>/" },
			{ "url" : "/status.asp", "string" : /<td width=49% bgcolor="#EEEEEE"><strong>Endere&ccedil;o[\s]+MAC<\/strong><\/td>[\s]+<td width=51% bgcolor="#EEEEEE">[\s]+([a-f\d:]{17})[\s]+<\/td>[\s]+<\/tr>/" },
		]
		return(self.rules)
