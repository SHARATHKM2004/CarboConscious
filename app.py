import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import random
from datetime import datetime

# Define emission factors (example values, replace with accurate data)
class CarbonOffsetMarketplace:
    def __init__(self):
        self.projects = pd.DataFrame({
            'Project': ['Reforestation in Amazon', 'Wind Farm in Texas', 'Solar Panels in Africa', 'Methane Capture in Landfills'],
            'Cost per Ton CO2': [15, 20, 18, 22],
            'Available Tons': [1000, 2000, 1500, 800]
        })
        if 'user_offsets' not in st.session_state:
            st.session_state.user_offsets = 0

    def display_marketplace(self):
        st.title("Carbon Offset Marketplace")
        st.write("Browse and purchase carbon offsets to neutralize your emissions:")
        selected_project = st.selectbox(
            "Choose a carbon offset project:",
            options=self.projects['Project'].tolist()
        )
        
        # Display details of the selected project
        if selected_project:
            project_details = self.projects[self.projects['Project'] == selected_project].iloc[0]
            st.write(f"Selected Project: {selected_project}")
            st.write(f"Cost per Ton CO2: ${project_details['Cost per Ton CO2']}")
            st.write(f"Available Tons: {project_details['Available Tons']}")
            
            # Add a button to purchase offsets
            tons_to_purchase = st.number_input("Enter the number of tons to purchase:", min_value=1, max_value=project_details['Available Tons'], value=1)
            if st.button("Purchase Offsets"):
                total_cost = tons_to_purchase * project_details['Cost per Ton CO2']
                st.success(f"You've purchased {tons_to_purchase} tons of carbon offsets for ${total_cost}!")
        for _, project in self.projects.iterrows():
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"{project['Project']}")
class EducationHub:
    def __init__(self):  # Correct constructor definition
        self.articles = [
            {
                'title': 'Understanding Carbon Footprint',
                'content': 'A carbon footprint is the total amount of greenhouse gases...',
                'category': 'Basics'
            },
            {
                'title': 'The Impact of Fast Fashion on Climate Change',
                'content': 'Fast fashion contributes significantly to global carbon emissions...',
                'category': 'Lifestyle'
            },
            {
                'title': 'Renewable Energy: The Future of Power',
                'content': 'Renewable energy sources like solar and wind are becoming increasingly...',
                'category': 'Technology'
            }
        ]
        self.videos = [
            {
                   'title': 'How to Reduce Your Carbon Footprint',
                'url': 'https://youtu.be/ma-16mYsilA?si=1X4Gd9T-g3fKlFpO',
                'category': 'Practical Tips'
            },
            {
                'title': 'The Science of Climate Change Explained',
                'url': 'https://youtu.be/k0Kp5fwaEds?si=w5mS7_b0v0yUaPSg',
                'category': 'Science'
            }
        ]
        self.infographics = [
            {
                'title': 'Carbon Footprint of Common Foods',
                'image_url': 'https://www.google.com/imgres?q=%27https%3A%2F%2Fexample.com%2Ffood_carbon_footprint.jp&imgurl=https%3A%2F%2F8billiontrees.com%2Fwp-content%2Fuploads%2F2021%2F06%2Ffood-carbon-footprint-calculator-diet-emissions.png&imgrefurl=https%3A%2F%2F8billiontrees.com%2Fcarbon-offsets-credits%2Fcarbon-ecological-footprint-calculators%2Ffood%2F&docid=cHXvBwRMjNgW5M&tbnid=EW3hKU0PekfGDM&vet=12ahUKEwier4n3-OOIAxXI8jgGHVc_AB4QM3oECBMQAA..i&w=1200&h=630&hcb=2&ved=2ahUKEwier4n3-OOIAxXI8jgGHVc_AB4QM3oECBMQAAg',
                'category': 'Diet'
            },
            {
                'title': 'Global Temperature Rise Over Time',
                'image_url': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fdecarbonization.visualcapitalist.com%2Fmapped-global-temperature-rise-by-country%2F&psig=AOvVaw1IMTcpzFFwX6vaI44appwu&ust=1727554753211000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNDvq4z544gDFQAAAAAdAAAAABAE',
                'category': 'Climate Data'
            }
        ]

    def display_hub(self):
        st.title("Sustainability Education Hub")
        
        tab1, tab2, tab3, tab4 = st.tabs(["Articles", "Videos", "Infographics", "Quiz"])
        
        with tab1:
            st.subheader("Articles")
            for article in self.articles:
                with st.expander(article['title']):
                    st.write(article['content'])
                    st.caption(f"Category: {article['category']}")
        
        with tab2:
            st.subheader("Educational Videos")
            for video in self.videos:
                st.video(video['url'])
                st.caption(f"{video['title']} | Category: {video['category']}")
        
        with tab3:
            st.subheader("Infographics")
            for infographic in self.infographics:
                st.image(infographic['image_url'], caption=infographic['title'])
                st.caption(f"Category: {infographic['category']}")
        
        with tab4:
            st.subheader("Sustainability Quiz")
            self.display_quiz()

    def display_quiz(self):
        questions = [
            {
                'question': 'What is the main greenhouse gas responsible for climate change?',
                'options': ['Carbon Dioxide', 'Methane', 'Water Vapor', 'Ozone'],
                'correct_answer': 'Carbon Dioxide'
            },
            {
                'question': 'Which of the following is a renewable energy source?',
                'options': ['Coal', 'Natural Gas', 'Solar', 'Oil'],
                'correct_answer': 'Solar'
            },
            {
                'question': 'What percentage of Earth\'s surface is covered by water?',
                'options': ['50%', '60%', '70%', '80%'],
                'correct_answer': '70%'
            }
        ]
        for question in questions:
            st.write(question['question'])
            user_answer = st.radio('Options', question['options'], key=question['question'])
            if st.button('Submit', key=f"submit_{question['question']}"):
                if user_answer == question['correct_answer']:
                    st.success("Correct!")
                else:
                    st.error(f"Incorrect! The correct answer is: {question['correct_answer']}")

        if 'quiz_score' not in st.session_state:
            st.session_state.quiz_score = 0
            st.session_state.quiz_total = len(questions)
            st.session_state.current_question = 0
            random.shuffle(questions)

        if st.session_state.current_question < len(questions):
            question = questions[st.session_state.current_question]
            st.write(question['question'])
            user_answer = st.radio('Choose your answer:', question['options'], key=f"q{st.session_state.current_question}")
            
            if st.button('Submit Answer'):
                if user_answer == question['correct_answer']:
                    st.session_state.quiz_score += 1
                    st.success('Correct!')
                else:
                    st.error(f'Incorrect. The correct answer is {question["correct_answer"]}.')
                st.session_state.current_question += 1
                st.experimental_rerun()
        else:
            st.write(f"Quiz completed! Your score: {st.session_state.quiz_score}/{st.session_state.quiz_total}")
            if st.button('Retake Quiz'):
                st.session_state.quiz_score = 0
                st.session_state.current_question = 0
                random.shuffle(questions)
                st.experimental_rerun
