import sys
import os
			
class utopia_news_pro_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<meta name="generator" content="Utopia News Pro - http://www.utopiasoftware.net/"/>' }
			{ "version" : '/<div align="center" class="fbox smallfont">\s*<!-- Copyright -->\s*Powered By: <a href="about\.php[^"^>]*">Utopia News Pro<\/a> ([^<]+)</ }
			{ "text" : '<!-- Beta: editnews2.php -->' }
			{ "text" : '<div class="sf">News generated by <a href="http://www.utopiasoftware.net">Utopia News Pro</a></div>' }
			{ "text" : '<!-- PrintNews.Bit -->' }
		]

