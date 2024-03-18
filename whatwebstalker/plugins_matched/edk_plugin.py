import plugins
			
class Pluginedk_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "inurl:alliance_detail | inurl:pilot_detail | inurl:corp_detail" },
			{ "text" : "<div class="menu-caption">Kills &amp; losses</div>" },
			{ "text" : "<tr class="kb-table-row-even">" },
			{ "text" : "&amp;scl_id=39">Industrial Command Ship</a></b></td>" },
			{ "text" : "<!-- /killlistable.tpl -->" },
		]
	return(self.rules)
