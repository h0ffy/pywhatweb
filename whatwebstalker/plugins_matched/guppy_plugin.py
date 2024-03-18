import sys
import os
			
class guppy_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="Generator" content="GuppY">' }
			{ "version" : '/<div class="foot"><span class='copyright'>&nbsp; <a class='copyright' href='http:\/\/www.freeguppy.org\/' title='GuppY site' target='_blank'> Site powered by GuppY v([\d\.]+) <\/a>/ }
			{ "version" : '/  <!--\[  GuppY v([\d\.]+) CeCILL Copyright \(C\) [\d]{4}\-[\d]{4} by Laurent Duveau \- http:\/\/www.freeguppy.org\/  \]-->/ }
	]

