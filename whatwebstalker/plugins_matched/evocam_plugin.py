import plugins
			
class Pluginevocam_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<title>EvoCam( \d)*<\/title>/" },
			{ "regexp" : "/<TITLE>EvoCam( Java| JavaScript)? Example Page<\/TITLE>/" },
			{ "text" : "Powered by <A HREF="http://www.evological.com/evocam.html">EvoCam</A>" },
			{ "regexp" : "/<applet archive="evocam.jar" code="com.evological.evocam.class"/" },
			{ "regexp" : "/<param name="archive" value="evocam.jar">/i },
		]
			return(self.rules)
