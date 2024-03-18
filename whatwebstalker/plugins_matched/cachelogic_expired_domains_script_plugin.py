import sys
import os
			
class cachelogic_expired_domains_script_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : "<option value="30">Last 30 days</option><option value="21">Last 21 days</option><option value="14">Last 14 days</option><option value="7">Last 7 days</option><option value="6">Last 6 days</option><option value="5">Last 5 days</option><option value="4">Last 4 days</option><option value="3">Last 3 days</option><option value="2">Last 2 days</option><option value="1">Last 1 days</option>" },
			{ "text" : "<option value="15">15</option><option value="12">12</option><option value="10">10</option><option value="8">8</option><option value="7">7</option><option value="6">6</option><option value="5">5</option><option value="4">4</option><option value="3">3</option><option value="2">2</option>" },
			{ "text" : "<br><br><br>Website is powered by <a href="http://cachelogic.net">Cachelogic.net</a>" },
			{ "string" : "Free", "text" : "<!-- Please do not remove. It is illegal to remove this footer in Cachelogic Expired Domains Free Edition-->" },
			{ "text" : "href="http://cachelogic.net">Cachelogic.net</a></td></tr>" },
		]

