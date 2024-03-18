import plugins
			
class Pluginvisionweb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "search" : "headers[server]", "regexp" : "/^IWeb\/([^\s]+)/" },
			{ "version" : "/VarPageTitle="Proxima\d? DVMS VisionWEB v([^\s^"]+)";/" },
			{ "text" : "<b>CIEFFE srl</b> - "We power Your eyes"<br" },
			{ "string" : /<meta name="COPYRIGHT" content="&copy; 2001-(2[\d]{3}) Insignis Technologies"/" },
		]
	return(self.rules)
