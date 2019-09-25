

# ========================================================
# A SIMPLE TRAINING PROGRAM TO INTEGRATE ODEs USING PYTHON
#    WITH THE EXTENDED EULER METHOD
# ========================================================

# ==============================================
# OBJECTIVE:
# -> assume you are given the ODE    dy/dx = (cos x)**2
#           with initial condition y(x=0) = 0 
# -> The x interval to solve the equation is (0, 8)
#
# -> the analytical solution (for comparison) is  
#                         y(x) = x/2 + sin(2x)/4

# -> THIS PROGRAM SOLVES THE ODE AND COMPARES IT 
#         WITH THE ANALYTICAL SOLUTION

# ==============================================

# -----------------
# HEADERS - 
import numpy as np
import matplotlib.pyplot as plt
#plt.ion()  # uncomment this for interactive plotting (e.g., with ipython).
# -----------------

# -------------------------
# PARAMETERS OF THE PROBLEM 
x0 = 0. 
xf = 8.
y0 = 0. 
# -------------------------

# -------------
# THE GRID IN x
# -------------
npx = 64 # at best an integer power of 2, for later grid refinement
         # Check different values (from very low --16-- to very high --4096--
         #    to see how the solution improves when you increase npx 
         #    using successive powers of 2)  
dx = (xf-x0)/npx
# --------------

# ---------------------------
# CHOOSE BETWEEN THE BASIC, FIRST ORDER EULER METHOD (secondorder = 0)
#         or THE EXTENDED, SECOND ORDER METHOD       (secondorder = 1)
secondorder = 1
# --------------------------

# ----------------------------
# ARRAY AND COUNTER INITIATION
xx = np.array([x0]) # initiate a numpy array for the abscissas
yy = np.array([y0]) # initiate a numpy array for the solution 
it =  0   # this is just a counter 
# ----------------------------

# -----------------------------------------------------
# DEFINE THE FUNCTION ON THE RIGHT-HAND SIDE OF THE ODE
def ff(xxx, yyy):
    return np.cos(xxx)**2.
# -----------------------------------------------------
    
# -----------------------------------
# THE MAIN INTEGRATION LOOP

while xx[-1] <= xf:
    yynew = yy[-1] + dx * ff(xx[-1], yy[-1])
    xxnew = xx[-1] + dx

    if secondorder:
        ffave = (ff(xx[-1], yy[-1]) + ff(xxnew, yynew)) /2.
        yynew = yy[-1] + dx*ffave

    yy = np.append(yy, yynew) # enlarge the solution array
    xx = np.append(xx, xxnew) # enlarge the x-array

    it += 1   # increase the counter
# -----------------------------------


# -----------------------
# THE ANALYTICAL SOLUTION
yyan = xx/2 + np.sin(2*xx)/4.
# -----------------------


print("I have finished in ", it, " steps")

# ----------------
# PLOTTING SECTION
# ----------------

plt.clf()
plt.figure(num=2,figsize=(8,8))

plt.plot(xx,yy,linewidth=3)
plt.plot(xx, yyan,"r",linewidth=3)
plt.legend(("numerical solution","analytical solution"))

plt.title("ODE solution",fontsize=20,color='k')

plt.xlabel("x",fontsize=20)
plt.ylabel("y",fontsize=20)

plt.show()



