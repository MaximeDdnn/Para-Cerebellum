from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import pandas as pd
import nibabel as nib
import matplotlib.pyplot as plt

# templating
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template.html")

tab = pd.read_csv('lut_perso.csv')


template_vars = {
    "recap_image": tab.to_html()}

html_out = template.render(template_vars)

# generate PDF
HTML(string=html_out, base_url='.').write_pdf("report3.pdf", stylesheets=["typography.css"])

