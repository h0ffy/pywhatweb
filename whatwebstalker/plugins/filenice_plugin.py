import plugins


class Pluginfilenice_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            {"text": "<!-- please leave the word fileNice visible on the page", "it's only polite really isn't it. -->"},
            {"text": "<!-- please leave the word fileNice and the link to fileNice.com in the about", "it's only polite really isn't it. I didn't do all this work just for you to try to pass it off as your own. -->"},
            {"text": "Free open source file browser available from <a href="http: // fileNice.com" title="fileNice.com">fileNice.com</a><br />"},
            {"text": "	<meta name="generator" content="the fantabulous mechanical eviltwin code machine" />"},
        ]
        return (self.rules)
