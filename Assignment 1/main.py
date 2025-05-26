import streamlit as st

st.set_page_config(page_title="Google Unit Converter", layout="centered")

st.title("🔄 Google Unit Converter")

category = st.selectbox("Select category", ["Length", "Weight", "Temperature"])

# Unit definitions
units = {
    "Length": ["meter", "kilometer", "mile", "inch", "foot"],
    "Weight": ["gram", "kilogram", "pound", "ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# Conversion functions
def convert_length(value, from_unit, to_unit):
    to_meters = {
        "meter": 1,
        "kilometer": 1000,
        "mile": 1609.34,
        "inch": 0.0254,
        "foot": 0.3048
    }
    value_in_meters = value * to_meters[from_unit]
    result = value_in_meters / to_meters[to_unit]
    return result

def convert_weight(value, from_unit, to_unit):
    to_grams = {
        "gram": 1,
        "kilogram": 1000,
        "pound": 453.592,
        "ounce": 28.3495
    }
    value_in_grams = value * to_grams[from_unit]
    result = value_in_grams / to_grams[to_unit]
    return result

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

# Select units
from_unit = st.selectbox("From Unit", units[category])
to_unit = st.selectbox("To Unit", units[category])
value = st.number_input("Enter value", min_value=0.0, format="%.4f")

if st.button("Convert"):
    if category == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif category == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