class Clubs:
    def __init__(self):
        # Properly initialize the 'clubs' attribute
        self.clubs = [
            {'name': 'Green Warriors', 'description': 'A club focused on planting trees and reforestation activities.'},
            {'name': 'Eco Innovators', 'description': 'A club focused on sustainable technology and eco-friendly innovation.'},
            {'name': 'Waste Reducers', 'description': 'This club encourages reducing waste and recycling in creative ways.'},
            {'name': 'Clean Energy Enthusiasts', 'description': 'A club for promoting clean and renewable energy sources.'},
            {'name': 'Carbon Trackers', 'description': 'A club focused on monitoring and reducing carbon footprints.'},
            {'name': 'Sustainable Living Advocates', 'description': 'A club for those who adopt sustainable living practices.'},
            {'name': 'Ocean Savers', 'description': 'A club dedicated to saving oceans and promoting marine life sustainability.'},
            {'name': 'Zero Waste Champions', 'description': 'A club focused on zero waste lifestyle and practices.'},
            {'name': 'Plastic-Free Pioneers', 'description': 'A club working towards eliminating plastic from daily life.'},
            {'name': 'Climate Action Network', 'description': 'A club dedicated to taking climate action at the community level.'}
        ]
        self.user_clubs = []

    def display_clubs(self):
        st.title("Join a Sustainability Club")
        st.write("Explore the various clubs focused on sustainability and eco-friendly practices. Join a club to participate in activities and discussions!")

        for club in self.clubs:
            with st.expander(club['name']):
                st.write(club['description'])
                if club['name'] in self.user_clubs:
                    st.button("Joined", disabled=True)
                else:
                    if st.button(f"Join {club['name']}"):
                        self.user_clubs.append(club['name'])
                        st.success(f"You've successfully joined {club['name']}!")

        # Display the clubs the user has already joined
        if self.user_clubs:
            st.subheader("Your Clubs")
            for club in self.user_clubs:
                st.write(f"✅ {club}")
