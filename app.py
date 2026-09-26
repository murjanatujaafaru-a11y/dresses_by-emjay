import urllib.parse
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Dresses by Emjay - Fit & Style Advisor",
    page_icon="👗",
    layout="centered",
)

# Custom Styling / Brand Header
st.markdown(
    """
    <style>
    .main-header {
        text-align: center;
        color: #8B0000;
        font-family: 'Playfair Display', serif;
    }
    .sub-header {
        text-align: center;
        color: #555555;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<h1 class='main-header'>✨ Dresses by Emjay</h1>", unsafe_allow_html=True
)
st.markdown(
    "<p class='sub-header'>Smart Fit & Style Advisor — Crafting elegance tailored to your silhouette.</p>",
    unsafe_allow_html=True,
)

st.divider()

# Interactive Measurement & Preference Form
with st.form("emjay_sizing_form"):
    st.subheader("1. Enter Your Body Measurements (in inches)")
    col1, col2, col3 = st.columns(3)

    with col1:
        bust = st.number_input("Bust", min_value=20.0, max_value=65.0, value=36.0)
    with col2:
        waist = st.number_input("Waist", min_value=18.0, max_value=60.0, value=28.0)
    with col3:
        hips = st.number_input("Hips", min_value=22.0, max_value=70.0, value=40.0)

    st.subheader("2. Garment Details & Occasion")
    fabric = st.selectbox(
        "Preferred Fabric Choice",
        [
            "Structured (Mikado / Brocade / Jacquard)",
            "Fluid & Flowy (Silk / Chiffon)",
            "Textured / Soft Stretchy",
        ],
    )

    fit_preference = st.radio(
        "Preferred Fit Style", ["Snug & Fitted", "Relaxed & Flowy"]
    )

    occasion = st.selectbox(
        "Occasion / Event Type",
        [
            "Corporate / Official Wear",
            "Wedding Guest / Celebration",
            "Dinner / Formal Gala",
            "Casual Chic",
        ],
    )

    submitted = st.form_submit_button("Get Size Recommendation & Styling Advice")

# Processing and Recommendation Output
if submitted:
    # Sizing Logic
    if bust <= 34 and waist <= 26 and hips <= 38:
        recommended_size = "UK 8 (Small)"
    elif bust <= 37 and waist <= 30 and hips <= 41:
        recommended_size = "UK 10 (Medium)"
    elif bust <= 40 and waist <= 33 and hips <= 44:
        recommended_size = "UK 12 (Large)"
    elif bust <= 43 and waist <= 36 and hips <= 47:
        recommended_size = "UK 14 (XL)"
    elif bust <= 46 and waist <= 40 and hips <= 50:
        recommended_size = "UK 16 (XXL)"
    else:
        recommended_size = "Custom Bespoke Size"

    # Fabric Tolerance Notice
    fabric_note = ""
    if "Structured" in fabric:
        fabric_note = "📌 **Fabric Note:** Mikado, Brocade, and Jacquard fabrics have minimal stretch. We account for zero-stretch structure to guarantee comfort."
    elif "Fluid" in fabric:
        fabric_note = "📌 **Fabric Note:** Silk and Chiffon offer elegant drape and slight natural movement."

    # Recommendation Display
    st.markdown("---")
    st.subheader("🎯 Your Personal Fit Result")
    st.success(
        f"**Recommended Dresses by Emjay Size:** `{recommended_size}`"
    )

    if fabric_note:
        st.info(fabric_note)

    # Style Guidance
    st.subheader("💡 Styling & Silhouette Advice")
    if occasion == "Corporate / Official Wear":
        st.write(
            "For structured office wear, pair this piece with block heels, minimal accessories, and a structured handbag for an effortless corporate presence."
        )
    elif occasion == "Wedding Guest / Celebration":
        st.write(
            "Complement this garment with a coordinating head tie or bold statement jewelry to elevate the celebration look."
        )
    else:
        st.write(
            "Pair with neutral accessories to highlight the craftsmanship and silhouette of the dress."
        )

    # WhatsApp Direct Order Integration
    # Replace '234XXXXXXXXXX' with your full WhatsApp Business phone number (including country code, e.g., 234...)
    whatsapp_number = "2348136749494"

    order_message = (
        f"Hello Dresses by Emjay! I generated my size recommendation on your advisor app:\n\n"
        f"• Recommended Size: {recommended_size}\n"
        f"• Measurements: Bust {bust}\", Waist {waist}\", Hips {hips}\"\n"
        f"• Fabric Choice: {fabric}\n"
        f"• Event: {occasion}\n\n"
        f"I would like to discuss available designs in this size!"
    )

    encoded_message = urllib.parse.quote(order_message)
    whatsapp_link = (
        f"https://wa.me/{whatsapp_number}?text={encoded_message}"
    )

    st.markdown("---")
    st.markdown(
        f"""
        <a href="{whatsapp_link}" target="_blank" style="
            display: inline-block;
            background-color: #25D366;
            color: white;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            border-radius: 8px;
            font-weight: bold;
        ">💬 Send Measurement Summary to WhatsApp</a>
        """,
        unsafe_allow_html=True,
    )