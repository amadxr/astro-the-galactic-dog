from app import app

@app.route('/')
@app.route('/index')
def index():
    return "I'm Astro, the Galactic Dog"
