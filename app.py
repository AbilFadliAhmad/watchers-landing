import os
import traceback
from flask import Flask, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

# =====================================================================
# PROTEKSI ERROR HANDLER
# =====================================================================
@app.errorhandler(500)
def handle_500(e):
    return f"<pre>{traceback.format_exc()}</pre>", 500

@app.errorhandler(400)
def handle_400(e):
    return f"<pre>{traceback.format_exc()}</pre>", 400

# =====================================================================
# RUTE UTAMA & HALAMAN 1: LOGIN (/login)
# =====================================================================
@app.route("/", strict_slashes=False)
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003, debug=True)