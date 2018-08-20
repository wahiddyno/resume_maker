from flask import Flask,render_template,make_response
import pdfkit

app = Flask('__name__')

@app.route('/generate')#http://127.0.0.1:5000/generate
def generate():
    render = render_template('index.html',name='wahid')
    pdf = pdfkit.from_string(render, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application.pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

    return response

if __name__ == "__main__":
    app.run(debug=True)
