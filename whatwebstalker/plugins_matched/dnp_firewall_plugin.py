import plugins
			
class Plugindnp_firewall_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Forum Gateway - Powered by DnP Firewall</title>" },
			{ "text" : "	<form name=dnp_firewall method=get action=dnp_fw.php" },
			{ "text" : "<input type=submit value=" " alt="Click to continue to your destination" style="background-image:url(default.jpg); height:444px; width:635px; cursor:pointer; border-width:0px;"> '},
			{ "version" : "/<\/html><center><div style='border-top:1px solid #666666; height:20px;  padding:1px; background: #333333 none repeat scroll 0% 0%; position: fixed; bottom: 0pt; right: 0pt; left: 0pt; width: 100%; z-index: 100; text-align: center; font-size:12pt;'><font size=1 style='color:gray;font-weight:bold;'><center>Protected by <a href='http:\/\/www.silveryhat.com\/delynie\/f142' title='Firewall Gateway by DnP Network&trade;' style='color:gray'>DnP Firewall<\/a> v([\d\.]{1,5}) &copy; 2005-[\d]{4}<\/font><\/div><\/center>/" },
		]
		return(self.rules)
