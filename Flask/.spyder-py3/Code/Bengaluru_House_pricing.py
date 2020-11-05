from flask import Flask  
app = Flask(__name__)  
@app.route('/get_location_names')   
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
        })
    response.headers.add('Access-control-allow-origin','*')
    return response 

if __name__ == '__main__':
 app.run()


