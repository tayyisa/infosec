from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename
import subprocess, tempfile, os, hashlib, shutil
from pathlib import Path

app = Flask(__name__)
app.secret_key = "secretkey"
UPLOAD_ROOT = Path(tempfile.gettempdir()) / "stegoapp"
UPLOAD_ROOT.mkdir(parents=True, exist_ok=True)

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/embed", methods=["POST"])
def embed():
    cover = request.files.get("cover")
    secret = request.files.get("secret")
    password = request.form.get("password", "")
    if not cover or not secret or not password:
        flash("Missing cover, secret or passphrase", "danger")
        return redirect(url_for("index"))
    cover_name = secure_filename(cover.filename)
    secret_name = secure_filename(secret.filename)
    cover_path = UPLOAD_ROOT / ("orig_" + cover_name)
    secret_path = UPLOAD_ROOT / ("secret_" + secret_name)
    out_path = UPLOAD_ROOT / ("stego_" + cover_name)
    cover.save(cover_path)
    secret.save(secret_path)
    if out_path.exists():
        out_path.unlink()
    shutil.copy2(cover_path, out_path)
    proc = subprocess.run(["steghide", "embed", "-cf", str(out_path), "-ef", str(secret_path), "-p", password], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if proc.returncode != 0:
        flash("Embed failed: " + (proc.stderr.strip() or proc.stdout.strip()), "danger")
        return redirect(url_for("index"))
    return send_file(out_path, as_attachment=True, download_name=out_path.name)

@app.route("/extract", methods=["POST"])
def extract():
    stego = request.files.get("stego")
    password = request.form.get("password_extract", "")
    if not stego or not password:
        flash("Missing stego file or passphrase", "danger")
        return redirect(url_for("index"))
    stego_name = secure_filename(stego.filename)
    stego_path = UPLOAD_ROOT / ("uploaded_" + stego_name)
    stego.save(stego_path)
    temp_dir = UPLOAD_ROOT / ("extract_" + next(tempfile._get_candidate_names()))
    temp_dir.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(["steghide", "extract", "-sf", str(stego_path), "-p", password], cwd=str(temp_dir), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if proc.returncode != 0:
        flash("Extraction failed: " + (proc.stderr.strip() or proc.stdout.strip()), "danger")
        return redirect(url_for("index"))
    extracted_files = list(temp_dir.iterdir())
    if not extracted_files:
        flash("No file extracted", "warning")
        return redirect(url_for("index"))
    extracted = extracted_files[0]
    return send_file(extracted, as_attachment=True, download_name=extracted.name)

if __name__ == "__main__":
    app.run(port=5000, debug=False)
