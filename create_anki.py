from flask import Flask, request
import json
import urllib.request

app = Flask(__name__)

# Set up AnkiConnect URL
anki_url = "http://localhost:8765"


def anki_request(action, **params):
    return {"action": action, "params": params, "version": 6}


def invoke(action, **params):
    requestJson = json.dumps(anki_request(action, **params)).encode("utf-8")
    response = json.load(
        urllib.request.urlopen(urllib.request.Request(anki_url, requestJson))
    )
    if len(response) != 2:
        raise Exception("response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("response is missing required error field")
    if "result" not in response:
        raise Exception("response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])
    return response["result"]


def note_exists(deck_name, back):
    notes_ids = invoke("findNotes", query=f'deck:"{deck_name}"')
    if notes_ids:
        for note_id in notes_ids:
            note_info = invoke("notesInfo", notes=[note_id])
            if note_info[0]["fields"]["Back"]["value"] == back:
                return True
    return False


# Route for creating a new Anki note
@app.route("/anki/notes", methods=["POST"])
def create_anki_notes():
    data = request.get_json()
    deck_name = data.get("deck")
    notes = data.get("notes")

    if deck_name and notes:
        invoke("createDeck", deck=deck_name)
        for note in notes:
            front = note.get("Front")
            back = note.get("Back")
            if note_exists(deck_name, back):
                print(f"Note {front}/{back[:10]}... already exists")
                continue
            anki_note = {
                "deckName": deck_name,
                "modelName": "Basic",
                "fields": note,
                "options": {"allowDuplicate": True},
                "tags": [],  # you can set tags here if needed
            }
            try:
                invoke("addNote", note=anki_note)
            except Exception as e:
                print(f"Error adding note {front}: {str(e)}")
        return "OK"
    else:
        return "Missing deck name or notes data", 400


@app.route("/")
def index():
    return "FLASK CONNECTED"


if __name__ == "__main__":
    app.run(debug=True, port=3001)
