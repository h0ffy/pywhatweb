import sys
import os
			
class wow_raid_manager_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : "75", "ghdb" : "Raid Management Provided by WoW Raid Manager"" },
			{ "version" : "/Raid Management Provided by <a href="http:\/\/www.wowraidmanager.net\/">WoW Raid Manager<\/a> v([\d\.]+)/" },
		]

