from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/interactive-map')
def interactive_map():
    return render_template('interactive-map.html')

@app.route('/sign-in')
def signIn():
    return render_template('signin-signup.html')

@app.route('/plan-your-visit')
def planYourVisit():
    return render_template('plan-your-visit.html')

@app.route('/about-us')
def aboutUs():
    return render_template('about-us.html')

@app.route('/explore-tours')
def exploreTours():
    return render_template('explore-tours.html')

if __name__ == '__main__':
    app.run(debug=True)