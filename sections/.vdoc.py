# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| echo: true

# Code for plotting gamma

import numpy as np
import matplotlib.pyplot as plt

t = np.array([-3,-2,-1,0,1,2,3])
f = t**2
plt.plot(t,f)
plt.plot(t,f,"ko")
plt.show()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| echo: true

# Displaying output of np.linspace

import numpy as np

t = np.linspace(-3,3, 7)
print("t =", t)
#
#
#
#
#
#| echo: true

# Plotting gamma with finer step-size

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-3,3, 100)
f = t**2
plt.plot(t,f)
plt.show()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| echo: false
#| fig-cap: "Fermat's spiral" 
# Plotting gamma with finer step-size

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,50, 500)
x = np.sqrt(t) * np.cos(t)
y = np.sqrt(t) * np.sin(t)

plt.plot(x,y)
plt.show()
#
#
#
#
#
#
#| echo: true
#| fig-cap: "Adding a bit of style" 
#| code-overflow: wrap

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,50, 500)
x = np.sqrt(t) * np.cos(t)
y = np.sqrt(t) * np.sin(t)

plt.figure(1, figsize = (5,5))

plt.plot(x, y, "--", color="deeppink", linewidth=1.5, label="Spiral")
plt.grid(True, color="lightgray")
plt.title("Fermat's spiral for t between 0 and 50")
plt.xlabel("x-axis", fontsize = 15)
plt.ylabel("y-axis", fontsize = 15)
plt.legend()
plt.show()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| echo: true

import numpy as np

t = np.arange(0,1, 0.2)
print("t =",t)
```
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| echo: false
#| fig-cap: "The 5 x 5 grid corresponding to the matrix A"
 
import numpy as np
import matplotlib.pyplot as plt

x_list = np.linspace(0, 4, 5)
y_list = np.linspace(0, 4, 5)

X, Y = np.meshgrid(x_list, y_list)

plt.figure(figsize = (5,5))
plt.plot(X,Y, marker='.', color='k', linestyle='none')
#
#
#
#
#
#
#
import numpy as np

x_list = np.linspace(0, 4, 5)
y_list = np.linspace(0, 4, 5)

print("x = ", x_list)
print("y = ", y_list)
```
#
#
#
#
#
#| echo: true
#| fig-cap: "Plot of the curve defined by f=0" 

# Plotting f=0

import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(-1, 1, 5000)
ylist = np.linspace(-1, 1, 5000)
X, Y = np.meshgrid(xlist, ylist)

Z =((3*(X**2) - Y**2)**2)*(Y**2) - (X**2 + Y**2)**4 

plt.figure(figsize = (5.5,5.5))
plt.contour(X, Y, Z, [0])
plt.xlabel("x-axis", fontsize = 15)
plt.ylabel("y-axis", fontsize = 15)
plt.show()
#
#
#
#
#
#
#
#
#
#
