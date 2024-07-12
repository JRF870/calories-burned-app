import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'RPM': list(range(40, 121)),
    'Watts': [92, 97, 102, 107, 113, 119, 125, 131, 138, 145, 152, 160, 167, 176, 184, 193, 202, 212, 222, 232, 243, 254, 266, 278, 290, 303, 316, 330, 344, 358, 373, 389, 404, 421, 438, 455, 473, 491, 510, 529, 549, 569, 590, 612, 634, 656, 680, 703, 728, 753, 778, 804, 831, 858, 886, 915, 944, 974, 1004, 1035, 1067, 1099, 1132, 1166, 1200, 1235, 1271, 1307, 1344, 1382, 1420, 1459, 1499, 1540, 1581, 1623, 1666, 1709, 1753, 1798, 1844],
    'Calories/min': [4.6, 4.9, 5.1, 5.3, 5.6, 6.0, 6.2, 6.5, 6.9, 7.2, 7.6, 8.0, 8.3, 8.8, 9.2, 9.6, 10.1, 10.6, 11.1, 11.6, 12.1, 12.7, 13.3, 13.9, 14.5, 15.1, 15.8, 16.5, 17.2, 17.9, 18.6, 19.4, 20.2, 21.0, 21.9, 22.7, 23.6, 24.5, 25.5, 26.4, 27.4, 28.4, 29.5, 30.6, 31.7, 32.8, 34.0, 35.1, 36.4, 37.6, 38.9, 40.2, 41.5, 42.8, 44.2, 45.6, 47.0, 48.5, 49.9, 51.4, 53.0, 54.5, 56.1, 57.7, 59.3, 60.9, 62.6, 64.3, 66.0, 67.8, 69.6, 71.4, 73.2, 75.1, 76.9, 78.9, 80.8, 82.7, 84.7, 86.7, 88.8]
}

df = pd.DataFrame(data)

# Streamlit App
st.title('Calories Burned Calculator')

st.write("""
Adjust the RPM slider to see the corresponding calories burned per minute.
""")

# RPM Slider
rpm = st.slider('RPM (Cadence)', min_value=40, max_value=120, value=80)

# Find the corresponding calories/min
calories_per_min = df.loc[df['RPM'] == rpm, 'Calories/min'].values[0]

# Display the result
st.write(f"At {rpm} RPM, you burn approximately {calories_per_min} calories per minute.")

# Plotting the data
fig, ax = plt.subplots()
ax.plot(df['RPM'], df['Calories/min'], label='Calories/min vs RPM', color='blue')
ax.scatter(rpm, calories_per_min, color='red')  # Highlight the selected RPM point
ax.set_xlabel('RPM')
ax.set_ylabel('Calories/min')
ax.set_title('Calories Burned per Minute')
ax.legend()

st.pyplot(fig)
