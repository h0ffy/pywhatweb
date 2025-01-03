import plugins


class Pluginlevel1_router_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"model": "/<TITLE>(WBR-[^\\s]+) Wireless Broadband NAT Router Web-Console<\\/TITLE>/"},
			{"url": "/status.htm", "string": / <!--TR > <TD > MAC Address <\/TD><TD ALIGN=CENTER COLSPAN=2>([A-F\d\-]{17})<\/TD><\/TR-->/" },
			{ "url" : "/bg_logo1.jpg", "md5" : "b78c9744264dadba05ba0d00d62a97b6" },
			{ "certainty" : "25", "text" : "<!---CAS:0003--><HTML>" },
		]
	return(self.rules)
