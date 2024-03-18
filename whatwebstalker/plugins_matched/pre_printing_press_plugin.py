import sys
import os
			
class Pluginpre_printing_press_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<p align="left"><select id="mylist" name="mylist" onchange = "go()" style="font-family:" },
			{ "text" : "<input id="ib_attrib_disk_quantity-2" type="radio" onClick="showsubcat(this.value)" value="olduser" name="allusers" />" },
			{ "text" : "<div align="center">&copy; Copyright PreProjects.com All Rights Reserved</div>" },
		]
		return(self.rules)

