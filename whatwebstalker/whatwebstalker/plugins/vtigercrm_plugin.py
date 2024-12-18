import plugins


class Pluginvtigercrm_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"name": "favicon md5", "url": "/themes/images/vtigercrm_icon.ico',"md5" : "d90cc1762bf724db71d6df86effab63c'},
			{ "name" : "favicon md5", "url" : "/include/images/vtigercrm_icon.ico',"md5" : "d90cc1762bf724db71d6df86effab63c'},
			{ "name" : "stats img", "text" : "<img src=\'http://stats.vtiger.com/stats.php?uid=" },
			{ "version" : "/<span style='color: rgb\([\d]{1,3}", "[\d]{1,3}", "[\d]{1,3}\);'>vtiger CRM ([^<]*)<\/span>},
			{ "name" : "copyright footer", "regexp" : "/&copy; 200[\d]{1}\-\d{4} <a href='http:\/\/www.vtiger.com' target='_blank'>vtiger.com<\/a>},
			{ "name" : "html body favicon", "text" : "/vtigercrm_icon.ico">'},
		]
	return(self.rules)
