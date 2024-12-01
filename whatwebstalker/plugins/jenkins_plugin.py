```python
import plugins

class Pluginjenkins_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : r"/<script>var isRunAsTest=false; var rootURL=\"[^\"]*\";<\/script>/" },
            { "version" : r"/<\/span><a href=\"http:\/\/jenkins\-ci\.org\/\">Jenkins ver\. ([^<]+)<\/a>/" },
            { "search" : "headers[x-hudson-theme]", "regexp" : r"/^.*$/" },
            { "search" : "headers[x-instance-identity]", "regexp" : r"/^.*$/" },
            { "search" : "headers[x-hudson-cli-port]", "regexp" : r"/^.*$/" },
            { "search" : "headers[x-jenkins]", "version" : r"/^(.+)$/" },
            { "search" : "headers[x-hudson]", "regexp" : r"/^.*$/" },
            { "search" : "headers[x-jenkins-cli-port]", "regexp" : r"/^.*$/" },
            { "search" : "headers[x-ssh-endpoint]", "regexp" : r"/^.*$/" },
        ]
        return self.rules
```