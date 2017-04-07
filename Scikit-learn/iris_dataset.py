#import load_iris function from datasets module
from sklearn.datasets import load_iris
iris = load_iris()
#print(type(iris))
#print(iris.data)#150 rows and 4 columns
print(iris.feature_names)
print(iris.target) #values of outcomes of all inputs here [0,1,2] are possible values
print(iris.target_names)#all outcomes(in classification) names
print(iris.target.shape)
x = iris.data #store feature matrix in x\
y = iris.target # store vector response in vector y