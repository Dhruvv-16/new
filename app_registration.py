import streamlit as st
import json

st.set_page_config(page_title="App Registration", layout="wide")
st.title("📋 App Registration")

# UI elements to input app registration details
app_name = st.text_input("App Name")
log_source = st.selectbox("Log Source", ["Datadog", "ELK", "Custom API"])
api_url = st.text_input("API URL (for logs)")

# Input API keys for Datadog or ELK
if log_source == "Datadog":
    datadog_api_key = st.text_input("Datadog API Key", type="password")
    datadog_app_key = st.text_input("Datadog App Key", type="password")
elif log_source == "ELK":
    elk_url = st.text_input("ELK URL")
elif log_source == "Custom API":
    custom_api_url = st.text_input("Custom API URL")

# Handle form submission
if st.button("Register App"):
    app_data = {
        "App Name": app_name,
        "Log Source": log_source,
        "API URL": api_url,
    }
    if log_source == "Datadog":
        app_data["Datadog API Key"] = datadog_api_key
        app_data["Datadog App Key"] = datadog_app_key
    elif log_source == "ELK":
        app_data["ELK URL"] = elk_url
    elif log_source == "Custom API":
        app_data["Custom API URL"] = custom_api_url

    # Save app data to file
    try:
        with open("registered_apps.json", "r+") as f:
            data = json.load(f)
            data.append(app_data)
            f.seek(0)
            json.dump(data, f)
    except Exception as e:
        st.error(f"Error saving registration: {e}")

    st.success("App Registered Successfully!")
