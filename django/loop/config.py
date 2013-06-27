# Jinja2
# from jinja2 import Environment, PackageLoader
# JinjaEnv = Environment(loader = PackageLoader('symply', 'templates'))
from jinja2 import Environment, PackageLoader, FileSystemLoader
import os
template_dir = os.path.join(os.path.dirname(__file__), "templates")
# JinjaEnv = Environment(loader = PackageLoader('autosync', 'templates'))
JinjaEnv = Environment(loader = FileSystemLoader(template_dir), autoescape=True)
