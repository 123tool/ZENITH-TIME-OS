import os, json
from rich.panel import Panel
from rich.text import Text
import pyfiglet

class Renderer:
    def __init__(self):
        with open('config.json', 'r') as f: self.config = json.load(f)
    
    def get_term_size(self):
        try: return os.get_terminal_size().columns
        except: return 80

    def render_display(self, content_text, title="ZENITH"):
        # Penyesuaian ukuran font berdasarkan lebar terminal
        width = self.get_term_size()
        return Panel(
            Text(content_text, style=self.config['theme_color']),
            title=f"[ {title} ]", 
            border_style=self.config['theme_color'],
            width=width - 2
        )
