import sys
import os
			
class webbased_pear_package_manager_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<img src="?img=pear" width="104" height="50" vspace="2" hspace="5" alt="PEAR">' },
			{ "text" : '<b>Warning:</b> This package management website is <b>not protected</b> with a password", "this is a MAJOR security risk. Please read the <a href="?command=doc-show&pkg=pear.php.net/PEAR_Frontend_Web&file=README" class="green">README</a>.' },
			{ "version" : '/<td valign="top">[\s]+<a href="[^"]*\/index\.php\?command=info&pkg=pear\.php\.net\/PEAR_Frontend_Web" class="blue">PEAR_Frontend_Web<\/a>[\s]+<\/td>[\s]+<td valign="top">[\s]+([^<^\n]+)[\s]+<\/td>/ },
			{ "string" : /<meta name="description" content="Webbased PEAR Package Manager on ([^"]+)" \/>/ },
		]

