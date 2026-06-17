# Renders the Company Autofill section (right column, top of main page).
# Looks up a company by name via Wikipedia/Wikidata and pre-fills the form fields.
import streamlit as st
from utils.autofill_system import build_startup_profile
from src.services.field_extractor import extract_fields


def render_autofill(col, industries: list, countries: list, states: list):
    with col:
        st.subheader("🔍 Company Autofill")
        st.caption("Type a company name to look up its public profile.")

        autofill_query = st.text_input("Company name", placeholder="e.g. Airbnb")
        if st.button("Look up", use_container_width=True) and autofill_query:
            with st.spinner("Fetching company data..."):
                autofill_result = build_startup_profile(autofill_query)
                profile = autofill_result.get("profile", {})
                profile_str = (
                    f"Company: {autofill_query}. "
                    f"Founded: {profile.get('founded_at') or ''}. "
                    f"Industry: {profile.get('industry') or ''}. "
                    f"Country: {profile.get('country') or ''}. "
                    f"City: {profile.get('city') or ''}. "
                    f"State: {profile.get('state') or ''}."
                )
            with st.spinner("Mapping fields..."):
                fields = {
                "company_name": autofill_query,
                "industry": profile.get("industry"),
                "founded_year": (
                    int(profile["founded_at"][:4])
                    if profile.get("founded_at")
                    else None
                ),
            }
                # fields = extract_fields(profile_str, industries, countries, states)

                st.write("PROFILE:", profile)
                st.write("PROFILE STRING:", profile_str)
                st.write("EXTRACTED:", fields)

                fields["company_name"] = autofill_query
                st.session_state.extracted_fields = fields
