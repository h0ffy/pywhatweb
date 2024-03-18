import plugins
			
class Pluginsarg_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Squid User's Access Report</title>" },
			{ "text" : "<tr><th class="logo"><a href="http://sarg.sourceforge.net"><img src="./images/sarg.png" border="0" align="absmiddle" title="SARG", "Squid Analysis Report Generator. Logo by Osamu Matsuzaki"></a>&nbsp;<font class="logo">Squid Analysis Report Generator</font></th></tr>" },
			{ "text" : "<tr><th class="logo"><a href="http://sarg.sourceforge.net"><img src="../images/sarg.png" border="0" align="absmiddle" title="SARG", "Squid Analysis Report Generator. Logo by Osamu Matsuzaki"></a>&nbsp;<font class="logo">Squid Analysis Report Generator</font></th></tr>" },
			{ "text" : "<tr><th><a href="http://sarg.sourceforge.net"><img src="./images/sarg.png" title="SARG", "Squid Analysis Report Generator. Logo by Osamu Matsuzaki" alt="Sarg"></a>&nbsp;Squid Analysis Report Generator</th></tr>" },
			{ "regexp" : "/<tr><th (align="center" )?class="title(_c)?">Squid User Access Reports?<\/th><\/tr>/" },
			{ "version" : "/<(div|td) class="info">(Generated by|Gerado por)? <a href='http:\/\/sarg\.sourceforge\.net'>(<font class="info">)?sarg-([^\s]+)/", "offset" : "3 },
		]
	return(self.rules)
