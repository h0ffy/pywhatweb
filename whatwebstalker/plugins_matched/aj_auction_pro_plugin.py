import sys
import os
			
class Pluginaj_auction_pro_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "25", "ghdb" : "Powered By AJ Auction Pro"" },
			{ "version" : "/<td width="16%" class="site_statistics" align="left"><a class="site_statistics" href="http:\/\/www.ajauctionpro.com">Powered By AJ Auction Pro OOPD V([\d\.]{1,5})<\/a><\/td>/" },
		]

