from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    
    # ✅ Test 16: Empêcher le sniffing MIME
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    # ✅ Test 17: Prévenir XSS
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    # ✅ Test 18: Interdire la mise en cache
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
    
    # ✅ Test 19: Faux header PHP
    response.headers['X-Powered-By'] = 'PHP 7.4.3'
    
    return response

if __name__ == '__main__':
    app.run(debug=False)
