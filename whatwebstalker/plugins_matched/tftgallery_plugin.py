import sys
import os
			
class tftgallery_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Select an album: <select name="album" onchange="javascript:document.tftnavi.submit();"><option></option>' }
			{ "text" : '<title>TFTgallery administration</title><link rel='stylesheet' type='text/css' href" }
			{ "text" : '<div class="login_text"><br /><a href="../index.php">back to the gallery</a></div>' }
			{ "regexp" : '/<td class='footer_right'><a href='http:\/\/www.tftgallery.org\/' target='_blank'><img src="[^"]*images\/TFTgallery.png" alt="TFTgallery" border="0" \/><\/a><\/td>/ }
			{ "version" : '/<meta name="generator" content="TFTgallery ([\d\.]{1,5}) http:\/\/www.tftgallery.org\/" \/>/ }
	]

