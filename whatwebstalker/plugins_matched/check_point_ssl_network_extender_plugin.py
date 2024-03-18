import sys
import os
			
class check_point_ssl_network_extender_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[server]", "regexp" : '/^Check Point SVN foundation$/ }
			{ "regexp" : '/<script src="cookies\.js"><\/script>[\s]+<script>document\.write\(conn_html\)<\/script>[\s]+<HEAD>/ }
			{ "url" : '/help_data.html", "regexp" : '/<meta name=Generator content="Microsoft Word 11 \(filtered\)">[\s]+<title>Check Point SSL Network Extender HELP<\/title>/ }
			{ "url" : '/logo.gif", "md5" : 'a5be381441844d96e70407481e1390b1" }
			{ "text" : '<meta name="description" content="Webui Login Page"/>  <!-- changes to this line must be reflected in sfwOverrides.js & lm_home.js -->", "string" : 'Security Gateway" }
			{ "version" : '/<form autocomplete="off" method="post" action="\/platform\.cgi\?" target="_top">[\s]+<input type="hidden" name="thispage" value="index\.htm">[\s]+<div class="version_div">([^<]+)<\/div>/", "string" : 'Security Gateway" }
		]

