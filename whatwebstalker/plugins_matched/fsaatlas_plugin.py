import plugins
			
class Pluginfsaatlas_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<title>fsaATLAS Enterprise v\.([^\s^<]+)<\/title>/" },
			{ "version" : "/<div style="position:absolute; width:100px; top:0px; right:0px"><img src="images\/fsaatlastext\.png" alt="fsaATLAS Enterprise v\.([^\s^"]+)"\/><\/div>/" },
			{ "text" : "<form action="LoginFinish.asp" method="post" name="MainForm">" },
			{ "text" : "<!-- AP - 06/02/2009 - Defect 1533 - Campus DataLink Link not appearing at the top navigation bar-->" },
		]
	return(self.rules)

