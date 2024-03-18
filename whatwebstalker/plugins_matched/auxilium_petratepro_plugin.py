import sys
import os
			
class Pluginauxilium_petratepro_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "text" : "<form method="post" name="myform2" action="index.php?cmd=11">" },
			{ "text" : "<p class="text"><b>Leader Of The Pack (Top 10 Pets)</b><br><br>" },
		]

