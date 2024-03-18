import sys
import os
			
class cerberus_helpdesk_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[set-cookie]", "regexp" : '/CerberusPublicGUI=[a-f\d]{32};/ }
			{ "text" : '<!-- If you have your own stylesheet for HTML elements", "you can remove the cerberus-html.css link -->' }
			{ "text" : '<td width="519" class="kb_most_viewed_articles">Most Viewed Knowledgebase Articles</td>' }
	]

