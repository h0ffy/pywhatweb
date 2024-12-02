import plugins
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Pluginairtiesrouter_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        try:
            logger.info("Starting Airties Router Plugin")
            self.rules = [
                { "version" : "/<title>Airties ([^<]+)<" }
            ]
            logger.info("Rules returned: %s", self.rules)
            return self.rules
        except Exception as e:
            logger.error("Error in Airties Router Plugin: %s", e)
            return []
