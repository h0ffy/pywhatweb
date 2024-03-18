import plugins
			
class Plugincanon_network_camera_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75,"ghdb" : "intitle:liveapplet inurl:LvAppl'},
			{ "certainty" : "75,"ghdb" : "+intitle:"Network Camera VB-C50i/VB-C50iR" +"Viewer for PC"'},
			{ "text" : "<TITLE>Network Camera VB-C50i/VB-C50iR</TITLE>", "version" : "'VB-C50i'},
			{ "text" : "function L(n,g) {var i=document.images[n]; if (i)I[n]=new H(i,i.src,"/v/"+g+".gif")}',"version" : "VB-C50i"},
			{ "text" : "function L(n,g) {var i=document.images[n];if (i)I[n]=new H(i,i.src,"/v/"+g+".gif")}',"version" : "VB-C50i"},
			{ "text" : "<param name=cabbase	value="LiveApplet.cab">',"version" : "WebView"},
			{ "text" : "<title>LiveApplet</title>',"version" : "WebView"},
		]
	return(self.rules)
