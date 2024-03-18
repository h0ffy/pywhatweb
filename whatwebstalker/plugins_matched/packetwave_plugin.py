import plugins
			
class Pluginpacketwave_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<td bgcolor="#cccccc" colspan=2 align="center"><input type="button" name="goto" value="Log On" onClick="encode_submit(this.form)">" },
		]
			return(self.rules)
