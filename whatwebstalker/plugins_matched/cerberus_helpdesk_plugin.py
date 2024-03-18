import plugins
			
class Plugincerberus_helpdesk_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[set-cookie]", "regexp" : "/CerberusPublicGUI=[a-f\d]{32};/" },
			{ "text" : "<!-- If you have your own stylesheet for HTML elements", "you can remove the cerberus-html.css link -->" },
			{ "text" : "<td width="519" class="kb_most_viewed_articles">Most Viewed Knowledgebase Articles</td>" },
		]
	return(self.rules)

