import logging
from flask import Flask,  render_template, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint
POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

@app.errorhandler(400)
def bad_request_error(error):
    logging.info(error)
    return render_template("error.html")



@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

if __name__ == "__main__":
  app.run()

