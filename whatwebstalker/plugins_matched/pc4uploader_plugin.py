import sys
import os
			
class Pluginpc4uploader_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "eval("page" + id + " = window.open(URL", "\'" + id + "\", "\'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=650,height=400,left = 199.5,top = 196.5\');");", "version" : "10.x" },
			{ "version" : "/Pc4Uploader <font color="#000080"> <b>v([\d\.]+)<\/b><\/font>/" },
			{ "version" : "/Pc4Uploader <font color="#000080"> <b>v([\d\.]+) Pro<\/b><\/font>/", "string" : "Pro" },
			{ "version" : "/<p id="legal" style="text-align: center">Powered by Pc4Uploader v<span lang="en-us">([\d\.]+)<\/span><\/p>/" },
			{ "version" : "/Powered by Pc4Uploader <b>v([\d\.]+)<\/b>&nbsp; Copyright <b>/" },
			{ "version" : "/Powered by Pc4Uploader <b>v([\d\.]+) Pro<\/b>&nbsp; Copyright <b>/", "string" : "Pro" },
		]
		return(self.rules)

