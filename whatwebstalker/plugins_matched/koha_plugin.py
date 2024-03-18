import sys
import os
			
class koha_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "md5" : '0c240ea1e838d2b398f48122924bf7a0", "url" : '/opac-tmpl/prog/en/includes/favicon.ico" },
			{ "md5" : '0c240ea1e838d2b398f48122924bf7a0", "url" : '/intranet-tmpl/prog/en/includes/favicon.ico" },
			{ "regexp" : '/<link rel="shortcut icon" href="\/(intranet|opac)-tmpl\/[^\/]+\/[a-z]{2}\/includes\/favicon\.ico" type="image\/x-icon" \/>/ },
			{ "version" : '/<meta name="generator" content="Koha ([^\s^"]+)" \/>/ },
			{ "regexp" : '/<input type="hidden" name="koha_login_context" value="(opac|intranet)" \/>/ },
			{ "text" : '<link rel="stylesheet" type="text/css" href="/intranet-tmpl/prog/en/lib/jquery/plugins/ui.tabs.css" />' },
			{ "text" : '<link rel="stylesheet" type="text/css" href="/opac-tmpl/prog/en/lib/jquery/plugins/ui.tabs.css" />' },
			{ "text" : '<li><a href="/cgi-bin/koha/lostpassword.pl" title="Password Lost and Found">Lost your password?</a></li>' },
			{ "certainty" : '25", "text" : '<!-- login prompt time-->' },
			{ "text" : '<div id="help"><span class="loggedin">You are not logged in | </span><a href="/cgi-bin/koha/help.pl" onclick="Help(); return false;">[ ? ]</a></div>' },
		]

