import streamlit as st
import datetime as dt

from predict_service_functions import predict_house_price

# Streamlit session state
if 'house_price' not in st.session_state:
    st.session_state.house_price = 0

# Variables
# The host where the price prediction service resides
yes_no_options = {
    'Yes': 1,
    'No': 0
}

room_size_options = {
    'Small': 0, 
    'Medium': 1, 
    'Large': 2, 
    'Extra large': 3
}

# Main function
def main():
    # Set browser tab title
    st.set_page_config(page_title="House price prediction app", menu_items=None, page_icon="random")

    # Set page title
    st.markdown('### House price prediction app')

    # Form title
    st.markdown('#### House features')

    # Create a container
    with st.container(border=True):
        # Create fields
        construction_date = st.number_input('Construction date', min_value=1900, step=1)
        land_size_sqm = st.number_input('Land size (sqm)', min_value=20, max_value=800, step=1)
        house_size_sqm = st.number_input('House size (sqm)', min_value=20, max_value=800, step=1)
        no_of_rooms = st.number_input('Number of rooms', min_value=1, max_value=100, step=1)
        no_of_bathrooms = st.number_input('Number of bathrooms', min_value=1, max_value=100, step=1)
        large_living_room = st.selectbox('Large living room', list(yes_no_options.keys()))
        parking_space = st.selectbox('Parking space', list(yes_no_options.keys()))
        front_garden = st.selectbox('Front garden', list(yes_no_options.keys()))
        swimming_pool = st.selectbox('Swimming pool', list(yes_no_options.keys()))
        wall_fence = st.selectbox('Wall fence', list(yes_no_options.keys()))
        water_front = st.selectbox('Water front', list(yes_no_options.keys()))
        room_size = st.selectbox('Room size', list(room_size_options.keys()))
        distance_to_school = st.number_input('Distance to school', min_value=0.1)
        distance_to_supermarket = st.number_input('Distance to supermarket', min_value=0.1)
        crime_rate_index = st.number_input('Crime rate index', min_value=0.1)
 
        # Create house dict
        # A sample house
        house = {
        'land_size_sqm': land_size_sqm,
        'house_size_sqm': house_size_sqm,
        'no_of_rooms': no_of_rooms,
        'no_of_bathrooms': no_of_bathrooms,
        'large_living_room': yes_no_options[large_living_room],
        'parking_space': yes_no_options[parking_space],
        'front_garden': yes_no_options[front_garden],
        'swimming_pool': yes_no_options[swimming_pool],
        'distance_to_school': distance_to_school,
        'wall_fence': yes_no_options[wall_fence],
        'house_age': dt.datetime.now().year - construction_date,
        'water_front': yes_no_options[water_front],
        'distance_to_supermarket': distance_to_supermarket,
        'crime_rate_index': crime_rate_index,
        'room_size': room_size_options[room_size]
        }

        # Create calculate price button
        calculate_price_clicked =  st.button('Calculate price')
        if calculate_price_clicked:
            # Get house price
            house_price = predict_house_price(house)
            # Store house price
            st.session_state.house_price =  house_price

        st.text_input('House price', disabled=True, value=st.session_state.house_price)

if __name__ == "__main__":
    main()