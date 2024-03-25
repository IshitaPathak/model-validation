# model-validation-eos30gr

## Model Overview

The hERG channel plays a crucial role in regulating the heart's electrical signals. However, certain drugs have the potential to block this channel, leading to a condition known as long QT syndrome, which can trigger dangerous heart rhythm abnormalities.

To identify drugs that may pose this risk, Ersilia developed deephERG, a computer-based model. Leveraging deep neural networks, deephERG analyzes extensive datasets containing information on thousands of chemicals. By scrutinizing the chemical structures and properties of these compounds, deephERG can predict their likelihood of blocking the hERG channel.

#

 The repository is organized into several folders:
 
  * `/notebooks`: Contains Jupyter notebooks where the most work is developed.
  * `/data`: Holds all csv files. Model predictions, obtained externally, are saved here. 
  * `/src`: Stores important functions for reuse throughout the repository, reducing the need for repetitive typing.
  * `/figures`: Contains plots produced during the model validation process.
    
  Additionally, there's a `requirements.txt` file listing all required packages to run the notebooks in this repository.
