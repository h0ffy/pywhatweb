import plugins
			
class Plugincodesys_web_visualization_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<TITLE>CoDeSys WebVisualization</TITLE>" },
			{ "text" : "<APPLET CODEBASE=. CODE=webvisu/WebVisu.class name="WebVisu" width="100%" height="100%" id="webvisuapplet">" },
			{ "text" : "<APPLET CODEBASE=. CODE=webvisu/WebVisu.class name="WebVisu" width="99%" height="99%" id="webvisuapplet">" },
			{ "text" : "<param name="archive" value="webvisu.jar,minml.jar">" },
		]
	return(self.rules)
