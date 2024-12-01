```python
import plugins

class Pluginhivemail_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : "<title>Database Error in HiveMail&trade;</title>" },
            { "version" : r"/\\/\\/ myaccounts holds the userpics\\s+myaccounts = \'[^\']*\';\\s+recaptcha_global = '[^"]+';\\s+hiveversion = 'v([^"]+)';/" },
            { "text" : '<input type="text" class="validate[ajax[ajaxUserCall]] input" name="answer" id="answer" />' },
            { "version" : r'/<meta name="product" content="Hivemail v([^"]+)">/' },
            { "search" : "headers[set-cookie]", "regexp" : r"/hivesession=/" },
        ]
        return self.rules
```