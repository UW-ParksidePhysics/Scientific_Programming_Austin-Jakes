import numpy as np

def gaussian(position, mean=0, standard_dev=1):

    Left_equation = 1 / (np.sqrt(2 * np.pi) * standard_dev)
    Exponential = -0.5 * ((position - mean) / standard_dev)**2
    return Left_equation * np.exp(Exponential)

if __name__ == "__main__":

    m = 0      
    s = 1      
    n = 10     
    
    x_values = np.linspace(m - 5*s, m + 5*s, n)
    f_values = gaussian(x_values, m, s)
    
    print(f"{'n':<5}  {'x':<5}  {'f(x)':<5}")
    print("-" * 100)
    
    for i in range(len(x_values)):
        print(f"{i+1:<5}  {x_values[i]:<5.3f}  {f_values[i]:<5.3f}")