import matplotlib.pyplot as plt
import numpy as np

#Could rewrite this part to take user input of an equation
sLigning = "6*x**2-34*x-112"


# create 1000 equally spaced points between -10 and 10
x = np.linspace(-10, 10, 1000)
# calculate the y value for each element of the x vector
y = eval(sLigning, {"x" : x})
fig, ax = plt.subplots()
ax.plot(x, y)


#Funktion der differe med numeriske eller lim
def diffentiere(ligning, xPunkt,h=1e-9):
    """Returnere hældning på ligning str ved xPunkt float"""
    dif = (eval(ligning, {"x": (xPunkt + h)}) - eval(ligning,{"x":xPunkt}))/h
    return dif

#newtons metode
def newtonR(ligning, x, iterations=50):
    newX=x-((eval(ligning,{"x":x}))/(diffentiere(ligning,x)))
    for i in range(iterations):
        newX=newX-((eval(ligning,{"x":newX}))/(diffentiere(ligning,newX)))
    return newX

#Første
nulPunkt1 = newtonR(sLigning,2000)
print(f"Første nulpunkt: {nulPunkt1}")
ax.plot(nulPunkt1, (eval(sLigning,{"x":nulPunkt1})) , marker="o")
#Anden
nulPunkt2 = newtonR(sLigning,-2000)
print(f"Andet nulpunkt: {nulPunkt2}")
ax.plot(nulPunkt2, (eval(sLigning,{"x":nulPunkt2})) , marker="o")


plt.grid()
plt.show()