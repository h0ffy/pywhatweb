import plugins
			
class Plugingroup_office_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[set-cookie]", "regexp" : "/groupoffice=[^;]+;/" },
			{ "version" : "/GO\.settings=\{[^\}]+"theme":"[^"]+","product_name":"Group-Office","product_version":"([^"^\s]+)","host":"/" },
			{ "md5" : "6cbe55dd826fe9e2e4306d5a5672382f", "url" : "themes/Default/images/favicon.ico" },
			{ "text" : "<!-- include everything after the loading indicator -->" },
			{ "text" : "<meta name="description" content="Take your office online. Share projects", "calendars", "files and e-mail online with co-workers and clients. Easy to use and fully customizable", "Group-Office takes online colaboration to the next level." />." },
			{ "text" : "<a style="color: white;" target="_blank" href="http://www.group-office.com">powered by Group-Office</a>" },
			{ "text" : "Powered by Group-Office: <a target="_blank" class="normal-link" href="http://www.group-office.com">http://www.group-office.com</a>" },
			{ "text" : "alert('The Group-Office javascripts were not loaded. Check the host property in config.php and see if the file_storage_path folder and it\\'s contents are writable');" },
			{ "text" : "alert('Could not load the application javascripts. Check the \"host\" property in config.php and see if the \"file_storage_path\" folder and it\\'s contents are writable');" },
		]
			return(self.rules)
