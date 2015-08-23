from flask import Flask
from Model import Dumpster, Vote
from DB import Store
from geojson import FeatureCollection

app = Flask(__name__)

store = Store()
session = store.session

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dumpster/all')
def all_dumpsters():
    dumpsters = store.get_all(Dumpster)
    features = []
    for dumpster in dumpsters:
        features.append(dumpster.__geojson__())
    featurecollection = FeatureCollection(features)
    return str(featurecollection)

@app.route('/dumpster/vote/<int:id>/<string:vote>')
def vote(id, vote):
    dumpster = store.get(Dumpster, id=id)
    if dumpster is None:
        return "Error 1"
    elif not (vote is 'up' or 'down'):
        return "Error 2"
    else:
        if vote == 'up':
            value=1
        elif vote == 'down':
            value=-1
        else:
            return "Error 3" + vote
        new_vote = Vote(dumpster=dumpster, value=value)
        store.session.add(new_vote)
        store.session.commit()
        return "OK"
if __name__ == '__main__':
   app.run(port=5001, debug=True)
