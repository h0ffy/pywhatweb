import plugins
			
class Plugintruition_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<A HREF="/cgi-bin/ncommerce3/ExecMacro/search.d2w/report?wl=151">Search</A>&nbsp;|&nbsp;" },
			{ "text" : "<!--Logon Information-faq answers below-->" },
			{ "ghdb" : "inurl:"/cgi-bin/ncommerce3/ExecMacro/static/" filetype:d2w" },
			{ "text" : "<li>DTWF050E: Net.Data is unable to locate the HTML block specification in the URL." },
			{ "text" : "<li>DTWP001E: Net.Data is unable to locate the macro file" },
			{ "text" : "location.href = "/cgi-bin/ncommerce3/ExecMacro/static/" },
		]
		return(self.rules)
