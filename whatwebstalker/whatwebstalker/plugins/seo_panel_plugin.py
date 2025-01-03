import plugins


class Pluginseo_panel_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<title>Seo Panel: Login section</title>"},
            {"text": "var wantproceed = 'Do you really want to proceed?';"},
            {"text": "var wantproceed = 'Wollen Sie wirklich fortfahren?';"},
            {"text": "<p class='note error'><p style='color:red'>You don't have permission to access this page!</p></p>"},
            {"certainty": "75", "text": "<meta name="description" content="Login to Seo Panel and utilise seo tools and plugins to increase the perfomance of your site." />"},
            {"certainty": "75", "text": "<p class="note error">JavaScript is turned off in your web browser. Turn it on to take full advantage of this site", "then refresh the page.</p>"},
        ]
        return (self.rules)