class EcoMarket:
    def __init__(self):
        self.products = [
            {"id": 1, "name": "Reusable Water Bottle", "price": 15, "description": "Stainless steel, BPA-free bottle", "image": r"C:\Users\shara\OneDrive\Pictures\Screenshots\Screenshot 2024-09-28 033818.png"},
            {"id": 2, "name": "Bamboo Toothbrush Set", "price": 10, "description": "Pack of 4 biodegradable toothbrushes", "image": r"C:\Users\shara\OneDrive\Pictures\Screenshots\Screenshot 2024-09-28 034029.png"},
            {"id": 3, "name": "Solar Power Bank", "price": 35, "description": "10000mAh solar-powered charger", "image": r"C:\Users\shara\OneDrive\Pictures\Screenshots\Screenshot 2024-09-28 034215.png"},
            {"id": 4, "name": "Reusable Grocery Bags", "price": 12, "description": "Set of 5 durable shopping bags", "image": r"C:\Users\shara\OneDrive\Pictures\Screenshots\Screenshot 2024-09-28 034325.png"},
            {"id": 5, "name": "Beeswax Food Wraps", "price": 18, "description": "Eco-friendly alternative to plastic wrap", "image": r"C:\Users\shara\OneDrive\Pictures\Screenshots\Screenshot 2024-09-28 034430.png"},
            {"id": 6, "name": "Bamboo Cutlery Set", "price": 20, "description": "Portable utensils for on-the-go", "image": r"C:\Users\shara\OneDrive\Pictures\Screenshots\Screenshot 2024-09-28 034535.png"},
            {"id": 7, "name": "Recycled Paper Notebook", "price": 8, "description": "100% recycled paper journal", "image": r"C:\Users\shara\Onedrive\Pictures\Screenshots\Screenshot 2024-09-28 034706.png"},
            {"id": 8, "name": "Eco-friendly Yoga Mat", "price": 40, "description": "Made from natural rubber and recycled materials", "image": r"C:\Users\shara\OneDrive\Pictures\Screenshots\Screenshot 2024-09-28 034815.png"},
            {"id": 9, "name": "Biodegradable Phone Case", "price": 25, "description": "Compostable phone protection", "image": r"C:\Users\shara\OneDrive\Pictures\Screenshots\Screenshot 2024-09-28 034922.png"},
            {"id": 10, "name": "Solar-powered Garden Lights", "price": 30, "description": "Set of 4 outdoor solar lights", "image": r"C:\Users\shara\OneDrive\Pictures\Screenshots\Screenshot 2024-09-28 035021.png"},

        ]
        if 'cart' not in st.session_state:
            st.session_state.cart = {}
        if 'wishlist' not in st.session_state:
            st.session_state.wishlist = set()

    def add_to_cart(self, product_id):
        if product_id in st.session_state.cart:
            st.session_state.cart[product_id] += 1
        else:
            st.session_state.cart[product_id] = 1
        st.success(f"Added to cart!")

    def remove_from_cart(self, product_id):
        if product_id in st.session_state.cart:
            if st.session_state.cart[product_id] > 1:
                st.session_state.cart[product_id] -= 1
            else:
                del st.session_state.cart[product_id]
        st.success(f"Removed from cart!")

    def toggle_wishlist(self, product_id):
        if product_id in st.session_state.wishlist:
            st.session_state.wishlist.remove(product_id)
            st.success(f"Removed from wishlist!")
        else:
            st.session_state.wishlist.add(product_id)
            st.success(f"Added to wishlist!")

    def display_products(self):
        st.title("🌿 Eco Market")
        st.write("Browse our selection of eco-friendly products to reduce your carbon footprint!")

        # Display products in a grid
        cols = st.columns(2)
        for idx, product in enumerate(self.products):
            with cols[idx % 2]:
                st.image(product['image'], use_column_width=True)
                st.subheader(product['name'])
                st.write(product['description'])
                st.write(f"Price: ${product['price']}")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"🛒 Add to Cart", key=f"add_{product['id']}"):
                        self.add_to_cart(product['id'])
                with col2:
                    if st.button(f"{'❤' if product['id'] in st.session_state.wishlist else '🤍'} Wishlist", key=f"wish_{product['id']}"):
                        self.toggle_wishlist(product['id'])
                st.write("---")

    def display_cart(self):
        st.sidebar.title("🛒 Your Cart")
        total = 0
        for product_id, quantity in st.session_state.cart.items():
            product = next((p for p in self.products if p['id'] == product_id), None)
            if product:
                st.sidebar.write(f"{product['name']} (x{quantity}): ${product['price'] * quantity}")
                total += product['price'] * quantity
                if st.sidebar.button(f"Remove", key=f"remove_{product_id}"):
                    self.remove_from_cart(product_id)
        st.sidebar.write(f"Total: ${total}")
        if st.sidebar.button("Checkout"):
            st.sidebar.success("Thank you for your purchase! Your eco-friendly products will be shipped soon.")
            st.session_state.cart = {}

    def display_wishlist(self):
        st.sidebar.title("❤ Your Wishlist")
        for product_id in st.session_state.wishlist:
            product = next((p for p in self.products if p['id'] == product_id), None)
            if product:
                st.sidebar.write(f"{product['name']} - ${product['price']}")
                if st.sidebar.button(f"Add to Cart", key=f"wishlist_add_{product_id}"):
                    self.add_to_cart(product_id)
                    st.sidebar.success(f"Added {product['name']} to cart!")

    def display_market(self):
        self.display_products()
        self.display_cart()
        self.display_wishlist()



marketplace = CarbonOffsetMarketplace()
# Initialize the Education Hub
education_hub = EducationHub()
 # Add more details and functionality as needed
clubs = Clubs()
EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal
        "Waste": 0.1,  # kgCO2/kg
        "Internet": 0.0005,  # kgCO2/byte
        "Fossil Fuels": 2.5,  # kgCO2/litre
        "Other": 0.1  # kgCO2/other
    },
    "USA": {
        "Transportation": 0.10,  # kgCO2/km
        "Electricity": 0.45,  # kgCO2/kWh
        "Diet": 1.5,  # kgCO2/meal
        "Waste": 0.12,  # kgCO2/kg
        "Internet": 0.0004,  # kgCO2/byte
        "Fossil Fuels": 2.7,  # kgCO2/litre
        "Other": 0.15  # kgCO2/other
    },
    "China": {
        "Transportation": 0.20,  # kgCO2/km
        "Electricity": 0.62,  # kgCO2/kWh
        "Diet": 1.0,  # kgCO2/meal
        "Waste": 0.09,  # kgCO2/kg
        "Internet": 0.0006,  
        "Fossil Fuels": 2.2,  
        "Other": 0.12  
    },
}
if "users" not in st.session_state:
    st.session_state["users"] = []  

# Set page config for the app
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")
import base64

