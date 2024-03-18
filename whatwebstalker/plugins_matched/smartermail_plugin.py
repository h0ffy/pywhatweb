import plugins
			
class Pluginsmartermail_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "string" : /<a href='http:\/\/www.smartertools.com\/smartermail\/mail-server-software.aspx' target='_blank'>SmarterMail (Enterprise|Professional|Free|FREE) ([\d\.]+)<\/a>( |&nbsp;)\|( |&nbsp;)<a href='http:\/\/www.smartertools.com\/smartermail\/mail-server-software.aspx' target='_blank'>(Windows Mail Server|Email Server Software|Mail Server Software)<\/a>/" },
			{ "version" : "/<a href='http:\/\/www.smartertools.com\/smartermail\/mail-server-software.aspx' target='_blank'>SmarterMail (Enterprise|Professional|Free|FREE) ([\d\.]+)<\/a>( |&nbsp;)\|( |&nbsp;)<a href='http:\/\/www.smartertools.com\/smartermail\/mail-server-software.aspx' target='_blank'>(Windows Mail Server|Email Server Software|Mail Server Software)<\/a>/", "offset" : "1 },
			{ "string" : /										<td class="?bar1inner"?>SmarterMail (Enterprise|Professional|Free|FREE) Edition ([\d\.]+)<\/td>/" },
			{ "version" : "/										<td class="?bar1inner"?>SmarterMail (Enterprise|Professional|Free|FREE) Edition ([\d\.]+)<\/td>/", "offset" : "1 },
			{ "text" : "<title>Login - SmarterMail</title>" },
		]
	return(self.rules)
