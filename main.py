import streamlit as st
from backend import get_data


st.title("Weather Forecast App")
location = st.text_input("City:")
days = st.slider("Forecast Days:", min_value=1, max_value=5,
                 help="Select how many days")
st.subheader(f"Forecast for the next {days} days in {location}")

if location:
    try:
        data = get_data(location, days)

        for date, daily_stats in data.items():
            st.header(f"Day {date}")
            st.markdown("<hr style='margin-top: -10px;'>", unsafe_allow_html=True)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.write("Time")
            with col3:
                st.write("Temperature")
            with col4:
                st.write("Feels like")
            with col5:
                st.write("Humidity")

            for day in daily_stats:
                col1, col2, col3, col4, col5 = st.columns(5)
                with col1:
                    st.write(day['time'])
                with col2:
                    st.image(day['image'], width=50)
                with col3:
                    st.write(f"{day['temperature']}°C")
                with col4:
                    st.write(f"{day['feels_like']}°C")
                with col5:
                    st.write(f"{day['humidity']}%")

    except KeyError as e:
        st.error("The City you entered is not found.")
