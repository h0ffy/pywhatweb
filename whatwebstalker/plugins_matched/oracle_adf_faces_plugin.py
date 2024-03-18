import sys
import os
			
class oracle_adf_faces_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<!-- Created by Oracle ADF Faces \((Version mismatch: )?ADF Faces API - ([\d_]+)\/ADF Faces Implementation - ([\d_]+)\)", "skin:([^-]+) -->/", "offset" : '1 }
			{ "version" : '/<!-- Created by Oracle ADF Faces \((Version mismatch: )?ADF Faces API - ([\d_]+)\/ADF Faces Implementation - ([\d_]+)\)", "skin:([^-]+) -->/", "offset" : '2 }
			{ "string" : /<!-- Created by Oracle ADF Faces \((Version mismatch: )?ADF Faces API - ([\d_]+)\/ADF Faces Implementation - ([\d_]+)\)", "skin:([^-]+) -->/", "offset" : '3 }
			{ "text" : '<meta name="generator" content="Oracle ADF Faces">' }
			{ "text" : '<script>var _AdfWindowOpenError='A popup window blocker has been detected in your browser. Popup blockers interfere with the operation of this application. Please disable your popup blocker or allow popups from this site.';</script>" }
		]

