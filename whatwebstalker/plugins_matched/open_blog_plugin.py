import sys
import os
			
class open_blog_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/Powered by <a href="http:\/\/www.open-blog.info[\/]*" target="_blank">Open Blog<\/a>/ },
			{ "text" : 'Powered by <a href="http://www.open-blog.info"' },
			{ "text" : '    	Powered by <a href="http://www.open-blog.info" target="_blank">Open Blog</a>' },
			{ "version" : '/			<a href="install.php">Install Open Blog<\/a> - choose this option", "if you would like to install Open Blog ([\d\.]+)<br \/>/ },
		]

