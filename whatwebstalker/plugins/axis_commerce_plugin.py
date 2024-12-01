```python
import plugins

class Pluginaxis_commerce_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "version" : r'/<div class="head"><h2>Login<\/h2><p class="powered">Powered by Axis v. ([\d\.]+)<\/p><\/div>/' },
            { "text" : '<div class="head"><h2>Forgot password</h2><p class="powered">Powered by Axis</p></div>' },
            { "text" : '<title>Login to Axis administrator panel</title>' },
            { "text" : r'<p class=\"bug-report\">Report any <a href=\'http://github.com/axis/axiscommerce/issues\' onclick=\'window.open(this.href); return false;\' title=\'Report\'>Bugs or Issues</a> you\'ve found</p>' },
            { "search" : "headers[set-cookie]", "regexp" : r'/axisid=[a-z\d]{20,32};/' },
        ]
        return self.rules
```