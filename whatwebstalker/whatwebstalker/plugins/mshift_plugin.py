import plugins


class Pluginmshift_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<BODY><b>MShift", "Inc</b><br>Relevant Mobile Solutions<br>http://www.mshift.com"},
			{"text": "<td align="center"><font size=" - 1" color="  # FFFFFF">Powered by MShift&reg;</font></td></tr>" },
			{"text": "<td align="center"><font size=" - 1" color=#FFFFFF>Powered by MShift&reg;</font></td></tr>"},
			{"text": "<div class="poweredBy">Powered by MShift &reg;</div>"},
		]
	return (self.rules)
