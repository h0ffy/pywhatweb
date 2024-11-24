import plugins


class Plugintradingeye_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"url": "/favicon.ico", "md5": "0ec12e5820517d3b62e56b9a8f1ee5bc"},
			{"url": "/_assets/img/site/favicon.ico",
     "md5": "0ec12e5820517d3b62e56b9a8f1ee5bc"},
			{"text": "<p id="credits"><a href="http: // www.tradingeye.com / ">powered by Tradingeye</a></p>"},
			{"text": "<meta name="author" content="dpivision.com Ltd" />"},
			{"certainty": "25", "text": "<p id="breadcrumbs">You are here:"},
			{"certainty": "25", "text": "</div><!-- end body/inner -->"},
			{"text": "<p id="skip">[<a href="  # main">skip to main content</a>]</p>" },
			{"version": "/<title>Tradingeye v([^\\s]+) :: Online Admin<\\/title>/"},
			{"text": "<th class="login_bg" colspan="2">Tradingeye Login</th>"},
		]
	return (self.rules)
