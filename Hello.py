# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.title("Welcome to Streamlit! 👋")
    st.header('BMI Calculator')

    weight = st.number_input('Enter your weight')
    height = st.number_input('Enter your height')
    st.write(f'Your weight is {weight} and your height is {height}.')
    if weight > 0 and height > 0:
      bmi = weight/((height*.01)**2)
      st.write(f'### Your BMI is {bmi:.2f}.')


if __name__ == "__main__":
    run()
