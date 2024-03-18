import sys
import os
			
class barracuda_spam_firewall_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<title>Barracuda Spam & Virus Firewall: Welcome</title>", "module" : 'Virus Firewall" },
			{ "text" : '<title>Barracuda Spam Firewall: Welcome</title><link rel="stylesheet" type="text/css" href="/barracuda.css">' },
			{ "text" : '<tr><td valign=top width=680 bgcolor="#ffffff" nowrap><table summary ="Logo Row" cellspacing=0 cellpadding=0 border=0><tr><td><a href="http://www.barracudanetworks.com?track=asg" class=transbutton><img src="' },
			{ "text" : '<a href="http://www.barracudanetworks.com?track=asg"><img src="/images/powered_by.gif" border=0' },
			{ "version" : '/<link rel="stylesheet" type="text\/css" href="\/barracuda.css\?v=([\d\.]+)">/", "module" : 'Virus Firewall" },
			{ "version" : '/<script language=javascript src="\/js_functions.([\d\.]+).js" type="text\/javascript"><\/script>/ },
			{ "firmware" : '/<td align=left class=config_module valign=top><font size=-2 color=#aaaaaa>Serial #[A-Z]+-[A-Z]+-[\d]+<br>Firmware v([\d\.]+) <font color=#ffffff>/ },
		]

