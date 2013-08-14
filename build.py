import jinja2
import collections, os

loader = jinja2.FileSystemLoader("src")
env = jinja2.Environment(loader = loader, lstrip_blocks = True, trim_blocks = True)

sections = collections.OrderedDict()
directories = collections.OrderedDict()

site_vars = {
    "title": "Rapptz",
    "css": "stylesheets/",
    "js": "javascripts/",
    "sections": sections,
    "directories": directories,
}

def add_section(name):
    sections[name] = { "name": name, "title": name.title() }

def add_directory(name, title, has_section = True):
    if has_section:
        sections[name] = { "name": name + "/index", "title": title.title() }
    directories[name] = { "name": name, "title": title.title(), "dir": name + '/', "has_section": has_section }

def render_section(name, is_section = True):
    site_vars["dir"] = "./"
    html = name + ".html"
    if not os.path.isfile(html):
        return
    template = env.get_template(html)

    if is_section:
        site_vars["current_section"] = sections[name]
    else:
        site_vars["current_section"] = ""
    result = template.render(site_vars)

    with open(html, 'w') as f:
        f.write(result)

def render_directory(name, has_section = True):
    # Modify the site variables to jump one directory.
    site_vars["dir"] = "../"
    if has_section:
        site_vars["current_section"] = sections[name]

    prefix = name + '_'

    # Loop through the directory and render them
    # For every file in the src directory that
    # matches name_ prefix, retrieve it.
    files = [x for x in os.listdir('src') if x.startswith(prefix)]

    for file in files:
        template = env.get_template(file)
        result = template.render(site_vars)
        html = name + '/' + file.lstrip(prefix)

        with open(html, 'w') as f:
            f.write(result)

def render():
    for section in sections:
        render_section(section)
    for directory in directories.values():
        render_directory(directory["name"], directory["has_section"])
    render_section("index", False)

add_section("projects")
add_directory("cpptuts", "C++ Tutorials")
render()