import plugins
			
class Pluginsony_projector_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "/", "text" : "<BODY onLoad="setWindowTitle();showIndex();">" },
			{ "url" : "/", "text" : "<form Action="/Forms/index_1" method="post"  NAME="form1">" },
			{ "url" : "/", "text" : "<script type="text/javascript" src="sonylogoJS.js"></script>" },
			{ "url" : "/index_J.htm", "text" : "<frame src="index_bg.htm" NAME="RIGHT" marginwidth="0" marginheight="0" scrolling="no" noresize>" },
			{ "url" : "/index_E.htm", "text" : "<frame src="index_bg.htm" NAME="RIGHT" marginwidth="0" marginheight="0" scrolling="no" noresize>" },
			{ "text" : "<TR><TD COLSPAN="2"><script type="text/javascript">sonylogo();</script></TD>" },
			{ "url" : "/info_data.htm", "model" : "/^var info_pj_value = \[[\s]+'([^\s^']+)','[\d]+','[^']{0,256}'\];/" },
			{ "url" : "/info_data.htm", "version" : "/^var info_other_value = \[[\s]+' ?([^\s^']+)'/" },
		]
	return(self.rules)

