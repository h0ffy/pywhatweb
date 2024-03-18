import sys
import os
			
class Pluginmailenable_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "</table><!-- loginPanel_shell_table -->" },
			{ "text" : "<td class="loginPanel_botLeft"><div class="loginPanel_botLeft_div"></div></td>" },
			{ "certainty" : "75", "text" : "<title>MailEnable - Webmail</title>" },
		]

