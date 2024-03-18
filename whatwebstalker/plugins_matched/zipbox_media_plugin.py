import sys
import os
			
class Pluginzipbox_media_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "POWERED BY ZIPBOX MEDIA" inurl:"album.php"" },
			{ "text" : "<a href="http://www.zipboxmedia.com" class="zbm"><img src="/images/zb_rotate_ft.gif" alt="Powered By ZIPBOX Media" border="0" /></a>" },
			{ "regexp" : "/<a href="https:\/\/secure.zipboxmedia.com\/signup\/\?referral=[\d]+" class="zbm" title="get your own ZIPBOX Media Store"><img src="\/images\/get_zipbox.gif" alt="Get A ZIPBOX Media Store" border="0" \/><\/a>/" },
			{ "regexp" : "/<h3 style="padding-top:2px; margin:0px; display:none"><a href="javascript:loadMoreMessages\([\d]+\)" id="load_more_messages">Load more messages<\/a><\/h3>/" },
		]

