from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('todo_list.html')