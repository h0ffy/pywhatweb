import sys
import os
			
class aja_video_converter_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>AJA Video - FS1 Admin: Main</title> <link href="/css/aja_fs1.css"", "model" : 'FS1" }
			{ "url" : '/json?action=get&configid=0&alt=json&paramid=eParamID_SysName", "string" : /\{"paramid":"839188480","name":"eParamID_SysName","value":"([^\"]+)"/ }
		]

