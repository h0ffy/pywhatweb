```python
import plugins

class Pluginbrowsercms_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        self.rules = [
            { "text" : "<!--User is member of the following groups:  -->" },
            { "text" : '<li class="bmcms"><a href="http://www.browsercms.com/index.ww" title="BrowserCMS 2.0" target="_blank"><span>Powered by BrowserCMS 2.0</span></a></li>', "version" : "2.x" },
            { "regexp" : r'/Powered by <a href="http:\\/\\/www.browsercms.com[\\/]*"[^>]+>BrowserCMS<\\/a>/i' },
            { "regexp" : r'/<a href="http:\\/\\/www.browsercms.com[\\/]*"[^>]+title="Powered by BrowserCMS"[^>]+/' },
            { "regexp" : r'/<a href="http:\\/\\/www.browsercms.com[^>]+><img[^>]*src="\\/site\\/images[^>]+ onmouseover="this.src=\'\\/site\\/images[^>]+onmouseout="this.src=\'\\/site\\/images[^>]+alt="Powered by BrowserCMS"[^>]*><\\/a>/i' },
            { "text" : '<form method="POST" action="/portlets/login/do-login.jsp" name="security">' },
            { "regexp" : r'/<input type="hidden" name="success_uri" value="[^>]*\\/page.ww\\?name=[^>]*\\&section=[^>]*"\\/>/' },
            { "regexp" : r'/<input type="hidden" name="failure_uri" value="[^>]*\\/page.ww\\?name=[^>]*\\&section=[^>]*"\\/>/' },
            { "version" : r'/<meta name="generator" content="BrowserCMS ([^\\"]+)"/' },
        ]
        return self.rules
```