import sys
import os
			
class my_php_indexer_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "version" : '/<!--Copyright--><a target="_blank" class="l" href="http:\/\/www.mafiatic.com">Powered by My PHP Indexer ([\d\.]+) \| Copyright &copy; [0-9]{4}\-[0-9]{4} Mafiatic Inc.<\/a><!--Copyright-->/ }
	]

