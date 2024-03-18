import plugins
			
class Pluginhp_virtual_connect_manager_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- HP Virtual Connect Manager                                            -->" },
			{ "text" : "<h2><img src="./images/progress_bar_large.gif"></h2><br />Loading", "please wait..." },
			{ "string" : /<!--[\s]+\(C\) Copyright (20[\d]{2}) Hewlett-Packard Development Company", "L\.P\.[\s]+-->/" },
			{ "url" : "/html/index.html", "text" : "<title>HP Virtual Connect Manager</title>" },
			{ "url" : "/html/index.html", "text" : "<frame id='MX_HIDDEN' name='MX_HIDDEN' src=\"common/hiddenFrame.html\" noresize>" },
		]
		return(self.rules)
