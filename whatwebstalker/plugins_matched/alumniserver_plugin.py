import sys
import os
			
class alumniserver_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75", "ghdb" : 'inurl:AlumniServerProject.php "AlumniServer project"' },
			{ "text" : '<div style="float:right;"><a href="AlumniServerProject.php" style="color:#c6cccd;margin:2px;margin-right:10px;">AlumniServer project</a></div>' },
			{ "text" : '<div style="margin:25px 15px 20px 15px;"><noscript><div style="color:red;margin-bottom: 15px;">Your browser does not support JavaScript!</div></noscript><h2>The AlumniServer project</h2>' },
			{ "certainty" : '25", "text" : '<meta name="keywords" content="Alumni,Student,Network,Community,University">' },
		]

