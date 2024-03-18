import sys
import os
			
class mootools_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "regexp" : '/^\/\/ Load your build at: http:\/\/mootools.net\/core\// },
			{ "version" : '/^MooTools.More[\s]*=[\s]*\{[\s]*version:[\s]*["']?([^\"^\']+)["']?/ },
			{ "version" : '/^var MooTools[\s]*=[\s]*\{[\s]*version:[\s]*["']?([^\"^\']+)/ },
			{ "regexp" : '/^\/\/MooTools More", "<http:\/\/mootools.net\/more>. Copyright \(c\) 2006-2008 Valerio Proietti", "<http:\/\/mad4milk.net>", "MIT Style License./ },
		]

