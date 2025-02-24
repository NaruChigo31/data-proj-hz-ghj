from graph1_plotly import fig1
from graph2_plotly import fig2
from graph3_plotly import fig3
# from graphs_all import graph1, graph2, graph3

from jinja2 import Template

output_html_path=r"../app/templates/graphs.html"
input_template_path = r"template.html"      

plotly_jinja_data = {"fig1":fig1.to_html(full_html=False), 
                     "fig2":fig2.to_html(full_html=False), 
                     "fig3":fig3.to_html(full_html=False)}

with open(output_html_path, "w", encoding="utf-8") as output_file:
    with open(input_template_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(plotly_jinja_data))
