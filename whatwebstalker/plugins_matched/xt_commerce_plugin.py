import sys
import os
			
class xt_commerce_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/<!--\n	This OnlineStore is brought to you by XT-Commerce", "Community made shopping\n	XTC is a free open source e-Commerce System\n	created by Mario Zanier & Guido Winger and licensed under GNU\/GPL.\n	Information and contribution at http:\/\/www.xt-commerce.com\n-->/ }
			{ "version" : '/<meta name="generator" content="\(c\) by xt:Commerce v([^,]{1,15}) ", "http:\/\/www.xt-commerce.com" \/>/ }
			{ "module" : /<meta name="generator" content="\(c\) by (eComBASE V[\d\.]{1,15})", "http:\/\/www.ecombase.de\/" \/>/ }
			{ "module" : /<meta name="generator" content="\(c\) by (xtcModified v[\d\.]{1,15}) dated: [\d]{4}-[\d]{2}-[\d]{2} ", "http:\/\/www.xtc-modified.org" \/>/ }
			{ "text" : '<meta name="generator" content="(c) by xtcModified ", "http://www.xtc-modified.org" />", "module" : 'xtcModified" }
			{ "text" : '<meta name="generator" content="(c) by xtcModified ----- http://www.xtc-modified.org" />", "module" : 'xtcModified" }
			{ "regexp" : '/<div class="copyright">eCommerce Engine &copy; [\d]{4} <a href="http:\/\/www.xt-commerce.com[\/]?" target="_blank">xt:Commerce Shopsoftware<\/a>/ }
			{ "regexp" : '/<div class="copyright"><a rel="follow" href="http:\/\/[^>^"]*\/ecombase.php" title="eComBASE licence">eComBASE<\/a> &copy; [\d]{4} based on /", "module" : 'eComBASE" }
			{ "module" : /<div class="copyright"><a href="http:\/\/www.xtc-modified.org" target="_blank">(xtcModified v[\d\.]{1,15}) dated: [\d]{4}-[\d]{2}-[\d]{2}<\/a>/ }
			{ "text" : '<div class="copyright"><a href="http://www.xtc-modified.org" target="_blank">xtcModified</a>", "module" : 'xtcModified" }
		]

