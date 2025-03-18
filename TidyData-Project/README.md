## Tidy Data Project

The goal of this project is to demonstrate various methods of cleaning, transforming, and visualizing data using the principles of tidy data. The project uses Python with Pandas and Matplotlib in a Jupyter notebook, and a dataset of 2008 olympic medalists to perform the different organizational functions. 

## What is Tidy Data?

Tidy data refers to datasets organized in such a way that the data can be parsed through easily by common data analysis tools like Pandas and Seaborn. It's a standard way to arrange data, and makes it easier to perform analysis and aggregations. The standard principles are the following:

1. Each variable forms a column
2. Each observation forms a row
3. Each value is a cell

## Instructions for Use:

Clone repository and type cd main.ipynb into the terminal following the name of the repository. This will open the main jupyter notebook.
Be sure to pip install pandas, matplotlib, and jupyter.
The dataset used is included in the repository.

## Dataset Description

This dataset looks at medals won in the 2008 olympics relative to the location of the athlete who won them. Rather than country, this dataset uses NUTS (Nomenclature of Territorial Units for Statistics) regions in Europe. The pre-processing steps taken prior to analysis of the data included melting the dataset such that each variable has its own column and each observation forms a row, and string cleaning to remove unwanted information cluttering up the table. 

## References  

- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)  
- [Tidy Data Principles by Hadley Wickham](https://vita.had.co.nz/papers/tidy-data.pdf)  

