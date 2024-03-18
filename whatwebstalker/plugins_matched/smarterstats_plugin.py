import sys
import os
			
class smarterstats_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "string" : /<a href='http:\/\/www.smartertools.com\/smarterstats\/web-analytics-seo-software.aspx' target='_blank'>SmarterStats (Enterprise|Professional|Free) ([\d\.]+)<\/a>( |&nbsp;)\|( |&nbsp;)<a href='http:\/\/www.smartertools.com\/smarterstats\/web-analytics-seo-software.aspx' target='_blank'>Web Log Analytics( & SEO Software)?<\/a>/ }
			{ "version" : '/<a href='http:\/\/www.smartertools.com\/smarterstats\/web-analytics-seo-software.aspx' target='_blank'>SmarterStats (Enterprise|Professional|Free) ([\d\.]+)<\/a>( |&nbsp;)\|( |&nbsp;)<a href='http:\/\/www.smartertools.com\/smarterstats\/web-analytics-seo-software.aspx' target='_blank'>Web Log Analytics( & SEO Software)?<\/a>/", "offset" : '1 }
			{ "string" : /<a href='http:\/\/www.smartertools.com\/Products\/SmarterStats\/Overview.aspx' target='_blank'>SmarterStats (Enterprise|Professional|Free) ([\d\.]+)<\/a>&nbsp;\|&nbsp;<a href='http:\/\/www.smartertools.com\/' target='_blank'>Windows Web Analytics<\/a>/ }
			{ "version" : '/<a href='http:\/\/www.smartertools.com\/Products\/SmarterStats\/Overview.aspx' target='_blank'>SmarterStats (Enterprise|Professional|Free) ([\d\.]+)<\/a>&nbsp;\|&nbsp;<a href='http:\/\/www.smartertools.com\/' target='_blank'>Windows Web Analytics<\/a>/", "offset" : '1 }
			{ "string" : /										<td class=bar1inner>SmarterStats (Enterprise|Professional|Free|FREE) Edition ([\d\.]+)<\/td>/ }
			{ "version" : '/										<td class=bar1inner>SmarterStats (Enterprise|Professional|Free|FREE) Edition ([\d\.]+)<\/td>/", "offset" : '1 }
			{ "text" : '<title>Login - SmarterStats</title>" }
		]

