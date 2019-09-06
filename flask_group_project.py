from flask import Flask, redirect
app = Flask(__name__)
@app.route('/')
def home():
    return "Are you ready to play a game? Get ready! Please type your name into the url."

@app.route('/<name>')
def pill(name):
    return f"{name}, please choose between the RED pill or BLUE pill by typing that color into the url."

@app.route('/<name>/<color>')
def redPill(name, color):
    if color == 'red':
        return f"{name}, wise choice. Choose HEADS or TAILS"
    else:
        return redirect('/' + name)

@app.route('/<name>/red/<coin>')
def coin(name, coin):
        if 'heads' == coin:
            return f"{name}, you made the right choice. Type a number between 1 and 10"
        else:
            return redirect('/' + name)

@app.route('/<name>/red/heads/<num>')
def number(name, num):
    num = int(num)
    if num < 5 and num > 0:
        return f"OMG {name}, you earned yourself a one way trip to Dasney Land. Piece out!"
    elif num >= 5 and num <= 10:
        return f"{name}, you recieved a glorious applause and move forward. You are given a gift. Do you OPEN it, give it AWAY, or give it to your CAT?"
    else:
        return f"GAME OVER, {name}...you're going to jail!"
    
@app.route('/<name>/red/heads/<num>/<gift>')
def gift(name, num, gift):
    if gift == 'cat':
        return "The cat sniffed the gift and walked away. Sad face."
    elif gift == 'open':
        return f"Congratulations {name} you now have become NASA's next astronaut! Do you want to go to the MOON or MARS"
    else:
        return "Loser...You just gave up a free trip to space."

@app.route('/<name>/red/heads/<num>/open/<space>')
def space(name, num, space):
    if space == 'moon':
        return redirect('/' + name)
    elif space == 'mars':
        return redirect('/' + name)
    else:
        return "We're done..."





if __name__=="__main__":
    app.run(debug=True)