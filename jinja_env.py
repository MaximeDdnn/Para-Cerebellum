from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import pandas as pd
import nibabel as nib
import matplotlib.pyplot as plt


def make_report(img_name, img_recap, quick_visual, resultat_suit):
    # create environment for templating
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("template.html")

    # my variables
    template_vars = {
        "img_name": img_name,
        "img_recap": img_recap.to_html(),
        "quick_visual": quick_visual,
        "resultat_suit" : resultat_suit
    }

    # template rendering
    html_out = template.render(template_vars)

    # generate PDF
    HTML(string=html_out, base_url='.').write_pdf("report3.pdf", stylesheets=["typography.css"])

