import plugins


class Pluginwow_raid_manager_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"certainty": "75", "ghdb": "Raid Management Provided by WoW Raid Manager"" },
			{ "version" : "/Raid Management Provided by <a href="http:\/\/www.wowraidmanager.net\/">WoW Raid Manager<\/a> v([\d\.]+)/" },
		]
	return(self.rules)
