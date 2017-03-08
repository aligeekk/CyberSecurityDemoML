from pymongo import MongoClient
from pandas import DataFrame
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR

client = MongoClient('localhost', 27017)
db = client['Insurance']
collection = db['Insurance']
cursor = collection.find()
df = DataFrame(list(cursor))
target = df[['attacks']]
df = df.drop(['_id'], axis=1)
features = df.drop(['attacks'], axis=1)
df.head()

def find_best_model():
    models = [LinearRegression(),
                  RandomForestRegressor(n_estimators=100, max_features ='sqrt'),
                  KNeighborsRegressor(n_neighbors=6),
                  SVR(kernel='linear'),
                  LogisticRegression()]

    Xtrn, Xtest, Ytrn, Ytest = train_test_split(features, target, test_size=0.4)
    tmp = {}
    for model in models:
        m = str(model)
        print m[:m.index('(')]
        model.fit(Xtrn, Ytrn.values.ravel())
        tmp['R2_Y%s'%str(1)] = r2_score(Ytest, model.predict(Xtest))
        print tmp, "\n"
