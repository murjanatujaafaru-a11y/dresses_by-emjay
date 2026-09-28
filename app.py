import urllib.parse
import streamlit as st

st.set_page_config(
    page_title="Dresses by Emjay — SmartFit Style Advisor",
    page_icon="👗",
    layout="centered",
)

# --- BRANDING HEADER ---
st.title("👗 Dresses by Emjay")
st.subheader("SmartFit Style & Sizing Advisor")
st.write(
    "Welcome! Find your perfect tailored fit for our ready-to-wear collection in under 30 seconds."
)

st.divider()

# --- 1. CUSTOMER INPUT FORM ---
with st.form("sizing_form"):
    st.subheader("1. Your Details")
    customer_name = st.text_input("Full Name", placeholder="e.g. Amina Bello")
    location = st.text_input(
        "City / State", placeholder="e.g. Lagos, Abuja, Port Harcourt"
    )

    st.subheader("2. Body Measurements (Inches)")
    bust = st.number_input(
        "Bust Measurement", min_value=20.0, max_value=60.0, value=36.0, step=0.5
    )
    waist = st.number_input(
        "Waist Measurement", min_value=20.0, max_value=60.0, value=28.0, step=0.5
    )
    hip = st.number_input(
        "Hip Measurement", min_value=20.0, max_value=60.0, value=40.0, step=0.5
    )

    submitted = st.form_submit_button("✨ Get Sizing Recommendation")


# --- 2. SIZING LOGIC & WHATSAPP ROUTING ---
if submitted:
    if not customer_name:
        st.error("Please enter your name before getting a recommendation.")
    else:
        # Sizing Calculation Logic
        if bust <= 34 and waist <= 26:
            recommended_size = "UK 8"
        elif bust <= 36 and waist <= 28:
            recommended_size = "UK 10"
        elif bust <= 38 and waist <= 30:
            recommended_size = "UK 12"
        elif bust <= 40 and waist <= 32:
            recommended_size = "UK 14"
        else:
            recommended_size = "UK 16+"

        # Display Result on Screen
        st.success(
            f"Hi **{customer_name}**! Based on your measurements, your recommended size for **Dresses by Emjay** is **{recommended_size}**."
        )

        # Build Pre-filled WhatsApp Message featuring the Brand Name
        raw_message = (
            f"Hi Dresses by Emjay! My name is {customer_name} from {location}.\n\n"
            f"I used your SmartFit Advisor and my recommended size is *{recommended_size}*.\n"
            f"• Bust: {bust}\"\n"
            f"• Waist: {waist}\"\n"
            f"• Hip: {hip}\"\n\n"
            f"I would like to place an order from your latest collection!"
        )

        # Encode text safely for web URLs
        encoded_message = urllib.parse.quote(raw_message)

        # Replace with your actual WhatsApp phone number (country code first, no + sign)
        whatsapp_number = "2348136749494"
        whatsapp_url = (
            f"https://wa.me/{whatsapp_number}?text={encoded_message}"
        )

        # Direct Action Button
        st.markdown(
            f"""
            <a href="{whatsapp_url}" target="_blank">
                <button style="
                    background-color: #25D366;
                    color: white;
                    padding: 12px 24px;
                    border: none;
                    border-radius: 8px;
                    font-size: 16px;
                    font-weight: bold;
                    cursor: pointer;
                    width: 100%;">
                    💬 Send Order Details to Dresses by Emjay
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )