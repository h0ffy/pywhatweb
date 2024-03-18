import plugins
			
class Pluginhuawei_firewall_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!--Modify by wangxiangguang 2006-9-29 for BYDD15857 Begin -->" },
			{ "text" : "<!--Modify by wangxiangguang 2006-9-29 for BYDD15857 End -->" },
			{ "text" : "<input type="text" onpaste="checkPaste(this,\'012\')" name="username" id="username" maxlength=" },
			{ "string" : /<div align="center">Copyright \(c\) Huawei Technologies Co\.", "Ltd\. 2005-(20[\d]{2})\. All rights reserved\. <\/div>/" },
			{ "string" : /<div align="center">Copyright \(c\) 2005-(20[\d]{2}) Huawei Technologies Co\.", "Ltd\.<\/div><\/td>/" },
			{ "search" : "headers[server]", "version" : "/^Eudemon Server ([^\s]+)$/", "model" : "Eudemon" },
		]
		return(self.rules)
