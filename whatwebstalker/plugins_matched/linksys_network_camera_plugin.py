import plugins
			
class Pluginlinksys_network_camera_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="description" content="WVC54GCA">", "model" : "WVC54GCA" },
			{ "text" : "<td bgcolor="#6766CC" align="right" valign="top"><span class="model" style="position:relative;top:-12px">WVC54GCA</span><img src="../blue_top_right.gif" alt=" border="0">", "model" : "WVC54GCA" },
			{ "text" : "<meta name="description" content="WVC80N">", "model" : "WVC80N" },
			{ "text" : "<td bgcolor="#6766CC" align="right" valign="top"><span class="model" style="position:relative;top:-12px">WVC80N</span><img src="../blue_top_right.gif" alt=" border="0">", "model" : "WVC80N" },
		]
		return(self.rules)
