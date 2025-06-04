import streamlit as st

# Page settings — MUST be first!
st.set_page_config(page_title="Proposal Generator", layout="wide")

# === Global Style Overrides ===
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        background-color: white !important;
        color: black !important;
        font-family: 'Century Gothic', sans-serif !important;
    }
    .stApp {
        background-color: white !important;
    }
    h1, h2, h3, h4, h5, h6, p, label, div, input, select, textarea {
        color: black !important;
        font-family: 'Century Gothic', sans-serif !important;
    }
    .stMarkdown, .stTextInput, .stSelectbox, .stDateInput, .stNumberInput, .stRadio {
        font-family: 'Century Gothic', sans-serif !important;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# === Logo + Title Section (Single clean block) ===
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/TaNeekwa/Flexgen-PG3x/main/FlexGen_Primary_Logo_-_Gradient.svg.png" width="200"/>
        <h1 style="font-size: 40px; margin-top: 10px;">Proposal Generator - FlexGen Edition ⚡</h1>
        <p style="font-size: 18px;">Enter project details below to generate your custom proposal.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# === Proposal Type Selector ===
proposal_type = st.selectbox("🧩 Proposal Type", ["EMS Proposal", "Full Product Proposal"])
st.markdown(f"You selected: **{proposal_type}**")

# === Conditional Section Based on Proposal Type ===
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

# === Project Info ===
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

# === System Configuration ===
with st.expander("🔋 System Configuration", expanded=True):
    battery_brand = st.selectbox("Battery Brand", ["CATL", "BYD", "Samsung SDI", "Cornex", "Other"])
    battery_size = st.number_input("Battery Size per Unit (MWh)", min_value=0.0, step=0.1)
    battery_qty = st.number_input("Number of Battery Containers", min_value=0, step=1)

    pcs_brand = st.selectbox("PCS Brand", ["EPC Power", "Sungrow", "Sineng", "Power Electronics", "Other"])
    pcs_size = st.number_input("PCS Size per Unit (MW)", min_value=0.0, step=0.1)
    pcs_qty = st.number_input("Number of PCS Blocks", min_value=0, step=1)

# === Scope of Services ===
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

# === Currency Selection ===
with st.expander("💱 Currency & Region", expanded=True):
    currency = st.radio("Currency for Proposal", ["USD", "EUR", "GBP", "Custom"])
    custom_fx = st.number_input("Custom FX Rate (1 USD = ?)", min_value=0.0, step=0.01, disabled=(currency != "Custom"))

# === Submission ===
if st.button("🚀 Generate Proposal"):
    st.success("Proposal generation initiated!")
