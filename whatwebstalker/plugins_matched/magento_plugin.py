import sys
import os
			
class magento_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'images/logo.gif" alt="Magento Commerce" /></a></h1>", "name" : 'default logo alt-text'}
			{ "version" : '%r{<a href="http://www.magentocommerce.com/bug-tracking" id="bug_tracking_link"><strong>Report All Bugs</strong></a> \((Magento Connect Manager |Downloader )?ver. ([0-9\.]+)\)}", "offset" : '1 }
			{ "regexp" : '%r{<link rel="stylesheet" type="text/css" href="[^"]+/skin/frontend/[^"]+/css/boxes.css" media="all"}", "name" : '/skin/front/*/css/boxes.css"}
			{ "name" : 'Meta keywords", "text" : '<meta name="keywords" content="Magento", "Varien", "E-commerce" />'}
			{ "text" : 'var searchForm = new Varien.searchForm('search_mini_form", "'search", "'"}
			{ "text" : ',mage/cookies.js" ></script>'}
			{ "regexp" : '/<div id="noscript-notice" class="magento-notice">/", "name" : 'JavaScript disabled warning'}
			{ "regexp" : '%r{<p>You must have JavaScript enabled in your browser to utilize the functionality of this website.</p>}", "name" : 'JavaScript disabled warning' }
			{ "url" : '/admin',"text" : '<title>Log into Magento Admin Page</title>'}
			{ "name" : 'Copyright footer", "string" : /Magento is a trademark of Magento Inc. Copyright &copy; ([0-9]{4}) Magento Inc/ }
			{ "name" : 'cookie called magento", "search" : 'headers[set-cookie]", "regexp" : '/^magento=[0-9a-f]+/ }
			{ "name" : 'cookie called frontend", "search" : 'headers[set-cookie]", "regexp" : '/^frontend=[0-9a-z]+/ }
			{ "name" : 'cookie called CUSTOMER", "search" : 'headers[set-cookie]", "regexp" : '/^CUSTOMER/i", "certainty" : '25 }
			{ "text" : '<script type="text/x-magento-init">' }
	]

