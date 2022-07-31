import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#setting interest rate to 5%
r = 0.05 
cf = pd.DataFrame({
  "Year": [1, 2, 3, 4, 5],
  "Cash_flow": [40000 , 40000, 40000, 40000, 40000]
})
per_dr = (1.0 +r)**cf["Year"]
per_dcf = cf["Cash_flow"]/per_dr
per_dcf = round(per_dcf, 2)
dr_val = round(per_dr - 1, 2)

cf["Discount_rate"] = dr_val
cf["Present_value"] = per_dcf

npv = cf["Present_value"].sum()

print(cf)
print(" ")
print("The net present value of this project: ${npv_value:.2f}.".format(npv_value = npv))

fig = plt.figure(figsize=(5,5))
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.plot(cf["Year"], cf["Present_value"])
ax1.set_xlabel("Years")
ax1.set_ylabel("PV")
ax1.set_title("Present Value Graph")
plt.show()