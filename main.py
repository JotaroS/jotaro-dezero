from core import Variable
import numpy as np


data = np.array(1.0)
x = Variable(data)
print(x.data)