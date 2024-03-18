import plugins
			
class Pluginzend_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "name" : "GHDB: "Powered by Zend Framework"',"certainty" : "75,"ghdb" : "Powered by Zend Framework"'},
			{ "string" : "PoweredBy Image',"url" : "images/PoweredBy_ZF.gif',"md5" : "eecf384879cde19f8f7f80c768c12295'},
			{ "string" : "Zend Logo Small',"url" : "images/logo_small.gif',"md5" : "0f76017aa12a3dcb9cabbff26e37ff5c'},
			{ "string" : "Footer Link',"text" : " alt="Powered by Zend Framework!" />'},
			{ "string" : "Null Controller',"url" : randstr(),"text" : "controllers/images/PoweredBy_ZF.gif" alt="Powerd by Zend Framework!" />'},
			{ "string" : "Null Controller',"url" : randstr(),"regexp" : "/<h1>Controller\/action not found!<\/h1>(\r\n|\n)<p>Controller\/action not found!<\/p>},
			{ "string" : "Zend_Controller_Dispatcher_Exception',"url" : randstr(),"text" : "( ! )</span> Zend_Controller_Dispatcher_Exception: Invalid controller specified (application) in'},
			{ "string" : "Zend_Controller_Dispatcher_Exception',"url" : randstr(),"text" : "<b>Fatal error</b>:  Uncaught exception 'Zend_Controller_Dispatcher_Exception"},
			{ "string" : "Zend_Controller_Router_Exception',"url" : randstr(),"text" : "Uncaught exception 'Zend_Controller_Router_Exception' with message 'No route matched the request'"},
			{ "string" : "Zend_Controller_Router_Exception',"url" : randstr(),"text" : "/Zend/Controller/Router/Rewrite.php</b> on line <b>"},
			{ "version" : "/<meta name="generator" content="Zend.com CMS ([\d\.]+)"/" },
			{ "text" : "<meta name="vendor" content="Zend Technologies'},
			{ "regexp" : "/Zend Framework/", "search" : "headers[x-powered-by]" },
			{ "version" : "/Zend Framework ([a-zA-Z0-9\.\/\+\-\(\)]+)/", "string" : "Framework", "search" : "headers[x-powered-by]" },
			{ "version" : "/Zend Core\/([a-zA-Z0-9\.\/\+\-\(\)]+)/", "string" : "Core", "search" : "headers[x-powered-by]" },
			{ "regexp" : "/^Zend /", "search" : "headers[server]" },
			{ "version" : "/Zend Core\/([a-zA-Z0-9\.\/\+\-\(\)]+)/", "string" : "Core", "search" : "headers[server]" },
		]
		return(self.rules)
