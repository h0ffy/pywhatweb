```python
import plugins

class Pluginbarracuda_backup_server_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : '<div id="logo-wrapper"><a id="logo" href="http://www.barracudanetworks.com/ns/?a=backup_localui">Barracuda Networks</a></div>' },
            { "url" : "/auth/signin/", "model" : r'/<div id="label">Backup Server ([^\s^<]+)<\/div>/' },
            { "url" : "/include/cui/images/favicon.ico", "md5" : "de2b6edbf7930f5dd0ffe0528b2bbcf4" },
            { "search" : "headers[set-cookie]", "regexp" : "/BACKUP_LOCAL_LOCALE=/" },
        ]
        return self.rules
```