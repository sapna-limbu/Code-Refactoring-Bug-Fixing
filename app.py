from flask import Flask, render_template, request

app = Flask(__name__)


# Initialize the notes list
notes = []

# Define the route for the home page
@app.route('/', methods=["GET", "POST"])
def index():
    
    if request.method == "POST":
        note = request.form.get("note") # Get the note from the form
        if note: # Check if a note was entered
            notes.append(note)
    return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
