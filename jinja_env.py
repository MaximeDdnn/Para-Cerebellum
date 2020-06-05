from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# templating
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template.html")

template_vars = {"visuel_image" : "lalal",
                 "recap_image" : "lolo"}

html_out = template.render(template_vars)

# generate PDF
HTML(string=html_out).write_pdf("report.pdf")


