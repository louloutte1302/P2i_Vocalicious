from flask import Flask, request, render_template
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"

sys.path.insert(0, str(SRC_DIR))

from recommend import recommend
from record_audio import record_audio
from play_track import play_preview

app = Flask(__name__)

RESULTS = []
LOGS = []


@app.route("/", methods=["GET", "POST"])
def index():
    global RESULTS, LOGS

    if request.method == "POST":
        action = request.form.get("action")

        upload_dir = BASE_DIR / "data" / "vocals_to_analyse"
        upload_dir.mkdir(parents=True, exist_ok=True)

        if action == "upload":
            file = request.files.get("audio")

            if file is None or not file.filename:
                return render_template(
                    "index.html",
                    results=RESULTS,
                    logs=["Aucun fichier sélectionné."]
                )

            file_path = upload_dir / file.filename
            file.save(file_path)

            results = recommend(file_path)
            logs = ["Analyse terminée."]

            if not results:
                RESULTS = []
                LOGS = ["Aucune recommandation."]
                return render_template(
                    "index.html",
                    results=RESULTS,
                    logs=LOGS
                )

            RESULTS = results
            LOGS = logs

            return render_template(
                "index.html",
                results=results,
                logs=logs
            )

        if action == "record":
            file_path = record_audio()
            results = recommend(file_path)
            logs = ["Enregistrement terminé.", "Analyse terminée."]

            if not results:
                RESULTS = []
                LOGS = ["Aucune recommandation."]
                return render_template(
                    "index.html",
                    results=RESULTS,
                    logs=LOGS
                )

            RESULTS = results
            LOGS = logs

            return render_template(
                "index.html",
                results=results,
                logs=logs
            )

    return render_template(
        "index.html",
        results=RESULTS,
        logs=LOGS
    )


@app.route("/listen", methods=["POST"])
def listen():
    global RESULTS, LOGS

    track_name = request.form.get("track_name")

    if track_name:
        play_preview(track_name)
        LOGS = LOGS + [f"Lecture lancée pour : {track_name}"]

    return render_template(
        "index.html",
        results=RESULTS,
        logs=LOGS
    )


if __name__ == "__main__":
    print("starting flask on 127.0.0.1:5055")
    app.run(host="127.0.0.1", port=5055, debug=True)