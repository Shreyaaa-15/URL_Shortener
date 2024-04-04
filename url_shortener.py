from flask import Flask, request, redirect
import string
import random

app = Flask(__name__)

url_mapping = {}

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/')
def index():
    return 'Welcome to the URL shortener!'

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['url']
    short_code = generate_short_code()
    url_mapping[short_code] = long_url
    return f'Shortened URL: {request.host_url}{short_code}'

@app.route('/<short_code>')
def redirect_to_long_url(short_code):
    long_url = url_mapping.get(short_code)
    if long_url:
        return redirect(long_url)
    else:
        return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)
