import streamlit as st
import pandas as pd
import os
import base64
from Login.Username.Password.LoginInfo import USER_CREDENTIALS

try:
    import openpyxl
except ImportError:
    openpyxl = None

# === Page Settings ===
st.set_page_config(page_title="Proposal Generator", layout="wide")

# === LOGIN LOGIC WITH STYLING ===
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    # Logo
    st.markdown("""
        <div style='display: flex; flex-direction: column; align-items: center; margin-top: 30px;'>
            <img src='https://raw.githubusercontent.com/TaNeekwa/Flexgen-PG3x/main/FlexGen_Primary_Logo_-_Gradient.svg.png' width='300' style='margin-bottom: 40px;' />
        </div>
    """, unsafe_allow_html=True)

    # Login card wrapper
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
                <div style='display: flex; justify-content: center;'>
                    <div style='background-color: #111; padding: 6px 12px; border-radius: 10px; width: 100%; max-width: 320px; box-shadow: 0 3px 10px rgba(0,0,0,0.25);'>
                        <h4 style='color: white; text-align: center; margin: 4px 0;'>🔐 Login</h4>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # Add spacing below login title
            st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

            username = st.text_input("Username", placeholder="Enter username", label_visibility="collapsed", key="login_user_input")
            password = st.text_input("Password", type="password", placeholder="Enter password", label_visibility="collapsed", key="login_pass_input")

            login_clicked = st.button("Login", use_container_width=True)

            if login_clicked:
                if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Invalid username or password.")

            st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# === Sidebar: Theme Toggle ===
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

with st.sidebar:
    toggle_val = st.toggle("🌞 Light / 🌙 Dark", value=st.session_state.dark_mode)

    if toggle_val != st.session_state.dark_mode:
        st.session_state.dark_mode = toggle_val
        st.experimental_rerun()

    st.markdown("<hr style='border: 1px solid white; margin-top: 20px; margin-bottom: 20px;'>", unsafe_allow_html=True)

dark_mode = st.session_state.dark_mode

# === Divider Styling (used later) ===
divider_color = "#fff" if dark_mode else "#000"
st.markdown(f"<hr style='border: 1px solid {divider_color}; margin-top: 20px; margin-bottom: 20px;'>", unsafe_allow_html=True)

# === THEME STYLING ===
if dark_mode:
    css_theme = """<style>
    body, .stApp {
        background-color: #111 !important;
        color: white !important;
        font-family: 'Century Gothic', sans-serif !important;
    }
    h1, h2, h3, h4, p, label {
        color: white !important;
    }
    div.stButton > button,
    div.stButton > button span {
        color: white !important;
    }
    img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        padding-bottom: 10px;
    }
    .stTextInput > div > div > input,
    .stSelectbox > div,
    .stNumberInput > div > input,
    .stDateInput > div > input,
    .stTextArea > div > textarea,
    .stRadio > div > label,
    .stCheckbox > div {
        background-color: #222 !important;
        color: white !important;
        border: 1px solid white !important;
        border-radius: 4px !important;
    }
    div[data-baseweb="select"] * {
        color: white !important;
    }
    .stSelectbox:hover, .stTextInput:hover, .stNumberInput:hover {
        background-color: #333 !important;
    }
    .st-expander > summary {
        color: white !important;
    }
    </style>"""
else:
    css_theme = """<style>
    body, .stApp {
        background-color: #ffffff !important;
        color: #1a1a1a !important;
        font-family: 'Century Gothic', sans-serif !important;
    }
    h1, h2, h3, h4, p, label {
        color: #1a1a1a !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #1a1a1a !important;
        color: white !important;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    div.stButton > button {
        background-color: #111 !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 600 !important;
        border: 1px solid white !important;
        text-align: center !important;
    }
    div.stButton > button * {
        color: white !important;
    }
    div.stButton > button:hover {
        background-color: #333 !important;
        color: white !important;
    }
    .stTextInput > div > div > input,
    .stSelectbox > div,
    .stNumberInput > div > input,
    .stDateInput > div > input,
    .stTextArea > div > textarea,
    .stRadio > div > label,
    .stCheckbox > div {
        background-color: #ffffff !important;
        color: white !important;
        border: 1px solid #d9d9d9 !important;
        border-radius: 6px !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
    }
    div[data-baseweb="select"] * {
        color: white !important;
    }
    .stSelectbox:hover, .stTextInput:hover, .stNumberInput:hover {
        background-color: #f7f7f7 !important;
    }
    .st-expander > summary {
        color: #1a1a1a !important;
    }
    </style>"""

