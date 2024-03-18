import sys
import os
			
class imperva_securesphere_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "name" : 'HTML Body',"text" : '<title>SecureSphere - Default</title>'}
			{ "name" : 'HTML Body',"text" : '<td><font class="gray-text-small">SecureSphere includes software developed by Oracle Corporation.</font></td></tr>'}
			{ "name" : 'HTML Body',"text" : 'src="/SecureSphere/scripts/infra/ActiveRequests.js">'}
			{ "name" : 'HTML Body',"text" : 'src="/SecureSphere/scripts/infra/Mprv.js"></script>'}
			{ "name" : 'HTML Body',"text" : 'src="/SecureSphere/scripts/infra/SessionUtils.js">'}
			{ "name" : 'Location Header", "search" : 'headers[location]", "regexp" : '/SecureSphere\/secsphLogin\.jsp}
		]

