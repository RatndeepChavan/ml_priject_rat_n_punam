from sklearn.datasets import load_iris
df = load_iris()
x = df['data']
y = df['target']
print(x[110])
# print(x)
# from sklearn.ensemble import RandomForestClassifier
# md = RandomForestClassifier()
# md.fit(x,y)
# print(md.predict(x[:5]))
#
# import pickle
# with open('model.iris', 'wb') as f: pickle.dump(md,f)
# with open('model.iris', 'rb') as f: mm = pickle.load(f)
#
# print(mm.predict(x[50:55]))