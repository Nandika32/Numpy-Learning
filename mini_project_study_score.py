import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([20,40,60,80,100])
print("Hours studied:",x)
print("Marks obtained:",y)
w=10
y_pred=x*w
print("Predicted scores:",y_pred)
error=np.abs(y-y_pred)
print("Error:", error)
print("Mean error:", np.mean(error))
w = 20
y_pred = x * w
print("Final predictions:", y_pred)
print("Final error:", np.mean(np.abs(y - y_pred)))
