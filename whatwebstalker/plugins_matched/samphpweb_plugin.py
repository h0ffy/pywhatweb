import sys
import os
			
class samphpweb_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "certainty" : '75,"ghdb" : 'This page was produced using SAM Broadcaster" "Copyright Spacial Audio Solutions"'}
			{ "certainty" : '75,"text" : '<meta HTTP-EQUIV="REFRESH" CONTENT="0;url=playing.html">'}
			{ "text" : '<a href="http://www.spacialaudio.com/products/sambroadcaster/" target="_blank"><img src="images/sam-bc.gif" border="0" alt="Powered by SAM Broadcaster" width="120" height="60" />'}
			{ "text" : '<a href="http://www.spacialaudio.com/products/sambroadcaster/" target="_blank"><img src="images/sam-bc.gif" width="120" height="60" border="0" alt="Powered by SAM Broadcaster">'}
			{ "text" : 'This page was produced using <a target="_blank" href="http://www.spacialaudio.com/products/sambroadcaster/">SAM Broadcaster</a>. © Copyright <a target="_blank" href="http://www.spacialaudio.com">Spacial Audio Solutions", "LLC</a>'}
			{ "text" : ' songwin = window.open("songinfo.php?songid="+songid", "songinfowin", "location=no,status=no,menubar=no,scrollbars=yes,resizeable=yes,height=400,width=650");'}
	]

