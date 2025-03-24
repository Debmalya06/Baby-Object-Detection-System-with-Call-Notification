import streamlit as st
import threading
from detector import detect_face, stop_detection

st.title("👶 Baby Face Obstruction Detection")

# Start Detection
def start():
    if "detection_thread" not in st.session_state or not st.session_state["detection_thread"].is_alive():
        st.session_state["detection_thread"] = threading.Thread(target=detect_face, daemon=True)
        st.session_state["detection_thread"].start()
        st.success("✅ Face detection started!")

# Stop Detection
def stop():
    stop_detection()  # Stop detection thread
    st.warning("⛔ Face detection stopped!")

# Assign unique keys to prevent DuplicateWidgetID error
st.button("Start Detection", on_click=start, key="start_button")
st.button("Stop Detection", on_click=stop, key="stop_button")

st.info("Press **Start Detection** to begin monitoring. Press **Stop Detection** to stop.")
