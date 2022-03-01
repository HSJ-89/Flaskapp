from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    return {
        'product': ['111',
                    '222',
                    '333',
                    '444',
                    '555']
    }
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 83, debug=True)