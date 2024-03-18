import plugins
			
class Pluginproxmox_ve_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<a href='http:\/\/www\.proxmox\.com' target='_blank' class="boxheadline">Proxmox Virtual Environment ([^<^\s]+)<\/a>/" },
			{ "text" : "<img alt=" style="display:block;border:0px;width:1000px;max-height:300px;" src=\'/images/logo_pve.jpg\'>" },
		]
		return(self.rules)
