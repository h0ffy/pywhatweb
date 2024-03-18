import plugins
			
class Plugindatanet_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<td><input class="txt" onkeypress='return keyPress\(this,event\);' type='password'( maxlength='10')? id='password'><\/td><\/tr>[\s]+<tr><td class="ver">\(Version ([^\s^<]+)\)<\/td>/", "offset" : "1 },
			{ "text" : "<div class="scada"><a class="scada" href=\'/scada\'>DataNet Scada Interface</a></div></body>" },
		]
		return(self.rules)

