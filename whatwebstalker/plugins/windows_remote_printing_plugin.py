import plugins


class Pluginwindows_remote_printing_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"ghdb": "inurl:"Printers / ipp_0001.asp" intitle:"All Printers on""},
			{"regexp": "/<frame src="ipp_000[\d]\.asp\?eprinter=/" },
		]
	return(self.rules)
