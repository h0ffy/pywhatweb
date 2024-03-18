import sys
import os
			
class Pluginerror_log_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "filepath" : "/\[[\d]{2}\-[A-Za-z]{3,4}\-[\d]{4} [\d]{2}:[\d]{2}:[\d]{2}\] PHP .{1,50}: .* in (.*) on line [0-9]+/" },
			{ "account" : "/\[[\d]{2}\-[A-Za-z]{3,4}\-[\d]{4} [\d]{2}:[\d]{2}:[\d]{2}\] PHP .{1,50}: .* in \/home\/([^\/]{1,32})\/.* on line [0-9]+/" },
		]

