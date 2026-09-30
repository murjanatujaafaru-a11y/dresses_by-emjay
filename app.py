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
    "Welcome! Find your perfect tailored fit and fabric guide for our ready-to-wear collection in under 30 seconds."
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

    submitted = st.form_submit_button("✨ Get Sizing & Style Recommendation")


# --- 2. SIZING LOGIC, ADVICE & WHATSAPP ROUTING ---
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

        # Dynamic Fit & Fabric Logic
        fit_style = "Structured Corporate Fit & Tailored Silhouette"
        
        # Determine proportions for custom fit advice
        if hip - waist >= 12:
            fit_advice = "You have an hourglass proportion. A fitted waistline with an A-line or flared skirt silhouette will accommodate your hips comfortably without pulling."
        elif bust - waist <= 4 and hip - waist <= 4:
            fit_advice = "You have a straight silhouette. Structured cuts, belted waistlines, and high-neck modest designs will add definition."
        else:
            fit_advice = "Standard corporate tailored fit. Offers clean structure through the bust and waist while maintaining modesty and comfort."

        recommended_fabrics = [
            "**Mikado / Jacquard:** Ideal for structured corporate dresses that hold their shape crisp throughout the day.",
            "**Silk / Silk Satin:** Perfect for fluid draping, modest evening wear, and high-comfort corporate fits.",
            "**Brocade:** Recommended for statement ceremonial or high-end modest corporate pieces."
        ]

        # --- DISPLAY RESULTS ON APP UI ---
        st.success(
            f"Hi **{customer_name}**! Based on your measurements, your recommended size for **Dresses by Emjay** is **{recommended_size}**."
        )

        # Style & Fabric Details Section
        st.subheader("👗 Fit & Fabric Recommendation")
        st.markdown(f"**Fit Style:** {fit_style}")
        st.info(f"💡 **Tailored Fit Advice:** {fit_advice}")

        st.markdown("**Recommended Fabrics for Your Fit:**")
        for fab in recommended_fabrics:
            st.markdown(f"- {fab}")

        st.divider()

        # Build Pre-filled WhatsApp Message featuring size + style details
        raw_message = (
            f"Hi Dresses by Emjay! My name is {customer_name} from {location}.\n\n"
            f"I used your SmartFit Advisor and my recommended size is *{recommended_size}*.\n"
            f"• Bust: {bust}\"\n"
            f"• Waist: {waist}\"\n"
            f"• Hip: {hip}\"\n\n"
            f"Fit Style: {fit_style}\n\n"
            f"I would like to place an order from your latest collection!"
        )

        # Encode text safely for web URLs
        encoded_message = urllib.parse.quote(raw_message)

        # WhatsApp phone number
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