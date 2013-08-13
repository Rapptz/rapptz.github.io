import jinja2
import collections

loader = jinja2.FileSystemLoader("src")
env = jinja2.Environment(loader = loader)

sections = collections.OrderedDict()

site_vars = {
    "title": "Rapptz",
    "css": "stylesheets/",
    "js": "javascripts/",
    "sections": sections,
    "dir": ""
}

def add_section(name):
    sections[name] = { "name": name, "title": name.title() }

def render_index():
    name = "index.html"
    template = env.get_template(name)
    result = template.render(site_vars)

    with open(name, 'w') as f:
        f.write(result)

def render_section(name):
    html = name + ".html"
    template = env.get_template(html)
    site_vars["current_section"] = sections[name]
    result = template.render(site_vars)

    with open(html, 'w') as f:
        f.write(result)

def render():
    render_index()
    for section in sections:
        render_section(section)

add_section("projects")
render()