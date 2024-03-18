import plugins
			
class Pluginib_lite_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<tr class="w_r"><td class="w_n">Access code</td><td width="140" class="w_v"><input id="psw_id" type="password" maxLength="15" size="20" name="q" value="></td></tr>" },
		]
		return(self.rules)
