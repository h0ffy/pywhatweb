import plugins
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Plugin1n1_hosting_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        try:
            logger.info("Starting 1n1 Hosting Plugin")
            self.rules = []
            logger.info("Rules returned: %s", self.rules)
            return self.rules
        except Exception as e:
            logger.error("Error in 1n1 Hosting Plugin: %s", e)
            return []
