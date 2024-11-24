import plugins


class Plugininformatics_cms_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"search": "headers[set-cookie]",
     "regexp": "/[\\d]+=HTMLTitle=[^\\s]*&OrgName=[^\\s]+&EmailThankYou=[^\\s]*&DefaultIdPage=[^\\s]+&State=/"},
			{"text": "<meta name="author" content="Informatics", "Inc.">"},
			{"regexp": "/Web Application by <a href="http: \/\/www\.(ia-informatics|informaticsinc)\.com" [^>]*target="_blank"><b>Informatics", "Inc\.<\/b><\/a>/" },
		]
	return(self.rules)
