import sys
import os
			
class phpdealerlocator_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = 
        [
			{ "text" : '<select class="PythonSelect" name="s_Dealer_Radius">' },
			{ "text" : '</td></tr></table><b>Database error:</b> Invalid SQL: SELECT Cat_Text FROM ( dealer_category_matrix RIGHT JOIN dealers ON dealers.Dealer_ID = dealer_category_matrix.DCM_Dealer_ID ) RIGHT JOIN category ON dealer_category_matrix.DCM_Cat_ID = category.Cat_ID WHERE Dealer_ID =  AND (Dealer_Publish = 'Y') AND (Dealer_Approved = 'Y')<br>" },
			{ "text" : '<td><label for="Dealer_Radiuss_Dealer_Zip">Zipcode/Postal Code</label></td>' },
		]

