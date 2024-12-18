import plugins


class Pluginionize_cms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"version": "/<div id="version">([\\d\\.]+) - Ionize CMS - MIT licence<\\/div>/"},
            {"text": "<div id="loginWindow" class=" clearfix">"},
            {"text": "<div id="content" class="content" onKeyPress="javascript: doSubmit(event)
             ">"},
            {"status": "404", "text": "<p class="note">view : <b>default/article</b></p>"},
            {"status": "404", "text": "<p class="article - date">07.09.2010</p>"},
            {"text": "<meta name="description" content="HandMade", "an Ionize theme" />"},
            {"regexp": "/<!--[\\s]+Displays the Google code defined in Ionize's Advanced settings panel[\\s]+-->/"},
        ]
        return (self.rules)
