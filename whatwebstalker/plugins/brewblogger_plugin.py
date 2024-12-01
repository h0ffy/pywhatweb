```python
import plugins

class Pluginbrewblogger_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r'/<div id="footer">Content &copy; 2011 [^\n]+ &mdash; BrewBlogger ([^\s]+) (Personal Edition|Club Edition) developed by <a href="http://www\.zkdigital\.com" target="_blank">zkdigital\.com<\/a>/' },
            { "string" : r'/<div id="footer">Content &copy; 2011 [^\n]+ &mdash; BrewBlogger ([^\s]+) (Personal Edition|Club Edition) developed by <a href="http://www\.zkdigital\.com" target="_blank">zkdigital\.com<\/a>/', "offset" : "1" },
        ]
        return self.rules
```