import sys
import os
			
class liferay_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : 'Powered by Liferay Portal", "certainty" : '10 }
			{ "text" : '<![CDATA[*/Liferay.Util.addInputFocus();/*]]>*" }
			{ "search" : 'headers[liferay-portal]", "string" : /^Liferay Portal (.+ Edition) (.+)$/ }
			{ "search" : 'headers[liferay-portal]", "version" : '/^Liferay Portal (.+ Edition) (.+)$/", "offset" : '1 }
			{ "search" : 'headers[set-cookie]", "regexp" : '/GUEST_LANGUAGE_ID=[a-z]{2,3}_[A-Z]{2,3};/ }
	]

