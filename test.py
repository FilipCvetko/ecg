import pandas as pd
import numpy as np
import wfdb
import ast
import matplotlib.pyplot as plt
import scipy.signal as ss  



path = ""
sampling_rate = 500

Y = pd.read_csv("ptbxl_database.csv", index_col=0)
Y.scp_codes = Y.scp_codes.apply(lambda x: ast.literal_eval(x))

data = wfdb.rdsamp("records100/00000/00008_lr")

agg_df = pd.read_csv("scp_statements.csv", index_col=0)
# Filter out the empty ones.
agg_df = agg_df[agg_df.diagnostic == True]

def aggregate_diagnostic(y_dic):
    tmp = []
    for key in y_dic.keys():
        if key in agg_df.index:
            tmp.append(agg_df.loc[key].diagnostic_class)
    return list(set(tmp))

# Apply diagnostic superclass
Y['diagnostic_superclass'] = Y.scp_codes.apply(aggregate_diagnostic)

print(data[1])
data = np.array(data[0])
print(data.shape)

# Plotajmo drugi odvod
x = np.linspace(0,2,200)
y = data[:200, 2]

# y = ss.savgol_filter(y, window_length=199, polyorder=7)

plt.plot(x,y, "-")
plt.ylim((-1,1))
plt.show()