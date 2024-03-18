import sys
import os
			
class docebolms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Powered by <a href="http://www.docebo.com/?versions" onclick="window.open(this.href); return false;">Docebo <sup>&reg;</sup></a>' }
			{ "regexp" : '/<div class="powered"><a href="http:\/\/www.docebo.com\/\?[a-z]+" target="_blank" alt="Powered by Docebo ." title="Powered by Docebo .">Powered by Docebo .<\/a><\/div>/ }
			{ "certainty" : '25", "version" : '/<title>DoceboCore ([\d\.]+)<\/title>/ }
			{ "version" : '/Powered by Docebo <sup>&reg;<\/sup> (Community|Enterprise) Edition/ }
			{ "version" : '/Powered by <a href="http:\/\/www\.docebo\.com\/\?versions" onclick="window\.open\(this\.href\); return false;">Docebo <sup>&reg;<\/sup> (Community|Enterprise) Edition<\/a>/ }
			{ "text" : 'lang_setup.setBody("<ul class=\"link_list_inline\" id=\"language_selection\"><li><a class=\"lang-sprite lang_' }
		]

