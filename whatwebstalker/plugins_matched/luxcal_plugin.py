import sys
import os
			
class luxcal_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : "75", "text" : "<meta name="description" content="LuxCal web calendar - a LuxSoft product" />" },
			{ "certainty" : "75", "text" : "<link rel="shortcut icon" href="lcal.ico" />" },
			{ "certainty" : "75", "text" : "<meta name="author" content="Roel Buining" />" },
			{ "text" : "<span class=\"floatR\"><a href=\"http://www.luxsoft.eu\"><font size='1'>powered by </font><i><b><font size='2' color='#0033FF'>Lux</font><font size='2' color='#AA0066'>Soft</font></b></i></a></span>" },
			{ "version" : "/<b><i><font size='2' color='#0033FF'>Lux<\/font><font size='2' color='#AA0066'>Cal<\/font><\/i><\/b><font size='1'> version ([^<]+)<\/font>/" },
		]

