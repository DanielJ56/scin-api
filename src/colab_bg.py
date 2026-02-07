from google.cloud import storage
from flask import Flask, request,send_file
import json
import io

app = Flask(__name__)

client = storage.Client.from_service_account_json("service_account.json")
bucket = client.bucket('dx-scin-public-data')

@app.route("/image", methods=["GET"])
def get_image():
    ref_id = request.args.get("path")
    path = "dataset/images/" + ref_id
    blob = bucket.blob(path)
    img_bytes = io.BytesIO()
    blob.download_to_file(img_bytes)
    img_bytes.seek(0)
    return send_file(
        img_bytes,
        mimetype="image/png",
        as_attachment=False,
        download_name=ref_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)