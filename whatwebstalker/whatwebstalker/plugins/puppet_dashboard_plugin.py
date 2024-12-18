import plugins


class Pluginpuppet_dashboard_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"url": "/images/favicon.ico", "md5": "ba4bfe5d1deb2b4410e9eb97c5b74c9b"},
			{"certainty": "75", "text": "<title>Puppet Node Manager</title>"},
			{"version": "/<li class='' id='dashboard-version'>[\\s]+<a href="https: \/\/github\.com\/puppetlabs\/puppet-dashboard\/blob\/([^\s]+)\/CHANGELOG">/" },
			{ "string" : /<p><a href="http:\/\/puppetlabs\.com\/">&copy; Copyright (20[\d]{2}) Puppet Labs<\/a><\/p>/" },
			{ "text" : "<a href='/' style=\"background-repeat: no-repeat; text-indent: -9000px; background-image: url('/images/dashboard_logo.png'); height: 23px; width: 155px\" title='Puppet Dashboard'>Puppet Dashboard</a>" },
		]
	return(self.rules)
