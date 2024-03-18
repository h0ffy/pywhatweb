import plugins
			
class Pluginvmware_virtualcenter_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<script type="text/javascript">document.write("<title>" + ID_VC_Welcome + "</title>");</script>" },
			{ "text" : "<meta name="description" content="VMware vSphere is virtual infrastructure software for partitioning", "consolidating and managing systems in mission-critical environments. VMware ESX Server provides a highly scalable platform with advanced resource management capabilities", "which can be managed by vSphere.">" },
			{ "url" : "/en/welcomeRes.js", "version" : "/var ID_VC_Welcome = "Welcome to VMware vSphere ([^\s^\"]+)";/" },
			{ "certainty" : "75", "text" : "<title>VMware Virtual Infrastructure Web Access</title>" },
			{ "url" : "/banner.png", "md5" : "53ea8ad28aabd281be50075c4977d31b" },
		]
		return(self.rules)

