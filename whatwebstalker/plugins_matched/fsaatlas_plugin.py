import sys
import os
			
class fsaatlas_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : "/<title>fsaATLAS Enterprise v\.([^\s^<]+)<\/title>/" },
			{ "version" : "/<div style="position:absolute; width:100px; top:0px; right:0px"><img src="images\/fsaatlastext\.png" alt="fsaATLAS Enterprise v\.([^\s^"]+)"\/><\/div>/" },
			{ "text" : "<form action="LoginFinish.asp" method="post" name="MainForm">" },
			{ "text" : "<!-- AP - 06/02/2009 - Defect 1533 - Campus DataLink Link not appearing at the top navigation bar-->" },
		]

