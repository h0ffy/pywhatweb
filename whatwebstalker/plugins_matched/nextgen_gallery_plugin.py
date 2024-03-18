import sys
import os
			
class Pluginnextgen_gallery_plugin:
    def get_rules(self):
        return(self.rules)
    def __init__(self):
        self.rules = [
			{ "regexp" : "/<link rel='stylesheet' id='NextGEN-css'  href='[^']*\/wp-content\/themes\/default_ngg\/nggallery.css\?ver=[\d\.]+' type='text\/css' media='screen' \/>/", "string" : "Wordpress" },
			{ "regexp" : "/<link rel='stylesheet' id='shutter-css'  href='[^']*\/wp-content\/plugins\/nextgen-gallery\/shutter\/shutter-reloaded.css\?ver=[\d\.]+' type='text\/css' media='screen' \/>/", "string" : "Wordpress" },
			{ "regexp" : "/<link rel='stylesheet' id='galleryview-css'  href='[^']*\/wp-content\/plugins\/nggGalleryview\/galleryview.css\?ver=[\d\.]+' type='text\/css' media='screen' \/>/", "string" : "Wordpress" },
			{ "version" : "/<meta name='NextGEN' content='([\d\.]+)' \/>/", "string" : "Wordpress" },
		]

