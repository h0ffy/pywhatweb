b'''
import plugins

class Pluginipeer_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r"/<title>iPeer V(\\d) with TeamMaker<\\/title>/" },
            { "text" : r'<h1 align="center"><span class="footer">Powered by iPeer and TeamMaker - Created by UBC and Rose-Hulman</span></h1>' },
            { "version" : r'/<span class="bannerText"><span style=\'font-size: 120%;\'>([^<]+)<\\/span>&nbsp;&nbsp;with TeamMaker<\\/span><\\/td>/' },
            { "search" : "headers[set-cookie]", "regexp" : r"/IPEER=[^;]+;/" },
        ]
        return self.rules
'''