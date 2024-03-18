import sys
import os
			
class semaphore_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "ghdb" : "Powered by Semaphore" inurl:semaphoreserver.exe filetype:exe" },
			{ "text" : "<html><head><title>Semaphore server Error</title></head><body>" },
			{ "text" : "<!-- Display the "Powered by Semaphore" logo -->" },
			{ "regexp" : "/<a href="http:\/\/www.smartlogic.com\/poweredbysemaphore"><img src="[^"^>]+\/semaphore\/semaphore_small\.gif"[^>]+alt="Powered by Semaphore" title="Powered by Semaphore" \/><\/a>/" },
		]

