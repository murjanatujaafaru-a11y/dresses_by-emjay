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
    "Welcome! Find your perfect tailored fit, fabric stretch guide, and styling advice for our ready-to-wear collection."
)

st.divider()

# --- FABRIC DATABASE ---
FABRIC_DETAILS = {
    "Brocade": {
        "stretchy": "Non-stretchy (Rigid & Structured)",
        "desc": "Rich, woven pattern that holds sharp silhouettes beautifully. Perfect for statement ceremonial wear.",
    },
    "Mikado": {
        "stretchy": "Non-stretchy (High Structure & Subtle Sheen)",
        "desc": "Heavyweight architectural fabric ideal for clean corporate cuts and tailored modest dresses.",
    },
    "Jacquard": {
        "stretchy": "Non-stretchy / Low stretch",
        "desc": "Textured luxury fabric with subtle depth. Maintains crisp shapes throughout the workday.",
    },
    "Silk / Silk Satin": {
        "stretchy": "Low stretch / Bias-cut flexibility",
        "desc": "Smooth, fluid, and highly breathable. Drapes elegantly for evening wear and relaxed fits.",
    },
}

# --- 1. CUSTOMER INPUT FORM ---
with st.form("sizing_form"):
    st.subheader("1. Your Details")
    customer_name = st.text_input("Full Name", placeholder="e.g. Amina Bello")
    location = st.text_input(
        "City / State", placeholder="e.g. Lagos, Abuja, Port Harcourt"
    )

    st.subheader("2. Body Measurements (Inches)")
    col1, col2, col3 = st.columns(3)
    with col1:
        bust = st.number_input(
            "Bust", min_value=20.0, max_value=60.0, value=36.0, step=0.5
        )
    with col2:
        waist = st.number_input(
            "Waist", min_value=20.0, max_value=60.0, value=28.0, step=0.5
        )
    with col3:
        hip = st.number_input(
            "Hip", min_value=20.0, max_value=60.0, value=40.0, step=0.5
        )

    st.subheader("3. Style Preferences")
    fabric_choice = st.selectbox(
        "Select Fabric Type",
        ["Brocade", "Mikado", "Jacquard", "Silk / Silk Satin"],
    )
    fit_choice = st.selectbox(
        "Select Fit Preference",
        ["Fitted / Tailored", "Relaxed / Flowy", "Modest / Structured"],
    )
    event_choice = st.selectbox(
        "Occasion / Event Type",
        [
            "Corporate Workwear & Executive Meetings",
            "Weddings & Traditional Ceremonies",
            "Dinner & Evening Galas",
            "Casual Luxury / Daily Wear",
        ],
    )

    submitted = st.form_submit_button("✨ Get Personalized Recommendation")


# --- 2. SIZING LOGIC & CUSTOM ADVICE ---
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

        # Fabric stretch & details
        fabric_info = FABRIC_DETAILS[fabric_choice]
        is_stretchy = fabric_info["stretchy"]

        # Stretch-based sizing caution
        if "Non-stretchy" in is_stretchy and fit_choice == "Fitted / Tailored":
            stretch_advice = (
                f"**Note on Fabric:** {fabric_choice} is **{is_stretchy}**. "
                "Since you selected a Fitted style, we recommend sticking strictly to your exact measurements "
                "or adding a +0.5 inch comfort margin at the waist to ensure ease of movement."
            )
        else:
            stretch_advice = f"**Fabric Stretch:** {fabric_choice} is **{is_stretchy}**. Works exceptionally well with a {fit_choice.lower()} cut."

        # Accessory pairing logic based on Event & Fabric Choice
        if "Weddings" in event_choice or fabric_choice in ["Brocade", "Jacquard"]:
            accessory_advice = (
                "- **Jewelry:** Statement gold or pearl earrings to match the rich texture of the fabric.\n"
                "- **Handbag:** Structured metallic or embellishment-detailed clutch.\n"
                "- **Footwear:** Pointed-toe heels or embellished straps."
            )
        elif "Corporate" in event_choice or fabric_choice == "Mikado":
            accessory_advice = (
                "- **Jewelry:** Minimalist stud earrings and a sleek wrist watch or subtle cuff.\n"
                "- **Handbag:** Structured leather tote or clean executive handbag.\n"
                "- **Footwear:** Classic pumps or block heels for all-day comfort."
            )
        else:  # Dinner / Evening / Silk
            accessory_advice = (
                "- **Jewelry:** Delicate drop earrings or a dainty pendant necklace that complements the neckline.\n"
                "- **Handbag:** Sleek satin clutch or minimalist chain bag.\n"
                "- **Footwear:** Strappy heels or elegant mule slippers."
            )

        # --- DISPLAY RESULTS ON APP UI ---
        st.success(
            f"Hi **{customer_name}**! Your recommended size for **Dresses by Emjay** is **{recommended_size}**."
        )

        st.subheader("🧵 Fabric Stretch & Fit Analysis")
        st.write(f"**Selected Fabric:** {fabric_choice}")
        st.write(f"**Fabric Profile:** {fabric_info['desc']}")
        st.info(stretch_advice)

        st.subheader("✨ Accessory & Styling Guide")
        st.write(f"**Tailored for:** {event_choice} ({fit_choice})")
        st.markdown(accessory_advice)

        st.divider()

        # Build Pre-filled WhatsApp Message featuring all custom choices
        raw_message = (
            f"Hi Dresses by Emjay! My name is {customer_name} from {location}.\n\n"
            f"I used your SmartFit Advisor and here are my order details:\n"
            f"• Recommended Size: *{recommended_size}*\n"
            f"• Bust: {bust}\" | Waist: {waist}\" | Hip: {hip}\"\n"
            f"• Fabric Choice: {fabric_choice}\n"
            f"• Desired Fit: {fit_choice}\n"
            f"• Event/Occasion: {event_choice}\n\n"
            f"I would like to place an order based on these recommendations!"
        )

        encoded_message = urllib.parse.quote(raw_message)
        whatsapp_number = "2348136749494"
        whatsapp_url = (
            f"https://wa.me/{whatsapp_number}?text={encoded_message}"
        )

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
                    💬 Send Order & Custom Styling Details to Dresses by Emjay
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )