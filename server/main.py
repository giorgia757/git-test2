from datetime import datetime
from flask import Flask, render_template_string


app = Flask(__name__)


def get_render_template_string():
    with open('templates/index.html') as f:
        template_string = f.read()
    return template_string


@app.route('/')
def index():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    template_string = get_render_template_string()
    return render_template_string(template_string.format(current_time=current_time))


if __name__ == "__main__":
    app.run(debug=True)
