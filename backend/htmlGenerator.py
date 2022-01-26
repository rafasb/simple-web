import os
import glob
from proyectos import proyectos
from jinja2 import Environment, FileSystemLoader

# Create the jinja2 environment.
current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))

# Find all files with the j2 extension in the current directory
templates = glob.glob('*.j2') 

def render_template(filename):
    return env.get_template(filename).render(proyectos=proyectos)

html = ""

for f in templates:
    rendered_string = render_template(f)
    html=html+rendered_string

fichero=open(os.path.dirname(current_directory)+"/public-html/resources/bloque.html","w")
fichero.write(html)
fichero.close()
