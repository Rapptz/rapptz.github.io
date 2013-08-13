import jinja2

loader = jinja2.FileSystemLoader("src")
env = jinja2.Environment(loader = loader)

site_vars = {
    "title": "test page",
    "css": "stylesheets/",
    "js": "javascripts/"
}

def render_index():
    name = "index.html"
    template = env.get_template(name)
    result = template.render(site_vars)

    with open(name, 'w') as f:
        f.write(result)

render_index()