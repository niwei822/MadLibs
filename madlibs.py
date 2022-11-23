"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]

@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/compliment")
def greet_person():
    """Greet user with compliment."""

    # player = request.args.get("person")

    # compliment = choice(AWESOMENESS)

    return render_template("compliment.html")

@app.route("/game")
def show_madlib_form():
    a_person = request.args.get("person")
    get_choice = request.args.get("choice")
    if get_choice == "yes":
        return render_template("game.html", person=a_person, choice=get_choice)
    else:
        return render_template("goodbye.html", choice=get_choice)
    
@app.route("/madlib")
def show_madlib():
    player = request.args.get("person")
    a_color = request.args.get("color")
    a_noun = request.args.get("noun")
    a_adj = request.args.get("adjective")
    
    return render_template("madlib.html", person=player, color=a_color, noun=a_noun, adjective=a_adj)
    
    


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
