import streamlit as st
import openai  # ✅ Import OpenAI once at the top
from PIL import Image
# === Page Settings (MUST be first) ===
st.set_page_config(page_title="Proposal Generator", layout="wide")

# === Theme Toggle ===
st.markdown("##### Switch Theme Mode")
dark_mode = st.toggle("🌞 Light / 🌙 Dark")

# === Conditional Styling ===
if dark_mode:
    css_theme = """<style>
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
    </style>"""
else:
    css_theme = """<style>
body, .stApp {
    background-color: #ffffff !important;
    color: #1a1a1a !important;
    font-family: 'Century Gothic', sans-serif !important;
}

/* Global heading and label text */
h1, h2, h3, h4, p, label, div, span {
    color: #1a1a1a !important;
}

/* Sidebar override */
section[data-testid="stSidebar"] {
    background-color: #1a1a1a !important;
    color: white !important;
}
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Logo */
img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    padding-bottom: 10px;
}

/* Form Inputs */
.stTextInput > div > div > input,
.stSelectbox > div,
.stNumberInput > div > input,
.stDateInput > div > input,
.stTextArea > div > textarea,
.stRadio > div > label,
.stCheckbox > div {
    background-color: #ffffff !important;
    color: white !important;  /* ✅ text inside inputs */
    border: 1px solid #d9d9d9 !important;
    border-radius: 6px !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
}

/* Dropdown & select items */
.css-1wa3eu0, .css-1okebmr, .css-1g6gooi, .css-14el2xx, .css-qc6sy-singleValue {
    color: white !important;  /* ✅ selected value text */
}
div[data-baseweb="select"] * {
    color: white !important;  /* ✅ all options in dropdown */
}
input, select, textarea {
    color: white !important;
}

/* Hover styling */
.stSelectbox:hover, .stTextInput:hover, .stNumberInput:hover {
    background-color: #f7f7f7 !important;
}

/* Expander text */
.st-expander > summary {
    color: #1a1a1a !important;
}
</style>"""
    # ✅ INSERT THIS IMMEDIATELY HERE, BEFORE ANY UI:
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
    st.markdown("### 🔌 EMS Proposal Configuration", unsafe_allow_html=True)
    ems_comm_protocol = st.selectbox("EMS Communication Protocol", ["Modbus TCP", "DNP3", "IEC 61850", "Custom"])
    ems_rack_type = st.selectbox("EMS Rack Type", ["Standard Rack", "Outdoor Cabinet", "Custom Integration"])
    ems_networking = st.selectbox("Networking Requirements", ["Basic", "Redundant", "Isolated Secure VLAN"])
elif proposal_type == "Full Product Proposal":
    st.markdown("### 🏗️ Full Product Configuration", unsafe_allow_html=True)
    enclosure_type = st.selectbox("Enclosure Type", ["ISO Container", "Walk-in Enclosure", "Custom Built"])
    hvac_option = st.selectbox("HVAC Type", ["Split System", "Packaged Unit", "Free Cooling", "None"])
    inverter_mounting = st.selectbox("Inverter Mounting", ["Skid Mounted", "Pad Mounted", "Integrated"])
# === AI Assistant ===
with st.expander("🤖 Need Help? Ask FlexBot", expanded=False):
    st.markdown("Type your question below — FlexBot can help you calculate block counts, clarify PCS/Battery specs, or answer proposal questions.")
    user_question = st.text_area("Ask FlexBot anything...")

    if user_question:
        with st.spinner("FlexBot is thinking..."):
            openai.api_key = st.secrets["OPENAI_API_KEY"]
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": (
                            "You are FlexBot, the AI assistant for FlexGen's proposal generator. "
                            "You answer questions about PCS, battery specs, block count formulas, client proposal logic, and configuration guidance. "
                            "Respond in a helpful, knowledgeable, and professional tone."
                        )},
                        {"role": "user", "content": user_question}
                    ]
                )
                st.success(response.choices[0].message.content.strip())
            except Exception as e:
                st.error(f"⚠️ FlexBot ran into an error: {e}")

# === Project & System Info ===
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### 📁 <b>Project Information</b>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
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

# === BD Details, Uploads, Advanced Settings ===
st.markdown("### 👥 <b>Business Development Details</b>", unsafe_allow_html=True)
with st.expander("BD Details", expanded=True):
    bd_rep = st.selectbox("BD Representative", ["Bridget Nolan", "Tyler Davis", "Tara Jo Brooks", "Chris Ramirez", "Other"])
    client_logo = st.file_uploader("📤 Upload Client Logo (Optional)", type=["png", "jpg"])
    if client_logo:
        st.image(client_logo, caption="Client Logo", width=150)
    client_file = st.file_uploader("📎 Attach Client Input or Specs (Optional)", type=["pdf", "docx", "xlsx"])

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

# === Sidebar Summary ===
with st.sidebar:
    st.markdown("### 🧾 Proposal Summary")
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

    # === FlexGen Logo & Footer (slightly padded, no scroll)
    st.markdown(
        """
        <div style="text-align: center; margin-top: 35px;">
            <img src="https://github.com/TaNeekwa/Flexgen-PG3x/blob/main/Pictures/Screenshot%202025-06-03%20224337.png?raw=true" 
                 width="140" style="margin-bottom: 8px;">
            <p style="font-size: 12px; color: gray;">Developed by FlexGen</p>
            <p style="font-size: 12px; color: gray;">Powered by FlexGen Proposal Generator</p>
        </div>
        """,
        unsafe_allow_html=True
    )
# === Submission Buttons ===
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("🚀 Generate Proposal"):
        st.success("Proposal generation initiated!")
with col2:
    if st.button("💾 Save Draft"):
        st.info("Proposal draft saved successfully.")
