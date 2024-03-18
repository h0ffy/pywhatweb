import plugins
			
class Pluginfbi_takedown_notice_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "md5" : "dc0743cd718f16198a72a501ae37fd9a" },
			{ "md5" : "89a9a91804802c42fcc3aadbfaff0e55" },
			{ "url" : "/banner.jpg", "md5" : "5d1d926064c1a4a427100a5833d47dfd" },
		]
		return(self.rules)
