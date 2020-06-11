from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def make_report(img_name, img_recap,  out_dir):
    # create environment for templating
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("template/template.html")

    # my variables
    template_vars = {
        "img_name": img_name,
        "img_recap": img_recap.to_html(),
        "resultat_suit" : resultat_suit
    }

    # template rendering
    html_out = template.render(template_vars)

    # generate PDF
    HTML(string=html_out, base_url='.').write_pdf("report3.pdf", stylesheets=["css/typography.css"])

