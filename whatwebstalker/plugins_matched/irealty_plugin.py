import sys
import os
			
class Pluginirealty_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://www.irealty.com/" title="iRealty"> iRealty </a>" },
			{ "text" : "<a target="_blank" href="http://www.irealtysoft.com/">- Powered by iRealty</a>" },
			{ "text" : "Powered by <a target="_blank" title="iRealty &mdash; Real Estate Listing Software" href="http://www.irealtysoft.com/">iRealty</a>," },
			{ "text" : "Powered by <a target="_blank" title="iRealty &mdash; Real Estate Listing Software" href="http://www.worksforweb.com/products/iRealty/">iRealty</a>," },
		]
		return(self.rules)

