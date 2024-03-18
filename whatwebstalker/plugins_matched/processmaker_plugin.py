import sys
import os
			
class processmaker_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<div class="x-pm-footer-text">\s+ProcessMaker Ver\. ([^\s]+)<br\/>/ }
			{ "text" : '<div class="companyLogo"><img src="/images/processmaker2.logo2.png"/></div>' }
			{ "text" : '<a href="http://www.processmaker.com" alt="Powered by ProcessMaker - Open Source Workflow & Business Process Management (BPM) Management Software" title="Powered by ProcessMaker" target="_blank">' }
			{ "text" : '<div class="content"><a href="#" onclick="openInfoPanel();return false;" class="FooterLink">| System Information |</a><br /><br />Copyright &copy; 2003-2012 <a href="http://www.colosa.com" alt="Colosa", "Inc." target="_blank">Colosa", "Inc.</a> All rights reserved.' }
			{ "text" : '<meta http-equiv="REFRESH" content="0;URL=/sys/en/classic/login/login.html" />' }
	]
