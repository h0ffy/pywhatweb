import sys
import os
			
class kibana_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "search" : 'headers[x-app-name]", "regexp" : '/^kibana$/ }
			{ "text" : '<body kibana ng-class' }
			{ "version" : '/<script>\s+window\.KIBANA_VERSION='([\d\.]+)';\s+window\.KIBANA_BUILD_NUM='[\d]+';/ }
			{ "name" : 'kbn-name header", "search" : 'headers[kbn-name]", "text" : '' }
			{ "name" : 'kbn-injected-metadata", "search" : 'body", "version" : '/<kbn-injected-metadata data="{&quot;version&quot;:&quot;([0-9\.]+)/ }
		]

