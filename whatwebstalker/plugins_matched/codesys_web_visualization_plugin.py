import sys
import os
			
class codesys_web_visualization_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<TITLE>CoDeSys WebVisualization</TITLE>' },
			{ "text" : '<APPLET CODEBASE=. CODE=webvisu/WebVisu.class name="WebVisu" width="100%" height="100%" id="webvisuapplet">' },
			{ "text" : '<APPLET CODEBASE=. CODE=webvisu/WebVisu.class name="WebVisu" width="99%" height="99%" id="webvisuapplet">' },
			{ "text" : '<param name="archive" value="webvisu.jar,minml.jar">' },
		]

