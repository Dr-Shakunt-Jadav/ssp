import streamlit as st

PAGES = [
    {"path": "app.py", "label": "Home"},
    {"path": "pages/0_intro.py", "label": "Intro"},
    {"path": "pages/1_initiate.py", "label": "Initiate"},
    {"path": "pages/2_fill_form.py", "label": "Fill Form"},
    {"path": "pages/3_form_overview.py", "label": "Form Overview"},
    {"path": "pages/4_Compare.py", "label": "Compare"},
    {"path": "pages/5_results.py", "label": "Results"},
    {"path": "pages/5_results_v2.py", "label": "Results V2"},
]
PATH_BY_LABEL = {page["label"]: page["path"] for page in PAGES}
ORDER = [page["label"] for page in PAGES]


def render_navigation(current: str):
    # Track navigation stack in session state
    if "nav_stack" not in st.session_state:
        st.session_state.nav_stack = []
    stack = st.session_state.nav_stack

    if not stack or stack[-1] != current:
        if current in stack:
            stack[:] = stack[: stack.index(current) + 1]
        else:
            stack.append(current)

    # Breadcrumb strip
    cols = st.columns(max(len(stack) * 2 - 1, 1))
    for i, crumb in enumerate(stack):
        with cols[i * 2]:
            if i < len(stack) - 1:
                if st.button(crumb, key=f"bc_{i}"):
                    st.session_state.nav_stack = stack[: i + 1]
                    st.switch_page(PATH_BY_LABEL[crumb])
            else:
                st.markdown(f"**{crumb}**")
        if i < len(stack) - 1:
            cols[i * 2 + 1].markdown(
                "<div style='text-align:center'>›</div>", unsafe_allow_html=True
            )

    st.divider()
    st.subheader(current)

    # Drill down into the next page in the flow
    children = ORDER[ORDER.index(current) + 1:]
    if children:
        next_page = children[0]
        col1, col2 = st.columns([5, 1])
        col1.write(f"**{next_page}**")
        if col2.button("›", key=f"drill_{next_page}"):
            stack.append(next_page)
            st.session_state.nav_stack = stack
            st.switch_page(PATH_BY_LABEL[next_page])
    else:
        st.success(f"You're at the end of the flow: **{current}**")
        if st.button("← Back"):
            stack.pop()
            st.session_state.nav_stack = stack
            st.switch_page(PATH_BY_LABEL[stack[-1]])
