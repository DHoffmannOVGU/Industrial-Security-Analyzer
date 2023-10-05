import streamlit as st
import streamlit_antd_components as sac
import json
import base64

def display_pdf(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700" type="application/pdf"></iframe>'
    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

def digitize_information():
    st.info(
        """In this step, the available information is digitilized and parsed into the specified metamodel. 
        
        """)
    with st.expander("The following cases are considered:"):
        st.success(
            """
            - The information is already available in a digital format according to the metamodel., e.g. in a database or a spreadsheet.
            Only integration is required.
            """
        )
        st.warning(
            """
            - The information is available in a digital format, but not according to the metamodel,
            e.g. in tool-specific output format. A conversion/transformation is required.
            """
        )
        st.error(
            """
            - The information is only available in a non-digital format, e.g. in a PDF or a Word document.
            A manual digitilization or a NLP-based approach is required.
            """
        )

    st.warning(
        """
        - For the many cases of industrial security, where the information is not available in a digital format,
        we are going to leverage a prompt engineering approach to digitilize the information.
        """
    )
    st.link_button("Here is an examplary chat with well working prompts", "https://chat.openai.com/share/eeac65a1-bdc5-40db-8332-58e9b0f24efd")

    with st.expander("This is how it looks like:"):
        before_column, after_column = st.columns(2)

        with before_column:
            st.subheader("Before")
            display_pdf("./pdf_data/IND_2.1_General ICS Components.pdf")
  
        
        with after_column:
            #Load Json example
            st.subheader("After")
            with open('./asset_data.json') as json_file:
                data = json.load(json_file)
                st.json(data["ICS Component"], expanded=True)
