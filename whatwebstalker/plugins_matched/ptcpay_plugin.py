import sys
import os
			
class Pluginptcpay_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "25", "ghdb" : "powered by PTCPay"" },
			{ "text" : "<div class="left"><img src="pre/images/ic_support.png" width="23" height="23" alt=" /></div>" },
			{ "text" : "<p>Powered by <a href="http://www.ptcpay.com" target="_blank">GeN4 Security+</a>" },
			{ "version" : "/<\/div><div class="foot">GeN4 Secur(ity|e)\+ ([\d\.]{1,6})  &copy; 2009 - 20[\d]{2} <a href="http:\/\/www.ptcpay.com" target="_blank">PTCPay.Com<\/a><\/div>/", "offset" : "1 },
		]

