import sys
import os
			
class codeigniter_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "string" : '404 Signature',"url" : randstr(),"md5" : 'e087ab5729efdfa939ba620e4593bd99'}
			{ "string" : '404 Signature',"url" : 'index.php/'+randstr(),"md5" : 'e087ab5729efdfa939ba620e4593bd99'}
			{ "string" : 'Database Error Signature',"url" : 'index.php/'+randstr(),"md5" : '951c845488483135e52252609a1d99b2'}
			{ "string" : 'Database Error Signature',"md5" : '951c845488483135e52252609a1d99b2'}
			{ "string" : 'Invalid Character Filter',"url" : randstr()+'!!!',"md5" : 'c9b724012ab64481a034f9a453143ece'}
			{ "string" : 'Invalid Character Filter',"url" : randstr()+'!!!',"text" : 'The URI you submitted has disallowed characters.'}
			{ "search" : 'headers[set-cookie]", "regexp" : '/ci_session/", "name" : 'ci_session cookie" }
	]

