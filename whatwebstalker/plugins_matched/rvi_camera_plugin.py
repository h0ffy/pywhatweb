import sys
import os
			
class Pluginrvi_camera_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Скачать файл установки OCX&nbsp;&nbsp;&nbsp;<a href="xdview.exe">", "url" : "/login.asp" },
			{ "text" : "<Meta name="Author" Content="hhdigital">'},
		]
		return(self.rules)