def display_title_with_logo(title, logo_path, logo_width):
    """
    Display the title with the logo beside it.

    Parameters:
    - title (str): The title text.
    - logo_path (str): Path to the logo image (can be a URL or local path).
    - logo_width (int): Width of the logo image.
    """
    # Read and encode the logo image in base64
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()

    # Display title and logo side by side
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; gap: 10px;">
            <h1 style="margin: 0;">{title}</h1>
            <img src="data:image/png;base64,{encoded_logo}" alt="Logo" style="width: {logo_width}px;">
        </div>
        """,
        unsafe_allow_html=True
    )

# Example usage: Replace with the actual path to your logo image
display_title_with_logo("CarboConscious ", r"C:\Users\shara\Downloads\Mind_Treas.png", 300)

# Add other elements of your Streamlit app
st.write("Welcome to the app! More content goes here...")
# Add custom CSS to style the app more explicitly for visibility
st.markdown(
    """
    <style>
    body {
        background-color: white;
        color: black;
    }
    .stApp {
        background-color: white;
        color: black;
    }
    .stTextInput, .stNumberInput, .stSelectbox, .stSlider, .stButton, .stMarkdown, .stTitle, .stHeader, .stSubheader, .stCaption, .stCode {
        font-weight: bold !important;
        background-color: white !important;
    }
    .css-1aumxhk, .css-qrbaxs, .css-17eq0hr, .css-1v3fvcr, .css-16huue1, .css-1avcm0n, .css-1cpxqw2 {
        color: black !important;
        font-weight: bold !important;
        background-color: white !important;
        border-radius: 5px !important;
        padding: 5px !important;
    }
    .css-1q8dd3e p, .css-1q8dd3e div {
        color: black !important;
    }
    .css-1aumxhk svg {
        color: black !important;
        fill: white !important;
    }
    .css-1avcm0n svg {
        fill: white !important;
    }
    .stSlider > div:first-child, .stNumberInput > div:first-child {
        color: white !important;
    }
    .stNumberInput, .stSlider {
        background-color: white !important;
        border: 2px solid black !important;
        border-radius: 5px !important;
        padding: 10px !important;
    }
   /* Style for Number Input Fields */
    .stNumberInput input {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
        border-radius: 4px !important;
    }
    
    /* Style for Sliders */
    .stSlider > div > div > div > div > div {
        background: #f0f0f0 !important; /* Background of slider track */
    }
    .stSlider > div > div > div > div > div > div {
        background-color: #ffffff !important; /* Handle and other inner elements */
    }

    /* Style for Text Inputs (if any) */
    input[type="text"] {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
        border-radius: 4px !important;
    }

    /* General adjustments for all inputs */
    input:focus, .stNumberInput input:focus {
        outline: none !important;
        box-shadow: none !important;
        border-color: #888 !important; /* Focus border color */
    }
    .stButton > button {
        background-color: white !important;
        color: white !important;
        border: 2px solid black !important;
        padding: 8px 12px !important;
        font-size: 18px !important;
        border-radius: 8px !important;
    }
    .stButton > button:hover {
        background-color: #444 !important;
        color: white !important;
        border: 2px solid black !important;
    }
    h1, h2, h3, h4, h5, h6, p, label, span, div, input, select, button {
        color: black !important;
    }

    /* Apply white background and black text to selectbox */
    div[data-baseweb="select"] {
        background-color: white !important;
        color: black !important;
        border: 2px solid black !important;
        border-radius: 5px !important;
        padding: 5px !important;
    }
     /* Ensure the text inside the selectbox dropdown is visible */
   div[data-baseweb="submit_button"] > div {  
   color: white !important;  
   background-color: white !important;  
    }
    .stButton > button[type="submit"] {  
    background-color: white !important;  
    color: black !important;  
    border: 2px solid black !important;  
    padding: 8px 12px !important;  
    font-size: 18px !important;  
    border-radius: 8px !important;  
    }

    /* Ensure the text inside the selectbox dropdown is visible */
    div[data-baseweb="select"] > div {
        color: white !important;
        background-color: white !important;
    }

    /* Style the dropdown items */
    div[data-baseweb="menu"] {
        background-color: white !important;
        color: white !important;
        
    
    }
    </style>
    """,
    unsafe_allow_html=True
)
def get_leaderboard():
    # Sort users by footprint to display on leaderboard
    return sorted(st.session_state["users"], key=lambda x: x["footprint"])


# Create a sidebar menu using option_menu
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "About", "Settings", "Gamification Mode", "Leaderboard", "Challenges", "Carbon Offset","Education","🌿 Eco Market","Clubs","Contact"],
        icons=["house", "info-circle", "gear", "trophy","info-circle","list-ol", "users","book","leaf","phone","envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            # ... (keep your existing styles)
    
            "container": {"padding": "0!important", "background-color": "#ffffff"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {
                "font-size": "18px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
                "color": "black",
            },
            "nav-link-selected": {"background-color": "#e0e0e0"},
        }
    )

    
if selected == "Gamification Mode":
    st.title("Gamification Mode: Track and Share Your Progress!")
    
    # Input form for username and carbon footprint
    with st.form("footprint_form"):
        username = st.text_input("Enter your username:")  # Get username input
        footprint = st.number_input("Enter your carbon footprint (in kg):", min_value=0.0)  # Get footprint input
        submit_button = st.form_submit_button("Submit")  # Submit button for the form
        st.markdown(
        """
        <style>
        button[type="submit"] {
            background-color: white !important; /* Set background to white */
            color: black !important;            /* Set text color to black */
            border: 1px solid #ccc !important;  /* Optional: Add a border */
            padding: 0.5em 1em !important;      /* Adjust padding */
            font-size: 16px !important;         /* Adjust font size */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    if submit_button and username and footprint > 0:
        # Append the new user data to the session state
        st.session_state["users"].append({"name": username, "footprint": footprint})
        st.success(f"User {username} with a footprint of {footprint} kg added to the leaderboard!")
    elif selected == "Leaderboard":
      st.title("Leaderboard: Compare Your Progress with Others!")
     # Check if there are any users in session state before displaying the leaderboard
    if st.session_state["users"]:
        leaderboard = get_leaderboard()  # Get sorted leaderboard data
        leaderboard_df = pd.DataFrame(leaderboard)  # Convert to DataFrame for display
        st.dataframe(leaderboard_df.style.set_table_attributes('style="color: black;"'))  # Set text color to black
    else:
        st.write("No users have been added yet.")  # Message if no users are present
    st.markdown("### Share your achievements:")
    # Share via Social Media buttons with icons
    st.markdown(
        """
        <style>
        .share-buttons {
            display: flex;
            justify-content: start;
        }
        .share-button img {
            width: 40px;
            height: 40px;
            margin-right: 15px;
        }
        </style>
        <div class="share-buttons">
            <a href="https://www.facebook.com/sharer/sharer.php?u=https://yourapp.com" target="_blank" class="share-button">
                <img src="https://cdn-icons-png.flaticon.com/512/124/124010.png" alt="Facebook" />
            </a>
            <a href="https://twitter.com/intent/tweet?text=I%20am%20reducing%20my%20carbon%20footprint!&url=https://yourapp.com" target="_blank" class="share-button">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="Twitter" />
            </a>
            <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://yourapp.com" target="_blank" class="share-button">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" />
            </a>
            <a href="https://api.whatsapp.com/send?text=Check%20out%20my%20carbon%20footprint%20progress!%20https://yourapp.com" target="_blank" class="share-button">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" alt="WhatsApp" />
            </a>
            <a href="mailto:?subject=My%20Carbon%20Footprint%20Progress&body=I%20am%20reducing%20my%20carbon%20footprint!%20Check%20it%20out%20at%20https://yourapp.com" class="share-button">
                <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="Email" />
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Collapsible Share Button with options
    if st.button("🔗 Share ➡️"):
        st.markdown("""
        **Share via:**
        
        - [Facebook](https://www.facebook.com/sharer/sharer.php?u=https://yourapp.com)
        - [Twitter](https://twitter.com/intent/tweet?text=I%20am%20reducing%20my%20carbon%20footprint%20by%20using%20this%20app!&url=https://yourapp.com)
        - [LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https://yourapp.com)
        - [WhatsApp](https://api.whatsapp.com/send?text=I%20am%20reducing%20my%20carbon%20footprint%20by%20using%20this%20app!%20https://yourapp.com)
        - [Email](mailto:?subject=My%20Carbon%20Footprint%20Progress&body=I%20am%20reducing%20my%20carbon%20footprint!%20Check%20it%20out%20at%20https://yourapp.com)
        """)
# Leaderboard page
elif selected == "Leaderboard":
    st.title("Leaderboard: Compare Your Progress with Others!")
    
    if st.session_state["users"]:
        leaderboard = get_leaderboard()
        leaderboard_df = pd.DataFrame(leaderboard)


        # Display the styled dataframe
        st.write(styled_leaderboard_df.to_html(), unsafe_allow_html=True)
    else:
        st.write("No users have been added yet.")
# Helper functions for quizzes
def get_quiz_questions(challenge):
    questions = {
        "30-Day Vegan Challenge": [
            {
                "question": "Which of the following foods is not vegan?",
                "options": ["Tofu", "Quinoa", "Honey", "Lentils"],
                "correct_answer": "Honey"
            },
            {
                "question": "Approximately how much water is saved by not eating one pound of beef?",
                "options": ["500 gallons", "1,000 gallons", "2,000 gallons", "5,000 gallons"],
                "correct_answer": "2,000 gallons"
            },
            {
                "question": "Which nutrient might vegans need to supplement in their diet?",
                "options": ["Vitamin C", "Vitamin B12", "Vitamin A", "Vitamin E"],
                "correct_answer": "Vitamin B12"
            }
        ],
        "Zero-Waste Week": [
            {
                "question": "Which of the following is NOT a principle of zero waste?",
                "options": ["Refuse", "Reduce", "Recycle", "Incinerate"],
                "correct_answer": "Incinerate"
            },
            {
                "question": "What percentage of plastic waste has been recycled globally?",
                "options": ["9%", "25%", "50%", "75%"],
                "correct_answer": "9%"
            },
            {
                "question": "Which material takes the longest to decompose in a landfill?",
                "options": ["Paper", "Aluminum can", "Plastic bottle", "Glass bottle"],
                "correct_answer": "Glass bottle"
            }
        ],
        "Bike to Work Month": [
            {
                "question": "On average, how many grams of CO2 does a car emit per kilometer?",
                "options": ["50 grams", "120 grams", "200 grams", "300 grams"],
                "correct_answer": "120 grams"
            },
            {
                "question": "What percentage of carbon emissions in a typical US city come from transportation?",
                "options": ["10%", "20%", "30%", "40%"],
                "correct_answer": "30%"
            },
            {
                "question": "How many calories does an average person burn biking for 30 minutes at a moderate pace?",
                "options": ["100 calories", "200 calories", "300 calories", "400 calories"],
                "correct_answer": "300 calories"
            }
        ],
        "Energy Saver Sprint": [
            {
                "question": "Which appliance typically uses the most energy in a household?",
                "options": ["Refrigerator", "Air conditioner", "Water heater", "Washing machine"],
                "correct_answer": "Air conditioner"
            },
            {
                "question": "What percentage of a home's energy use does lighting typically account for?",
                "options": ["5%", "10%", "15%", "20%"],
                "correct_answer": "15%"
            },
            {
                "question": "Which of these light bulb types is the most energy-efficient?",
                "options": ["Incandescent", "CFL", "LED", "Halogen"],
                "correct_answer": "LED"
            }
        ]
    }
    return questions.get(challenge, [
        {
            "question": "What is the primary greenhouse gas responsible for global warming?",
            "options": ["Carbon Dioxide", "Methane", "Water Vapor", "Ozone"],
            "correct_answer": "Carbon Dioxide"
        }
    ])

def take_quiz(questions):
    score = 0
    for q in questions:
        answer = st.radio(q["question"], q["options"])
        if answer == q["correct_answer"]:
            score += 1
    return (score / len(questions)) * 100

def calculate_progress(quiz_scores):
    if not quiz_scores:
        return 0
    return sum(quiz_scores) / len(quiz_scores)

# Main Streamlit app code
if selected == "Challenges":
    st.title("Community Challenges: Join a Team or Take a Challenge!")
    
    # Initialize session state for joined challenges and quiz scores if they don't exist
    if 'joined_challenges' not in st.session_state:
        st.session_state.joined_challenges = {}
    if 'quiz_scores' not in st.session_state:
        st.session_state.quiz_scores = {}

    # Display current challenge
    st.subheader("🏆 Current Challenge: Reduce 1000 kg of CO2 in 30 days as a team!")
    
    # Progress bar for the current challenge
    team_progress = 650  # This would be dynamically updated in a real app
    st.progress(team_progress / 1000)
    st.write(f"Team Progress: {team_progress} kg / 1000 kg")
    
    # Option to join a challenge or team
    st.write("You can join a challenge or team and compete to reduce the most carbon emissions.")
    if st.button("Join Challenge", key="join_main_challenge"):
        st.success("You have successfully joined the challenge!")
        st.balloons()
    
    # List of available challenges
    st.subheader("📋 Available Challenges")
    challenges = [
        {"name": "30-Day Vegan Challenge", "difficulty": "Medium", "impact": "High"},
        {"name": "Zero-Waste Week", "difficulty": "Hard", "impact": "Very High"},
        {"name": "Bike to Work Month", "difficulty": "Easy", "impact": "Medium"},
        {"name": "Energy Saver Sprint", "difficulty": "Easy", "impact": "Medium"},
    ]
    
    for i, challenge in enumerate(challenges):
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        with col1:
            st.write(f"{challenge['name']}")
        with col2:
            st.write(f"Difficulty: {challenge['difficulty']}")
        with col3:
            st.write(f"Impact: {challenge['impact']}")
        with col4:
            if challenge['name'] not in st.session_state.joined_challenges:
                if st.button(f"Join", key=f"join_challenge_{i}"):
                    st.session_state.joined_challenges[challenge['name']] = 0
                    st.session_state.quiz_scores[challenge['name']] = []
                    st.success(f"You've joined the {challenge['name']}!")
            else:
                st.write("Joined")
    
    # Personal challenge tracker with quizzes
    st.subheader("🎯 Your Active Challenges")
    if st.session_state.joined_challenges:
        for challenge, progress in st.session_state.joined_challenges.items():
            st.write(f"{challenge}")
            
            # Quiz section
            if st.button(f"Take Quiz for {challenge}", key=f"quiz_{challenge}"):
                quiz_questions = get_quiz_questions(challenge)
                quiz_score = take_quiz(quiz_questions)
                st.session_state.quiz_scores[challenge].append(quiz_score)
                
                # Update progress based on quiz score
                progress = calculate_progress(st.session_state.quiz_scores[challenge])
                st.session_state.joined_challenges[challenge] = progress
            
            st.progress(progress / 100)
            st.write(f"Progress: {progress}%")
            
            if st.session_state.quiz_scores[challenge]:
                st.write(f"Latest Quiz Score: {st.session_state.quiz_scores[challenge][-1]}%")
    else:
        st.write("You haven't joined any challenges yet. Join a challenge to start taking quizzes and tracking your progress!")
    
    # Leaderboard for the current challenge
    st.subheader("🏅 Challenge Leaderboard")
    leaderboard_data = {
        "Team": ["Green Warriors", "EcoHeroes", "Carbon Cutters", "Planet Savers", "Your Team"],
        "CO2 Reduced (kg)": [800, 750, 700, 680, 650]
    }
    leaderboard_df = pd.DataFrame(leaderboard_data)
    st.table(leaderboard_df)
    
    # Tips for succeeding in challenges
    st.subheader("💡 Tips for Challenge Success")
    st.info("""
    1. Set realistic goals for yourself.
    2. Track your progress daily.
    3. Share your journey on social media for accountability.
    4. Team up with friends or family for motivation.
    5. Celebrate small victories along the way!
    6. Take quizzes regularly to boost your knowledge and progress!
    """)
    
    # Option to create a custom challenge
    st.subheader("🆕 Create Your Own Challenge")
    custom_challenge_name = st.text_input("Challenge Name")
    custom_challenge_duration = st.slider("Challenge Duration (days)", 1, 90, 30)
    custom_challenge_goal = st.number_input("CO2 Reduction Goal (kg)", min_value=1)
    
    if st.button("Create Custom Challenge", key="create_custom_challenge"):
        if custom_challenge_name:
            st.session_state.joined_challenges[custom_challenge_name] = 0
            st.session_state.quiz_scores[custom_challenge_name] = []
            st.success(f"Custom challenge '{custom_challenge_name}' created and joined successfully!")
            st.write(f"Duration: {custom_challenge_duration} days")
            st.write(f"Goal: Reduce {custom_challenge_goal} kg of CO2")
        else:
            st.warning("Please enter a name for your custom challenge.")
        
    
if selected == "Home":
    st.title("CARBON FOOTPRINT CALCULATOR")
    st.subheader("Smart AI for Carbon Conscious Living ⚠")

    # User inputs
    country = st.selectbox("🌍 Your Country", ["India", "USA","China"])

    col1, col2 = st.columns(2)

    with col1:
        distance = st.slider("🚗 Daily commute distance (in km)", 0.0, 100.0)
        electricity = st.slider("💡 Monthly electricity consumption (in kWh)", 0.0, 1000.0)
        internet_usage = st.number_input("🌐 Internet usage (in bytes)", 0, 1000000000)  # Up to 1 GB for example

    with col2:
        waste = st.slider("🍽 Waste generated per week (in kg)", 0.0, 100.0)
        meals = st.number_input("🍽 Number of meals per day", 0, 10)
        fossil_fuels = st.number_input("⛽ Fossil fuels used (in litres)", 0.0, 1000.0)
    # Normalize inputs
    distance *= 365
    electricity *= 12
    meals *= 365
    waste *= 52
    internet_usage = internet_usage  # Use as is
    fossil_fuels = fossil_fuels  # Use as is
    

    # Calculate emissions
    transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance / 1000
    electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity / 1000
    diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals / 1000
    waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste / 1000
    internet_emissions = EMISSION_FACTORS[country]["Internet"] * internet_usage / 1000000000  # Assuming bytes
    fossil_fuels_emissions = EMISSION_FACTORS[country]["Fossil Fuels"] * fossil_fuels  # Direct count
    total_emissions = round(transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2)
    if st.button("Calculate CO2 Emissions"):
        # Display results
        st.header("Results")
        col3, col4 = st.columns(2)

        with col3:
            st.subheader("Carbon Emissions by Category")
            st.info(f"🚗 Transportation: {transportation_emissions:.2f} tonnes CO2 per year")
            st.info(f"💡 Electricity: {electricity_emissions:.2f} tonnes CO2 per year")
            st.info(f"🍽 Diet: {diet_emissions:.2f} tonnes CO2 per year")
            st.info(f"🗑 Waste: {waste_emissions:.2f} tonnes CO2 per year")  
            st.info(f"🌐 Internet Usage: {internet_emissions:.2f} tonnes CO2 per year")
            st.info(f"⛽ Fossil Fuels: {fossil_fuels_emissions:.2f} tonnes CO2 per year")
        with col4:
            st.subheader("Total Carbon Footprint")
            st.success(f"🌍 Your total carbon footprint is: {total_emissions:.2f} tonnes CO2 per year")
        
        # Pie chart for emissions breakdown
        labels = ['Transportation', 'Electricity', 'Diet', 'Waste','Internet Usage','Fossil Fuels']
        values = [transportation_emissions, electricity_emissions, diet_emissions, waste_emissions, internet_emissions,fossil_fuels_emissions]
        pie_fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        pie_fig.update_layout(title_text='Carbon Emissions Breakdown by Category')
        st.plotly_chart(pie_fig)

        # New: Bar chart for emissions over different time periods
        st.subheader("Emissions Breakdown by Time Period")
        
        time_period = st.radio("Select time period:", ["Monthly"])

        if time_period == "Monthly":
            time_factor = 12
        else:
            time_factor = 1

        # Calculate emissions for the selected time period
        emissions_data = {
            "Category": ['Transportation', 'Electricity', 'Diet', 'Waste','Internet Usage','Fossil Fuels'],
            "CO2 Emissions (tonnes)": [
                transportation_emissions / time_factor,
                electricity_emissions / time_factor,
                diet_emissions / time_factor,
                waste_emissions / time_factor,
                internet_emissions/ time_factor,
                fossil_fuels_emissions/time_factor,          
 ]}

        # Create DataFrame and bar chart
        df = pd.DataFrame(emissions_data)
        bar_fig = go.Figure([go.Bar(x=df['Category'], y=df['CO2 Emissions (tonnes)'])])
        bar_fig.update_layout(title_text=f'CO2 Emissions ({time_period})', xaxis_title='Category', yaxis_title='CO2 Emissions (tonnes)')
        st.plotly_chart(bar_fig)
         # Badge based on total emissions
        if total_emissions <= 2.0:
            badge = "Platinum"
            st.balloons()  # Celebrate Platinum badge
        elif total_emissions <= 5.0:
            badge = "Gold"
            st.balloons()  # Celebrate Gold badge
        elif total_emissions <= 8.0:
            badge = "Silver"
            st.snow()  
            st.success("🎖 You've earned the Silver Badge! 😊")  # Happy face for Silver
        else:
            badge = "Bronze"
            st.warning("⚠️ Great job, but be cautious!😞")# Sad face for Bronze
            # Sad face for Bronze

        # Display badge
        st.success(f"🏅 You've earned the {badge} Badge!")
        # Dynamic suggestions based on emissions
        if transportation_emissions > 0.5:
            st.markdown("### Transportation Suggestions")
            st.write("- Consider using public transport or carpooling.")
            st.write("- Opt for fuel-efficient vehicles.")
        
        if electricity_emissions > 0.5:
            st.markdown("### Electricity Suggestions")
            st.write("- Use energy-efficient appliances.")
            st.write("- Switch to renewable energy sources.")
        
        if diet_emissions > 0.5:
            st.markdown("### Diet Suggestions")
            st.write("- Incorporate more plant-based meals.")
            st.write("- Support local food producers.")
        
        if waste_emissions > 0.1:
            st.markdown("### Waste Management Suggestions")
            st.write("- Implement a composting system.")
            st.write("- Recycle as much as possible.")
        internet_emissions = float(internet_emissions)
        if internet_emissions > 4:
            st.markdown("### Internet Usage Suggestions")
            st.write("- Reduce streaming quality when possible.")
            st.write("- Unsubscribe from unnecessary email lists.")
        if fossil_fuels_emissions > 0.05:
             st.markdown("### Fossil Fuel Reduction Suggestions")
             st.write("- Advocate for renewable energy policies.")
             st.write("- Invest in or support clean energy initiatives.")

      
if 'streak' not in st.session_state:
    st.session_state.streak = 0

if 'last_check_in' not in st.session_state:
    st.session_state.last_check_in = None
if 'streak' not in st.session_state:
    st.session_state.streak = 0

def daily_check_in():
    today = datetime.now().date()
    if st.session_state.last_check_in != today:
        st.session_state.streak += 1
        st.session_state.last_check_in = today
        st.success(f"Daily check-in successful! Streak: {st.session_state.streak} days")
    else:
        st.warning("You've already checked in today.")

# Adding to the app UI
st.subheader("Daily Check-in")
if st.button("Check-in"):
    daily_check_in()

st.write(f"Current Streak: {st.session_state.streak} days")

# Daily Check-in Reminder
if 'last_check_in' in st.session_state and st.session_state.last_check_in is not None:
    today = datetime.now().date()
    if st.session_state.last_check_in != today:
        st.warning("Reminder: Don't forget to check in today!")

# Suggested behaviors
suggested_behaviors = [
    "Use public transport instead of driving.",
    "Turn off lights when not in use.",
    "Reduce meat consumption this week.",
    "Use reusable bags instead of plastic.",
    "Try a no-waste grocery store.",
]

# Display a random suggestion
random_suggestion = random.choice(suggested_behaviors)
st.info(f"Suggestion for today: {random_suggestion}")
if selected == "Carbon Offset":
    marketplace.display_marketplace()
if selected == "Education":#education_hub = EducationHub()
    education_hub.display_hub()
elif selected == "Clubs":
    clubslubs=Clubs()
    clubs.display_clubs()
elif selected == "About":
    st.title("About This App")
    st.markdown("""
    **Personal Carbon Calculator** is an AI-powered app designed to help users track their carbon emissions 
    based on their daily activities such as transportation, electricity usage, diet, and waste generation. 
    The app provides personalized recommendations to help reduce carbon footprint and contribute to a more 
    sustainable planet.

    ### Key Features:
    - **Real-time Footprint Data**: Get instant calculations of your emissions.
    - **Personalized Recommendations**: Receive tailored suggestions on how to minimize your environmental impact.
    - **Gamification**: Earn badges for reducing your carbon footprint and share your achievements with friends.
    - **Carbon Offset**: Explore options to offset your emissions by participating in verified carbon offset programs.
    - **Interactive Visualizations**: Visualize your emissions breakdown through charts and graphs.
    - **Secure and User-Friendly**: Built with security and user experience in mind.

    ### How It Works:
    1. **Input Your Data**: Provide your daily/weekly/monthly data related to transportation, electricity, diet, and waste.
    2. **Calculate Your Emissions**: The app will use country-specific emission factors to compute your CO2 emissions.
    3. **Get Insights**: View your total carbon footprint, category-wise breakdown, and trends over time.
    4. **Take Action**: Use the recommendations to reduce your carbon impact and see how small changes can make a big difference.
    """)

    st.image("https://www.slidegeeks.com/media/catalog/product/cache/560x315/G/r/Green_Footprint_Vector_Icon_Ppt_PowerPoint_Presentation_Styles_Design_Ideas_Slide_1.jpg", caption="Reduce Your Carbon Footprint for a Sustainable Future")

    st.subheader("Credits")
    st.markdown("""
    - Developed by: Mind_Treasures
    - Data Sources: Publicly available carbon emission datasets.
    - Icons: [Streamlit Option Menu](https://github.com/victoryhb/streamlit-option-menu)
    """)
    education_hub.display_hub()
elif selected == "🌿 Eco Market":
    eco_market = EcoMarket()
    eco_market.display_market()
# Settings section content
elif selected == "Settings":
    st.title("Settings")
    st.markdown("Use the options below to customize your experience.")
    # Allow users to change country and save the preference
    country = st.selectbox("Select your country", ["India", "USA", "China"], index=0)
    st.success(f"Country set to {country}")

    # Add toggle for receiving notifications
    notifications = st.checkbox("Enable Notifications")
    if notifications:
        st.success("Notifications Enabled")
    else:
        st.warning("Notifications Disabled")

    # Dark mode toggle (CSS could be applied for this purpose)
    dark_mode = st.checkbox("Enable Dark Mode (Coming Soon)")
    if dark_mode:
        st.warning("Dark Mode is not yet supported.")
    
    # Option to reset user data (in a real app, this would clear saved data)
    if st.button("Reset All Data"):
        st.success("All user data has been reset.")
elif selected == "Contact":
    st.title("Contact")
    st.markdown("sahrathkm@gmail.com")