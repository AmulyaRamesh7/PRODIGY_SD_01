import streamlit as st

# Page title
st.set_page_config(page_title="Temperature Converter", page_icon="🌡️")

st.title("🌡️ Temperature Conversion App")
st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin.")

# User input
temperature = st.number_input("Enter Temperature Value:", value=0.0)

unit = st.selectbox(
    "Select Original Unit:",
    ("Celsius", "Fahrenheit", "Kelvin")
)

# Conversion logic
def convert_temperature(value, unit):
    if unit == "Celsius":
        c = value
        f = (c * 9/5) + 32
        k = c + 273.15

    elif unit == "Fahrenheit":
        f = value
        c = (f - 32) * 5/9
        k = c + 273.15

    elif unit == "Kelvin":
        k = value
        c = k - 273.15
        f = (c * 9/5) + 32

    return c, f, k


# Button
if st.button("Convert"):
    c, f, k = convert_temperature(temperature, unit)

    st.success("Converted Values:")

    st.write(f"🌡️ Celsius: {c:.2f} °C")
    st.write(f"🌡️ Fahrenheit: {f:.2f} °F")
    st.write(f"🌡️ Kelvin: {k:.2f} K")
