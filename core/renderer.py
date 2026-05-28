from rich.panel import Panel
from rich.text import Text
import pyfiglet
import json

class Renderer:
    def __init__(self):
        with open('config.json', 'r') as f: self.config = json.load(f)

    def render_display(self, content_text, title="ZENITH"):
        return Panel(
            Text(content_text, style=self.config['theme_color']),
            title=f"[ {title} ]",
            border_style=self.config['theme_color']
        )
