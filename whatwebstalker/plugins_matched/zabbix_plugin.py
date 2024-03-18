import sys
import os
			
class Pluginzabbix_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<script type="text\/javascript" src="jsLoader\.php\?ver=([^\s&]+)&lang=en_[a-zA-Z]{2}"><\/script>/" },
			{ "version" : "/<td class="page_footer_l">[\s]*<a class="highlight" href="http:\/\/www\.zabbix\.com">Zabbix&nbsp;([^\s&]+)&nbsp;Copyright 2001-20[\d]{2} by&nbsp;SIA Zabbix<\/a><\/td>/" },
			{ "version" : "/<a class="highlight" href="http:\/\/www\.zabbix\.com">Zabbix ([^\s]+) Copyright 2001-20[\d]{2} by Zabbix SIA<\/a>/" },
			{ "version" : "/<a href="http:\/\/www\.zabbix\.com" class="highlight">ZABBIX ([^\s<]+)<\/a>&nbsp;Copyright 2001-20[\d]{2} by <a href="http:\/\/www\.zabbix\.com" class="highlight">SIA Zabbix<\/a>/" },
		]
		return(self.rules)

