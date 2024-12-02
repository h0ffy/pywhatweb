import plugins
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Plugin3dcart_plugin(plugins.Base):
    def __init__(self):
        pass

    def start(self):
        try:
            logger.info("Starting 3dcart Plugin")
            self.rules = [
                { "text" : "<!--START: 3dcart stats-->" },
                { "text" : "<!--END: 3dcart stats-->" },
                { "search" : "headers[set-cookie]", "regexp" : "/3dvisit/" },
                { "search" : "headers[set-cookie]", "regexp" : "/^affiliate\s/", "name" : "affiliate cookie", "certainty" : "25" },
            ]
            logger.info("Rules returned: %s", self.rules)
            return self.rules
        except Exception as e:
            logger.error("Error in 3dcart Plugin: %s", e)
            return []
