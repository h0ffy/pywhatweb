import plugins
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Plugin6kbbs_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        try:
            logger.info("Starting 6KBBS Plugin")
            self.rules = [
                { "version" : "/<meta name=\"generator\" content=\"6KBBS v([^\"^>]+)\" \/>/" },
                { "regexp" : "/<meta name=\"copyright\" content=\"2003-20[\d]{2} 6KBBS\" \/>/" },
                { "text" : "<meta name=\"author\" content=\"www.6kbbs.com\" />" },
                { "version" : "/Powered by <a href=\"http:\/\/www\.6kbbs\.com\" target=\"_blank\">6kbbs V([^<^\s]+)<\/a> &copy; 2003-20[\d]{2}/" },
            ]
            logger.info("Rules returned: %s", self.rules)
            return self.rules
        except Exception as e:
            logger.error("Error in 6KBBS Plugin: %s", e)
            return []
