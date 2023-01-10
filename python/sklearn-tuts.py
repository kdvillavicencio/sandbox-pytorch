# SCIKIT LEARN TUTORIAL
# https://www.digitalocean.com/community/tutorials/python-scikit-learn-tutorial

# -- DATASETS --
from sklearn import datasets

# Load data
iris = datasets.load_iris()

# -- SVM --
from sklearn import svm
clf = svm.LinearSVC()
clf.fit(iris.data, iris.target)

# predict for unseen data
clf.predict([[5.0, 3.6, 1.3, 0.25]])

# Parameters of model can be changed by using the attributes ending with an underscore
print(clf.coef_)

# -- LINEAR REGRESSION --
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0,0],[1,1],[2,2]], [0,1,2])
print(reg.coef_)

# -- KNN --
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier()
knn.fit(iris.data, iris.target)

# Predict results
knnResult = knn.predict([[0.1, 0.2, 0.3, 0.4]])
print(knnResult)

# -- KNN CLustering --
from sklearn import cluster

# Create clusters for k=3
k = 3
k_means = cluster.KMeans(k)

# Datafit
k_means.fit(iris.data)

# Print results
print( k_means.labels_[::10])
print( iris.target[::10])