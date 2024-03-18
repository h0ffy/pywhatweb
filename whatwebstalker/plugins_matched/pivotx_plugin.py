import sys
import os
			
class pivotx_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<!-- PivotX -->' }
			{ "text" : '<script src="includes/js/pivotx.js" type="text/javascript"></script>' }
			{ "text" : '<img src="templates_internal/assets/pivotx.png" alt="PivotX" /></a>' }
			{ "version" : '/<em>PivotX - ([^<]+)<\/em> &nbsp; - &nbsp; &copy; 20[\d]{2}/ }
			{ "text" : '<meta name="generator" content="PivotX" />' }
			{ "version" : '/<meta name="generator" content="PivotX" \/><!-- version: PivotX - ([^\s]+) -->/ }
	]
