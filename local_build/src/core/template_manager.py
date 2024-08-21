from jinja2 import Environment, FileSystemLoader
import os

def render_template(template_name, context):
   
    template_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    return template.render(context)

if __name__ == "__main__":
    context = {"name": "shrey"}
    rendered_email = render_template("welcome_email.html", context)
    print(rendered_email)