st.markdown(css_theme, unsafe_allow_html=True)

# === MAIN TITLE (only after login) ===
if st.session_state.authenticated:
    st.markdown("""
    <div style="text-align: center; padding-top: 10px;">
        <img src="https://raw.githubusercontent.com/TaNeekwa/Flexgen-PG3x/main/FlexGen_Primary_Logo_-_Gradient.svg.png" 
             alt="FlexGen Logo" width="300" />
        <h1 style="font-size: 42px; margin-top: 20px;">
            Proposal Generator 
        </h1>
        <p style="font-size: 18px;">Enter project details below to generate your custom proposal.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<hr style='border: 3px solid {divider_color}; margin-top: 20px; margin-bottom: 30px;'>", unsafe_allow_html=True)

   # === Proposal Type + Input Form Upload ===
col1, spacer, col2 = st.columns([2, 0.4, 3])  # Adjust layout as needed

with col1:
    st.markdown("### <strong>🧩 Proposal Type</strong>", unsafe_allow_html=True)
    proposal_type = st.selectbox(
        "",  # Hide default label
        ["EMS Proposal", "Full Product Proposal"],
        label_visibility="collapsed"
    )
    st.markdown(f"You selected: **{proposal_type}**")

    st.markdown("### <strong>👥 Business Development</strong>", unsafe_allow_html=True)
    bd_rep = st.selectbox("BD Representative", [
        "Jason Abiecunas", "Kody Calkins", "Don Harris", "JC, Reymond", "Other"
    ])

with col2:
    st.markdown("### <strong>📤 Upload Input Form (Excel)</strong>", unsafe_allow_html=True)
    uploaded_form = st.file_uploader(
        "",  # Hide default label
        type=["xlsx", "xlsm", "xls"],
        help="Drop the input form here to auto-fill fields.",
        label_visibility="collapsed"
    )

if uploaded_form:
    uploaded_form.seek(0)  # Reset pointer before reading
    try:
        excel_data = pd.ExcelFile(uploaded_form)
        df_preview = pd.read_excel(excel_data, sheet_name=0, skiprows=7, nrows=20)

        with st.expander("📄 Table Preview (Field Autofill View)", expanded=False):
            st.dataframe(df_preview, use_container_width=True)
    except Exception as e:
        st.error(f"⚠️ Could not preview Excel data: {e}")

# === Project & System Info ===
st.markdown("<hr>", unsafe_allow_html=True)
col1, spacer, col2 = st.columns([2, 0.4, 3])  # Correct use of ratio-based columns

with col1:
    st.markdown("### 📁 <b>Project Information</b>", unsafe_allow_html=True)
    proposal_id = st.text_input("Proposal ID")
    customer_name = st.text_input("Customer Name")
    project_name = st.text_input("Project Name")
    country = st.selectbox("Country", ["USA", "Canada", "Germany", "UK", "Sweden", "Argentina"])
    if country == "USA":
        state = st.selectbox("State", ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
                                       "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
                                       "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                                       "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
                                       "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
                                       "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
                                       "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
                                       "Wisconsin", "Wyoming"])
    else:
        state = None
    market = st.selectbox("Market", ["ERCOT", "CAISO", "PJM", "UK Grid", "European Grid"])
    cod = st.date_input("Expected COD (Commercial Operation Date)")

with col2:
    st.markdown("### 🔋 <b>System Configuration</b>", unsafe_allow_html=True)
    battery_brand = st.selectbox("Battery Brand", ["CATL", "BYD", "Samsung SDI", "Cornex", "Other"])
    battery_size = st.number_input("Battery Size per Unit (MWh)", min_value=0.0, step=0.1)
    battery_qty = st.number_input("Number of Battery Containers", min_value=0, step=1)
    pcs_brand = st.selectbox("PCS Brand", ["EPC Power", "Sungrow", "Sineng", "Power Electronics", "Other"])
    pcs_size = st.number_input("PCS Size per Unit (MW)", min_value=0.0, step=0.1)
    pcs_qty = st.number_input("Number of PCS Blocks", min_value=0, step=1)


# === Divider ===
st.markdown("<hr style='margin-top: 25px; margin-bottom: 10px;'>", unsafe_allow_html=True)



# === Divider ===
st.markdown("<hr style='margin-top: 25px; margin-bottom: 10px;'>", unsafe_allow_html=True)


# === Scope + Currency ===
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🛠️ <b>Scope of Services</b>", unsafe_allow_html=True)
    with st.expander("Scope Options", expanded=True):
        field_commissioning = st.checkbox("Field Commissioning Services")
        grid_testing = st.checkbox("Grid Qualification Testing")
        performance_guarantees = st.checkbox("Performance Guarantees")
        onsite_support = st.checkbox("Onsite Support")
        spare_parts = st.checkbox("Spare Parts Inventory")
        preventative_maintenance = st.checkbox("Preventative Maintenance")
        oem_warranty = st.checkbox("OEM Warranty Extension")
        custom_scope = st.checkbox("Custom Scope Needed?")
        custom_scope_details = st.text_area("If custom, please describe the scope", disabled=not custom_scope)

with col2:
    st.markdown("### 💱 <b>Currency & Region</b>", unsafe_allow_html=True)
    with st.expander("Financial Options", expanded=True):
        currency = st.radio("Currency for Proposal", ["USD", "EUR", "GBP", "Custom"])
        custom_fx = st.number_input("Custom FX Rate (1 USD = ?)", min_value=0.0, step=0.01, disabled=(currency != "Custom"))


from PIL import Image
# === FlexBot Assistant (Styled Chat Expander) ===
with st.container():
    st.markdown(
        """
        <style>
        .floating-box {
            position: fixed;
            bottom: 25px;
            right: 25px;
            background-color: white;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0px 2px 10px rgba(0,0,0,0.2);
            z-index: 9999;
            width: 300px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

  # === Sidebar Layout: Theme Toggle + Summary + Footer ===
with st.sidebar:
    # === Proposal Preview ===
    st.markdown("### 🧾 Proposal Preview")
    st.write(f"**Proposal Type:** {proposal_type}")
    st.write(f"**Customer:** {customer_name or '—'}")
    st.write(f"**Project:** {project_name or '—'}")
    st.write(f"**BD Rep:** {bd_rep}")
    st.write(f"**Country:** {country} | **Market:** {market}")
    st.write(f"**Battery:** {battery_qty}x{battery_size} MWh ({battery_brand})")
    st.write(f"**PCS:** {pcs_qty}x{pcs_size} MW ({pcs_brand})")
    st.write(f"**Currency:** {currency}")

  # === Divider ===
    st.markdown("<hr>", unsafe_allow_html=True)

    # === Quote of the Day
    st.markdown(
        """
        <div style="text-align: center; margin: 25px 0;">
            <img src="https://github.com/TaNeekwa/Flexgen-PG3x/blob/main/Pictures/Screenshot%202025-06-03%20224827.png?raw=true" 
                 width="140">
            <p style="font-size: 12px; color: gray;">Quote of the Day</p>
        </div>
        """,
        unsafe_allow_html=True
    )
# === FlexGen Logo & Footer (bottom of main page) ===
st.markdown("""
<hr style="margin-top: 40px; margin-bottom: 10px;">

<div style="text-align: center; margin-top: 20px;">
    <img src="https://github.com/TaNeekwa/Flexgen-PG3x/blob/main/Pictures/Screenshot%202025-06-03%20224337.png?raw=true" 
         width="140" style="margin-bottom: 8px;">
    <p style="font-size: 12px; color: gray;">Developed by FlexGen</p>
    <p style="font-size: 12px; color: gray;">Powered by FlexGen</p>
</div>
""", unsafe_allow_html=True)
# === Submission Buttons ===
st.markdown("""
<style>
.button-row {
    display: flex;
    gap: 15px;
    justify-content: center;
    margin-top: 20px;
}
div.stButton > button {
    background-color: #111 !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 0.5rem 1.5rem !important;
    font-weight: 600 !important;
    border: 1px solid white !important;
    text-align: center !important;
}

/* ✅ Ensure text inside the button also stays white */
div.stButton > button span {
    color: white !important;
}

div.stButton > button:hover {
    background-color: #333 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="button-row">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("🚀 Generate Proposal", use_container_width=True)
    with col2:
        st.button("💾 Save Draft", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


