import sys
import os
			
class sazcart_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/[^&]+&raquo; Powered by SazCart<\/title>/ }
			{ "text" : '<a href="http://www.sazcart.com">Powered by SazCart</a> | <a href="http://www.sazcart.com">Copyright &#169; 2005 - 2006 SazCart.com</a>  </div>' }
	]

