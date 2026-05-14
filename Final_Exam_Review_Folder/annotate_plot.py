__author__

import matplotlib.pyplot as plt
import numpy as np

def annotate_plot(annotations: dict) -> list:
    annotation_objects = []
       for label, config in annotations.items():
            if not all(key in config for key in ('position', 'alignment', 'fontsize')):
                raise KeyError(f"Missing required keys in annotation: {label}")

pos = config['position']
ha, va = config['alignment']
fs = config['fontsize']

text_obj = plt.text(
            pos[0], pos[1], label,
            horizontalalignment=ha,
            verticalalignment=va,
            fontsize=fs
        )
        annotation_objects.append(text_obj)
        
return annotation_objects

if __name__ == "__main__":
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y)
    plt.title("Sample Annotated Plot")

plt.grid(True)
plt.show()

