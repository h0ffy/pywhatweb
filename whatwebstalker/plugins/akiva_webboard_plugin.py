import plugins
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Pluginakiva_webboard_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        try:
            logger.info("Starting Akiva Webboard Plugin")
            self.rules = [
                { "text" : "<!-- --- AKIVA COPYRIGHT NOTICE --- -->" },
                { "text" : "<!-- Under the terms of the WebBoard License Agreement -->" },
                { "text" : "<!-- wbmain 8/22/2005 11:11AM -->" },
                { "text" : "<img src=\"images/branding-bottom.gif\" width=\"46\" height=\"44\" alt=\"Powered by WebBoard\">" },
                { "version" : "/<td class=\"botBrandingLeft\"  nowrap >Powered by <a href=\"http:\/\/get\.webboard\.com\?pid=WB80&sid=9999999999999\" target=\"_blank\" class=\"topicsSmallLink\">WebBoard ([\d])<\/a><br>&copy;20[\d]{2} Akiva Corporation/" },
            ]
            logger.info("Rules returned: %s", self.rules)
            return self.rules
        except Exception as e:
            logger.error("Error in Akiva Webboard Plugin: %s", e)
            return []
