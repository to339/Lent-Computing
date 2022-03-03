from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib







    
def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels

    print(x)
    d0 = x[0]
    p_coeff = np.polyfit(x-d0, y, p)
    


    poly = np.poly1d(p_coeff)
    

    
    return (poly,d0)
