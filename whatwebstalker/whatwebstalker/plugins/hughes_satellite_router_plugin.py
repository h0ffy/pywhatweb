import plugins


class Pluginhughes_satellite_router_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<frame src=/fs/dynaform/dw_logo.html scrolling=no marginheight=0 marginwidth=0 NORESIZE>"},
			{"model": "/<title>([A-Z]{0,2}[\\d]{1,5}[A-Z]?) System Control Center<\\/title>/"},
			{"url": "/fs/dynaform/welcome.html", "model": "/<ctrlCenter style="font - size: 14pt; color:  # 000000; font-weight: bold">([^\s]+) <\/ctrlCenter>/" },
			{"url": "/sys_info/",
     "version": "/<\\/td><\\/tr><tr><td><div class=text>Software Release:<\\/td><td><div class=text>([^<^\\s]+)<\\/td><\\/tr>/"},
			{"url": "/sys_info/", "string": / <\/td><\/tr><tr><td><div class=text>LAN[\d]{1,2} MAC Address:<\/td><td><div class=text>([A-F\d:]{17})<\/td><\/tr>/" },
			{ "search" : "headers[www-authenticate]", "regexp" : "/^Basic realm="HUGHES Terminal"$/" },
		]
	return(self.rules)
