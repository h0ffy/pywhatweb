import sys
import os
			
class Pluginbluenet_video_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "string" : "window.location.href='/cgi-bin/client_execute.cgi?tUD=0';"},
			{ "version" : "/<title>BlueNet Video Viewer Version ([^<]+)<\/title>/", "url" : "/cgi-bin/client_execute.cgi?tUD=0'},
			{ "string" : "clsid:4A7C606D-03DB-4E91-9AB0-275F5A4599FD", "url" : "/cgi-bin/client_execute.cgi?tUD=0'},
		]

