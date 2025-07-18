import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

st.sidebar.title('Animation Settings')
interval = st.sidebar.slider('Animation Speed (ms)', min_value=50, max_value=500, value=200)

st.title('Animated Line Chart')

fig, ax = plt.subplots()
x = np.linspace(0, 70, 100)
y = np.sin(x)
#y=np.linspace(-60,10,100)

line, = ax.plot(x, y)

# def update(frame):
#     line.set_ydata(np.sin(x + frame / 10))
#     return line,

# ani = FuncAnimation(fig, update, frames=np.arange(0,100), interval=interval)

st.pyplot(plt)

st.title('Animated Bar Chart')

fig, ax = plt.subplots()
x = np.arange(10)
y = np.random.randint(1, 10, size=10)

colors = np.random.rand(600,3)  
bars = ax.bar(x, y,color = colors)

### def update(frame):
##     ax.clear()
# #    new_heights = np.random.randint(1, 10, size=10)
##     for bar, h, color in zip(bars, new_heights, colors):
# #        bar.set_height(h)
##         bar.set_color(color)
##     ax.set_ylim(0, 10)
##     ax.set_title('Animated Bar Chart')
##     return bars

# ## Create the animation
# #ani = FuncAnimation(fig, update, frames=range(100), interval=interval)



# def update(frame):
#     ax.clear()
#     new_heights = np.random.randint(1, 10, size=10)
#     for bar, h in zip(bars, new_heights):
#         bar.set_height(h)
#     ax.set_ylim(0, 10)
#     ax.set_title('Animated Bar Chart')
#     return bars

#ani = FuncAnimation(fig, update, frames=range(100), interval=interval)

st.pyplot(plt)


st.title('Animated 3D Bar Chart')

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate initial data
x = np.arange(10)
y = np.arange(10)
x, y = np.meshgrid(x, y)
z = np.zeros_like(x)
dx = dy = 0.5
dz = np.random.rand(10, 10)
#colors = plt.cm.viridis(dz / dz.max())

# Create initial bars
bars = ax.bar3d(x.ravel(), y.ravel(), z.ravel(), dx, dy, dz.ravel(),color = colors)

# Define the update function for animation
# def update(frame):
#     ax.clear()
#     dz = np.random.rand(10, 10)
#     colors = plt.cm.viridis(dz / dz.max())
#     bars = ax.bar3d(x.ravel(), y.ravel(), z.ravel(), dx, dy, dz.ravel(), color=colors)
#     ax.set_title('Animated 3D Bar Chart')
#     return bars,

# # Create the animation
# ani = FuncAnimation(fig, update, frames=range(100), interval=interval)

# Render the animation
st.pyplot(plt)




# Create a streamlit app
st.title('Animated 3D Scatter Plot')

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate initial data
x = np.random.standard_normal(100)
y = np.random.standard_normal(100)
z = np.random.standard_normal(100)
s = ax.scatter(x, y, z)

# Define the update function for animation
def update(frame):
    ax.clear()
    x = np.random.standard_normal(100)
    y = np.random.standard_normal(100)
    z = np.random.standard_normal(100)
    s = ax.scatter(x, y, z)
    ax.set_title('Animated 3D Scatter Plot')
    return s,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=interval)

# Render the animation
st.pyplot(plt)