import plugins
			
class Pluginhesk_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<script language="Javascript" type="text\/javascript" src="(\.\.\/|\.\/)?hesk_javascript\.js"><\/script>/" },
			{ "regexp" : "/<link href="(\.\/)?hesk_style\.css" type="text\/css" rel="stylesheet"/" },
			{ "regexp" : "/<link rel="stylesheet" type="text\/css" href="(\.\/)?hesk_style\.css"/" },
			{ "text" : "<body onload="javascript:var i=new Image();i.src=\'./img/orangebtnover.gif\';var i2=new Image();i2.src=\'./img/greenbtnover.gif\';">" },
			{ "text" : "<img src="img/loading.gif" width="24" height="24" alt=" border="0" style="vertical-align:text-bottom" /> <i>Loading knowledgebase suggestions...</i>" },
			{ "text" : "<!-- START KNOWLEDGEBASE SUGGEST -->" },
			{ "text" : "<p style="text-align:center"><a href="admin/" class="smaller">Go to Administration Panel</a></p>" },
			{ "regexp" : "/<p style="text-align:center"><span class="smaller">Powered by <a href="http:\/\/www\.hesk\.com" class="smaller"( target="_blank")? title="Free Help Desk Software HESK">Help Desk Software<\/a> HESK&trade;/" },
			{ "text" : "Powered by <a href="http://www.phpjunkyard.com/free-helpdesk-software.php" class="smaller" target="_blank">Help desk software</a> HESK<sup>TM</sup></span>", "version" : "<1.0" },
			{ "version" : "/<p align="center"><font class="smaller">Powered by <a href="[^>^"]{0,256}" class="smaller" target="_blank">Help desk software Hesk<\/a> ([^\s^<]+)<\/font>/" },
		]
		return(self.rules)
