import plugins
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Plugin3com_nbx_plugin(plugins.Base):
    def __init__(self):
        pass
        
    def start(self):
        try:
            logger.info("Starting 3Com NBX Plugin")
            self.rules = [
                { "text" : "<head><title>NBX NetSet</title>" },
                { "text" : "<HEAD><TITLE>NBX NetSet</TITLE>" },
                { "text" : "3Com Corporation or its subsidiaries" },
                { "text" : "<!-- Gregory Brucato  4/22/98  NBX Corporation -->" },
                { "version" : "/<META HTTP-EQUIV=\"sysObjectID\" CONTENT=\"([\d\.]{20,30})\">/" },
                { "text" : "<span class=\"splashTitleIPTelephony\">&nbsp;3Com<SUP><span class=\"splashTitleNBXReg\">&reg;</span></SUP> IP Telephony Solution</span>" },
                { "firmware" : "/<td colspan=\"3\" class=\"splashVersionCol\" valign='bottom'>[\s]+Version:&nbsp;([^<]+)<br \/>[\s]+Created:&nbsp;/" },
                { "firmware" : "/<TABLE BORDER=\"0\" CELLPADDING=\"0\" CELLSPACING=\"0\"><TR><TD ALIGN=\"right\" WIDTH=\"130\" HEIGHT=\"75\">[\s]+Version:(&nbsp;)?([^<]+)<BR>/", "offset" : "1" },
                { "model" : "/<span class=\"splashTitleNBX\">NBX<SUP><span class=\"splashTitleNBXReg\">&reg;<\/span><\/SUP><\/span>[\s]+<span class=\"splashTitlePlatform\">(&nbsp;)?([^<]+)<\/span>/", "offset" : "1" }
            ]  
            
            # New rules for additional 3Com devices
            self.rules.extend([
                { "text" : "<head><title>3Com Device</title>" },
                { "text" : "<HEAD><TITLE>3Com Device</TITLE>" },
                { "text" : "3Com Corporation Device" },
                { "firmware" : "/<td class=\"version\">Version: ([^<]+)<\/td>/" },
                { "model" : "/<span class=\"deviceModel\">Model: ([^<]+)<\/span>/" }
            ])
            
            logger.info("Rules returned: %s", self.rules)
            return self.rules
        except Exception as e:
            logger.error("Error in 3Com NBX Plugin: %s", e)
            return []
