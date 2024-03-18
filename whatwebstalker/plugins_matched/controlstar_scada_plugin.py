import sys
import os
			
class controlstar_scada_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<APPLET archive="scada.jar", "toolbox.jar", "batik.jar", "crimson-parser.jar" code="Scada" style="position:absolute;left:0;top:0;width:expression(document.body.clientWidth);height:expression(document.body.clientHeight);" >' }
	]

