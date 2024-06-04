#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyslope import *
import plotly.graph_objects as go


# In[2]:


s = Slope(height=3, angle=30, length=10)

fig = s.plot_boundary()
wid, hei = 800, 400
fig.update_layout(width=wid, height=hei, margin=dict(l=20, r=20, t=20, b=20),)


# In[3]:


# Material defined with key word arguments
m1 = Material(
    unit_weight=20,
    friction_angle=45,
    cohesion=2,
    depth_to_bottom=2
)

# Material defined with positional arguments
m2 = Material(20, 30, 2, 5)

# An unlimited number of materials can be assigned at one time
s.set_materials(m1, m2)

fig = s.plot_boundary()
wid, hei = 800, 400
fig.update_layout(width=wid, height=hei, margin=dict(l=20, r=20, t=20, b=20),)


# In[4]:


u1 = Udl(magnitude = 10, offset = 0, length = 2)

s.set_udls(u1)


fig = s.plot_boundary()
wid, hei = 800, 400
fig.update_layout(width=wid, height=hei, margin=dict(l=20, r=20, t=20, b=20),)


# In[5]:


s.set_water_table(1)


fig = s.plot_boundary()
wid, hei = 800, 400
fig.update_layout(width=wid, height=hei, margin=dict(l=20, r=20, t=20, b=20),)


# In[6]:


# The user can change the number of slices and iterations with the method below.
# The line below is implicitly called and only required by the user if they want to change iterations
s.update_analysis_options(
    slices=50,
    iterations=2500,
    tolerance=0.005,
    max_iterations=50
)

# run analysis
s.analyse_slope()

# print out minimum calculated factor of safety
print(s.get_min_FOS())


# In[7]:


s.plot_critical()


# In[8]:


s.plot_all_planes(max_fos=1.8)

fig.update_layout(
    title="Pan Instead of Zoom",
    xaxis_title="X Axis",
    yaxis_title="Y Axis",
    dragmode='pan'  # Sets the interaction mode to 'pan'
)


# In[ ]:





# In[ ]:





# In[ ]:




