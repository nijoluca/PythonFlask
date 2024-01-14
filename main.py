from flask import Flask, render_template, request
from spellchecker import SpellChecker


app = Flask(__name__)

spell = SpellChecker()

@app.route('/')
def home():
    return render_template('writing_pad.html')

@app.route('/save', methods=['POST'])
def save_content():
    content = request.form.get('content')
    mistakes = find_spelling_mistakes(content)
    highlighted_content = highlight_mistakes(content, mistakes)

    return render_template('writing_pad.html', content=content, highlighted_content=highlighted_content)

def find_spelling_mistakes(content):
    words = content.split()
    mistakes = spell.unknown(words)
    return mistakes

def highlight_mistakes(content, mistakes):
    for mistake in mistakes:
        content = content.replace(mistake, f'<span style="background-color: yellow;">{mistake}</span>')

    return content

if __name__ == '__main__':
    app.run(debug=True)


