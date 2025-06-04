import streamlit as st

# === Page Settings (MUST be first) ===
st.set_page_config(page_title="Proposal Generator", layout="wide")
st.markdown("##### Switch Theme Mode")
dark_mode = st.toggle("🌞 Light / 🌙 Dark")

# === Theme Toggle ===
dark_mode = st.toggle("🌗 Dark Mode")

# === Conditional Styling ===
if dark_mode:
    css_theme = """
    <style>
    body, .stApp {
        background-color: #111 !important;
        color: white !important;
        font-family: 'Century Gothic', sans-serif !important;
    }

    h1, h2, h3, h4, p, label, div, span {
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

    .css-1wa3eu0, .css-1okebmr, .css-1g6gooi, .css-14el2xx, .css-qc6sy-singleValue {
        color: white !important;
    }

    div[data-baseweb="select"] * {
        color: white !important;
    }

    input, select, textarea {
        color: white !important;
    }

    .stSelectbox:hover, .stTextInput:hover, .stNumberInput:hover {
        background-color: #333 !important;
    }

    .st-expander > summary {
        color: white !important;
    }
    </style>
    """
else:
    css_theme = """
    <style>
    body, .stApp {
        background-color: #ffffff !important;
        color: #1a1a1a !important;
        font-family: 'Century Gothic', sans-serif !important;
    }

    h1, h2, h3, h4, p, label, div, span {
        color: #1a1a1a !important;
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
        background-color: #ffffff !important;
        color: #1a1a1a !important;
        border: 1px solid #d9d9d9 !important;
        border-radius: 6px !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
    }

    .css-1wa3eu0, .css-1okebmr, .css-1g6gooi, .css-14el2xx, .css-qc6sy-singleValue {
        color: #1a1a1a !important;
    }

    div[data-baseweb="select"] * {
        color: #1a1a1a !important;
    }

    input, select, textarea {
        color: #1a1a1a !important;
    }

    .stSelectbox:hover, .stTextInput:hover, .stNumberInput:hover {
        background-color: #f7f7f7 !important;
    }

    .st-expander > summary {
        color: #1a1a1a !important;
    }
    </style>
    """

st.markdown(css_theme, unsafe_allow_html=True)
# === Logo + Title Section ===
st.markdown("""
<div style="text-align: center; padding-top: 10px;">
    <img src="https://raw.githubusercontent.com/TaNeekwa/Flexgen-PG3x/main/FlexGen_Primary_Logo_-_Gradient.svg.png" 
         alt="FlexGen Logo" width="300" />
    <h1 style="font-size: 42px; margin-top: 20px;">
        Proposal Generator - FlexGen Edition ⚡
    </h1>
    <p style="font-size: 18px;">Enter project details below to generate your custom proposal.</p>
</div>
""", unsafe_allow_html=True)

# === Proposal Type ===
proposal_type = st.selectbox("🧩 Proposal Type", ["EMS Proposal", "Full Product Proposal"])
st.markdown(f"You selected: **{proposal_type}**")

# === Conditional Inputs ===
if proposal_type == "EMS Proposal":
    st.subheader("🔌 EMS Proposal Configuration")
    ems_comm_protocol = st.selectbox("EMS Communication Protocol", ["Modbus TCP", "DNP3", "IEC 61850", "Custom"])
    ems_rack_type = st.selectbox("EMS Rack Type", ["Standard Rack", "Outdoor Cabinet", "Custom Integration"])
    ems_networking = st.selectbox("Networking Requirements", ["Basic", "Redundant", "Isolated Secure VLAN"])

elif proposal_type == "Full Product Proposal":
    st.subheader("🏗️ Full Product Configuration")
    enclosure_type = st.selectbox("Enclosure Type", ["ISO Container", "Walk-in Enclosure", "Custom Built"])
    hvac_option = st.selectbox("HVAC Type", ["Split System", "Packaged Unit", "Free Cooling", "None"])
    inverter_mounting = st.selectbox("Inverter Mounting", ["Skid Mounted", "Pad Mounted", "Integrated"])

col1, col2 = st.columns(2)

with col1:
    with st.expander("📁 Project Information", expanded=True):
        proposal_id = st.text_input("Proposal ID")
        customer_name = st.text_input("Customer Name")
        project_name = st.text_input("Project Name")
        country = st.selectbox("Country", ["USA", "Canada", "Germany", "UK", "Sweden", "Argentina"])

        if country == "USA":
            state = st.selectbox("State", [
                "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
                "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
                "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
                "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
                "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
                "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
                "Wisconsin", "Wyoming"
            ])
        else:
            state = None

        market = st.selectbox("Market", ["ERCOT", "CAISO", "PJM", "UK Grid", "European Grid"])
        cod = st.date_input("Expected COD (Commercial Operation Date)")

with col2:
    with st.expander("🔋 System Configuration", expanded=True):
        battery_brand = st.selectbox("Battery Brand", ["CATL", "BYD", "Samsung SDI", "Cornex", "Other"])
        battery_size = st.number_input("Battery Size per Unit (MWh)", min_value=0.0, step=0.1)
        battery_qty = st.number_input("Number of Battery Containers", min_value=0, step=1)

        pcs_brand = st.selectbox("PCS Brand", ["EPC Power", "Sungrow", "Sineng", "Power Electronics", "Other"])
        pcs_size = st.number_input("PCS Size per Unit (MW)", min_value=0.0, step=0.1)
        pcs_qty = st.number_input("Number of PCS Blocks", min_value=0, step=1)

col1, col2 = st.columns(2)

with col1:
    with st.expander("🛠️ Scope of Services", expanded=True):
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
    with st.expander("💱 Currency & Region", expanded=True):
        currency = st.radio("Currency for Proposal", ["USD", "EUR", "GBP", "Custom"])
        custom_fx = st.number_input("Custom FX Rate (1 USD = ?)", min_value=0.0, step=0.01, disabled=(currency != "Custom"))

# === Submission ===
if st.button("🚀 Generate Proposal"):
    st.success("Proposal generation initiated!")
    # [Insert your export logic here later]
