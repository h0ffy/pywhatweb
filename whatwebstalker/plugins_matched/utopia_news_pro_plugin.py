import plugins
			
class Pluginutopia_news_pro_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="Utopia News Pro - http://www.utopiasoftware.net/"/>" },
			{ "version" : "/<div align="center" class="fbox smallfont">\s*<!-- Copyright -->\s*Powered By: <a href="about\.php[^"^>]*">Utopia News Pro<\/a> ([^<]+)</" },
			{ "text" : "<!-- Beta: editnews2.php -->" },
			{ "text" : "<div class="sf">News generated by <a href="http://www.utopiasoftware.net">Utopia News Pro</a></div>" },
			{ "text" : "<!-- PrintNews.Bit -->" },
		]
		return(self.rules)

