from flask import Flask
from flask import jsonify
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


def get_db_data():
    DATABASE_URL = os.environ['DATABASE_URL']
    db = create_engine(DATABASE_URL)

    sql = text('SELECT * FROM datas')
    results = db.execute(sql)
    return results


@app.route('/')
def index():
    return ('Welcome to get temperature and humidity data')

@app.route('/api')
def api():
    results = get_db_data()
    data = []
    line = 0 

    for row in results:
        r = [row['times'],row['temperature'], row['humidity']]
        data.insert(line, r)
        line +=1

    return jsonify({'data': data})

if __name__ == '__main__':
    app.config['DEBUG']=True
    app.run(threaded=True, port=5000)