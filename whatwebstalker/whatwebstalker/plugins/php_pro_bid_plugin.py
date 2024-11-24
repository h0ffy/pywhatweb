import plugins


class Pluginphp_pro_bid_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"version": "/            <div class="version">Current Version:[\r\n]+               ([\\d\\.]{1,5})            <\\/div>[\r\n]+/"},
			{"regexp": "/<td colspan="2" bgcolor="  # [^"]{3,6}" style="color: #ffffff; font-weight: bold;">PLEASE LOGIN TO THE ADMIN AREA<\/td>/" },
		]
	return (self.rules)
