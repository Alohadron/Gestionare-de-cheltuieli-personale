import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.write("# We need a Plan!")



back = st.button("Back")


if back:
    switch_page("expence manager")
