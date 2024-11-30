import plugins
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Plugin4d_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        try:
            logger.info("Starting 4D Plugin")
            self.rules = [
                { "search" : "headers[server]", "version" : "/^4D_v[\d]{1,2}(_SQL)?\/([\d\.]+)$/", "offset" : "1" },
            ]
            logger.info("Rules returned: %s", self.rules)
            return self.rules
        except Exception as e:
            logger.error("Error in 4D Plugin: %s", e)
            return []
