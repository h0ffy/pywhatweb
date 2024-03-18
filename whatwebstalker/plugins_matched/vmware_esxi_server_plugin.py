import plugins
			
class Pluginvmware_esxi_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<script type="text/javascript">document.write("<title>" + ID_EESX_Welcome + "</title>");</script>" },
			{ "text" : "<meta name="description" content="VMware ESXi Server is virtual infrastructure software for partitioning", "consolidating", "and managing systems in mission-critical environments. VMware ESXi Server provides a highly scalable virtual machine platform with advanced resource management capabilities", "which can be managed by VMware vCenter Server.">" },
			{ "text" : "<h1><script type="text/javascript">document.write(ID_EESXServer3);</script></h1>" },
		]
		return(self.rules)
