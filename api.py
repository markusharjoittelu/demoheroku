from flask import Flask
from flask import jsonify
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
# Allow Cross Origin Resource Sharing for all origins
# For demo use only
CORS(app)
load_dotenv()

# Create SQL query using sqlalchemy params to get data from DB
def get_db_data():
    DATABASE_URL = os.environ['DATABASE_URL']
    db = create_engine(DATABASE_URL)
    sql = text('SELECT * FROM datas')
    results = db.execute(sql)
    return results

# Data server root route, nothing here
@app.route('/')
def index():
    return ('Welcome to get temperature and humidity data')

# Data server api route for getting data in json form
@app.route('/api')
def api():
    results = get_db_data()
    data = []
    line = 0 

    # Inset data from DB to list for jsonify function
    for row in results:
        r = [row['id'],row['times'],row['temperature'], row['humidity']]
        data.insert(line, r)
        line +=1

    return jsonify(data)

if __name__ == '__main__':
    app.config['DEBUG']=True
    app.run(threaded=True, port=5000)