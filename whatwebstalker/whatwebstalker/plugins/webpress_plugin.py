import plugins


class Pluginwebpress_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "Powered By <a href="http: // www.ecomenterprises.com" target="_blank" class="small_text">WebPress</a><SUP><FONT SIZE=" - 5">TM</FONT></SUP></td>"},
			{"text": "Powered by <a href="http: // goywp.com" id="webpresslink">WebPress</a><br></p></td>"},
			{"text": "Powered by </font><font size="1" color="  # 000000" face="Arial">YWP</font>" },
			{"version": "/<!-- Powered by YWP ([\\d\\.]+) -->/"},
			{"version": "/<meta name="generator" content="YWP([\d\.]+)">/" },
		]
	return(self.rules)
