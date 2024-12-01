import plugins

class Pluginaruba_device_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "string" : r"</noscript>\s+<div id=\"system-info\">\s+<ul>\s+<li>System Name : ([^<]+)</li>" },
            { "regexp" : r"<img src=\"/images/arubalogo\.gif\" width=\"200\" height=\"51\"\s+alt=\"Aruba( Wireless)? Networks\" title=\"Aruba( Wireless)? Networks\"/>" },
            { "text" : "<form id=\"login-form\" method=\"post\" autocomplete=\"off\" action=\"/screens/wms/wms.login\">" },
            { "url" : "/images/arubalogo.gif", "md5" : "0edcf58b30fccecb053a6e7d3e9846ad" },
            { "url" : "/images/arubalogo.gif", "md5" : "3dcb2475aa28fc1d685f863e79cc837f" },
        ]
        return self.rules