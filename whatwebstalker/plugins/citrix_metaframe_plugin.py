import plugins

class Plugincitrix_metaframe_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "regexp" : r"/Copyright \(c\) [\d]+ - [\d]+ Citrix Systems, Inc. All Rights Reserved./" },
            { "text" : 'window.location="/Citrix/MetaFrame";' },
            { "text" : "<title>MetaFrame Presentation Server Log In</title>" },
        ]
        return self.rules