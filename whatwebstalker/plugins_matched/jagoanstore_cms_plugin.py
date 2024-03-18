import sys
import os
			
class jagoanstore_cms_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'CMS <a style="color:#fff;font-size:11px;" href="http://www.jagoanstore.com/" target="_blank">Toko Online</a> by <a href="http://www.jagoanstore.com/" target="_blank"><img src="http://www.jagoanstore.com/jagstorecom-lil.png" border=0 align="absmiddle" /></a></div>\');' },
			{ "string" : /<div class="copy">Copyright (20[\d]{2}) Toko Online ini menggunakan JagoanStore CMS dari JagoanWeb Indonesia<\/div>/ },
		]

