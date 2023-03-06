# -*- coding: utf-8 -*-
"""4 March plotly assignment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W8uxZuzT20Q6uCgq7--O_NLL34qqVMCu
"""

import plotly.graph_objects as go

import seaborn as sns
import plotly.express as px

# Load the titanic dataset
titanic_data = sns.load_dataset("titanic")

# Plot a scatter plot for age and fare columns
fig = px.scatter(titanic_data, x="age", y="fare")
fig.show()

import plotly.express as px
tips_data = px.data.tips()

# Plot a box plot for the "total_bill" column
fig = px.box(tips_data, y="total_bill")
fig.show()

import plotly.express as px
tips_data = px.data.tips()

# Plot a histogram with pattern_shape and color parameters
fig = px.histogram(tips_data, x="sex", y="total_bill", color="day", pattern_shape="smoker")
fig.show()

import plotly.express as px
iris_data = px.data.iris()

# Plot a scatter matrix plot with color parameter
fig = px.scatter_matrix(iris_data, color="species")
fig.show()

Distplot is a function in the seaborn library that allows you to plot a histogram along with a kernel density estimate (KDE) curve for a univariate distribution of observations. It provides a visual representation of the probability density function of a continuous variable.