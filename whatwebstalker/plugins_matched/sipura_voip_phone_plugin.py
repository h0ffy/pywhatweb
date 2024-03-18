import plugins
			
class Pluginsipura_voip_phone_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<form action="bsipura.spa" method="POST">" },
			{ "text" : "<img width="100%" src="/spabanner.jpg" border="0" alt="Sipura Technology Inc">" },
			{ "model" : "/<tr bgcolor="#dcdcdc"><td>Product Name:<td><font color="darkblue">([^<]+)<\/font><td>Serial Number:<td>/" },
			{ "version" : "/<tr bgcolor="#d3d3d3"><td>Software Version:<td><font color="darkblue">([^<]+)<\/font><td>Hardware Version:<td><font color="darkblue">[^<]+<\/font>/" },
			{ "firmware" : "/<tr bgcolor="#d3d3d3"><td>Software Version:<td><font color="darkblue">[^<]+<\/font><td>Hardware Version:<td><font color="darkblue">([^<]+)<\/font>/" },
			{ "string" : /<tr bgcolor="#dcdcdc"><td>MAC Address:<td><font color="darkblue">([A-F\d]{12})<\/font><td>Client Certificate:<td>/" },
			{ "module" : /<\/font><a href="\/calllog\.htm" target=_calllog_[\d]+><font class=swalft>(Call History)<\/font><\/a><\/p><\/div>/" },
			{ "url" : "/pdir.htm", "string" : /<td>[\d]+\.<td>&nbsp;<input class="inputc" size="40" name="[\d]+" value="(n=[^;]*;p=[\d]+)" maxlength=[\d]+>/" },
		]
	return(self.rules)
