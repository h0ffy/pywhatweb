import sys
import os
			
class flax_article_manager_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '/images/flaxweb_newsletter_bg.gif" bgcolor="#FFFFFF" valign="top"> ' }
			{ "text" : '<b><a href="http://www.flaxweb.com/products/articles"><font color="#666666">Article ' }
			{ "text" : '<title>Flax Article CMS Administration Panel</title>' }
			{ "text" : 'recent updates for Flax Article Manager</font></b></a></div>' }
			{ "text" : '<td width=67%><font color=#FFFFFF><a href=admin.php class=htext>Flax ' }
			{ "text" : '<td><a href="http://www.flaxweb.com/products/articles">For more details about Flax article manager (CMS) please click ' }
			{ "version" : '/[\s]+Copyright [0-9]{4} &copy; Flax Article Manager v([\d\.]+)<\/div>/ }
		]

