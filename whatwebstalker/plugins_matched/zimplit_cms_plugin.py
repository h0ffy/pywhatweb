import sys
import os
			
class Pluginzimplit_cms_plugin:
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script[^>]+src="http:\/\/(client\.zimplit|www\.zimplit|zimplit)\.(org|com)\/(users\/publicUser|editor)\/(jquery|ZimgZoomer|ZZMenu)\.js"[^>]*><\/script>/i },
			{ "version" : "/<script[^>]+src="http:\/\/(client\.zimplit|www\.zimplit|zimplit)\.(org|com)\/users\/publicUser_v([\d\._]+)\/(jquery|ZimgZoomer|ZZMenu)\.js"[^>]*><\/script>/i", "offset" : "2 },
			{ "text" : "<!-- YOU ARE ONLY ALLOWED TO HIDE", "DELETE OR MODIFY "POWERED BY ZIMPLIT CMS" LINK", "IF THE DOMAIN HAS BEEN REGISTERED WITH A COMMERCIAL LICENSE AT WWW.ZIMPLIT.ORG -->" },
			{ "text" : "<!-- Please don't delete this. You can use this template for free and this is the only way that you can say thanks to me -->" },
			{ "regexp" : "/<a[^>]+href="http:\/\/(www\.)?zimplit\.org\/?"[^>]*>Powered(&nbsp;| )by(&nbsp;| )Zimplit(&nbsp;| )CMS<\/a>/i },
			{ "regexp" : "/Powered(&nbsp;| )by(&nbsp;| )<A[^>]+href="http:\/\/(www\.)?zimplit\.org\/?"[^>]*>Zimplit(&nbsp;| )CMS<\/A>/i },
		]
		return(self.rules)

