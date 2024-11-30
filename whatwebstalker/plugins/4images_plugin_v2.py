import plugins
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Plugin4images_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        try:
            logger.info("Starting 4images Plugin")
            self.rules = [
                { "regexp" : "/Copyright &copy; 2002-[0-9]{4} <a href=\"http:\/\/www.4homepages.de[\>]*>4homepages.de<\/a>/" },
                { "version" : "/Powered by <b>4images<\/b> ([\d\.]+)/" },
            ]
            logger.info("Rules returned: %s", self.rules)
            return self.rules
        except Exception as e:
            logger.error("Error in 4images Plugin: %s", e)
            return []
