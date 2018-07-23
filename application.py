from flask import Flask, render_template

application = Flask(__name__)
application.debug = False


@application.route("/", methods=['GET', 'POST'])
def main():
    return render_template('index.html')


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=25200)
