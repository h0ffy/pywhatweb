import plugins


class Pluginmootools_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"regexp": "/^\\/\\/ Load your build at: http:\\/\\/mootools.net\\/core\\//"},
			{"version": "/^MooTools.More[\\s]*=[\\s]*\\{[\\s]*version:[\\s]*["']?([^\"^\']+)["']?/" },
			{ "version" : "/^var MooTools[\s]*=[\s]*\{[\s]*version:[\s]*["']?([^\"^\']+)/" },
			{ "regexp" : "/^\/\/MooTools More", "<http:\/\/mootools.net\/more>. Copyright \(c\) 2006-2008 Valerio Proietti", "<http:\/\/mad4milk.net>", "MIT Style License./" },
		]
	return(self.rules)
