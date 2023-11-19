
from jazzmin.settings import AbstractSettings

class Settings(AbstractSettings):
    # Customize your settings here
    show_title = False
    show_ui_builder = False
    change_form_template = 'admin/custom_change_form.html'
    custom_css = {
        'all': ['path/to/your/custom.css'],
    }
