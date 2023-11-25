from flask import Flask, make_response, render_template

import pdfkit


config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe')



app = Flask(__name__)

@app.route('/<name>/<location>')
def home(name,location):
    rendered =render_template('index.html',name=name,location=location)

    pdf = pdfkit.from_string(rendered,False,configuration=config)

    response = make_response(pdf)

    response.headers['Content-Type'] = 'application/pdf'

    response.headers['Content-Disposition'] = 'inline;filename=output.pdf'

    return response
if __name__ == "__main__":
    app.run(debug=True)