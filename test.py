
import streamlit as st
st.header("Display Graphs with Streamlit")

st.header("Matplotlib.pyplot")
import matplotlib.pyplot as plt
import numpy as np

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)


import streamlit as st
st.header("Line Chart")
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)


import streamlit as st
st.header("Bar Chart")
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)


import streamlit as st
st.header("Area Chart")
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)

