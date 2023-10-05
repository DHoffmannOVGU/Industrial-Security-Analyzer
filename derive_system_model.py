import streamlit as st
import streamlit_antd_components as sac

def system_model():
    st.header("Derive system model")
    st.success("The system model is the first step in the process of digitilizing your assets. It is a high level overview of the system and its components. It is used to identify the assets that are part of the system and to identify the data that is available for each asset.")
    with st.expander("Gather available information"):
        st.info("Information from the following sources is used to derive the system model:")
        st.link_button("ISO 27001 via BSI-IT", "https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium/Zuordnung_ISO_und_IT_Grundschutz.pdf?__blob=publicationFile&v=5")
        st.link_button("NIST Cybersecurity Framework", "https://www.nist.gov/cyberframework")
        st.link_button("BSI-Bausteine", "https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/IT-Grundschutz-Bausteine/Bausteine_Download_Edition_node.html")
        st.link_button("BSI-Grundschutzkatalog", "https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html")

    with st.expander("Identify system metamodel"):
        st.info("The metamodel specifies the structure of the data, used in database schemas and alike.")
        sac.menu([
            sac.MenuItem('Asset', icon='app', children=[
                sac.MenuItem('Identification', icon='bag-check', tag='object', children=[
                    sac.MenuItem('Name', icon='bag-check', tag='string'),
                    sac.MenuItem('Description', icon='bag-check', tag='string'),
                    sac.MenuItem('Team', icon='bag-check', tag='string'),
                    ]),
                sac.MenuItem('Vulnerabilities', icon='bag-check', tag='list_object', children=[
                    sac.MenuItem('Name', icon='bag-check', tag='string'),
                    sac.MenuItem('Description', icon='bag-check', tag='string'),
                    sac.MenuItem("ID", icon='bag-check', tag='string'),
                    sac.MenuItem("Origin", icon='bag-check', tag='string'),
                    sac.MenuItem('CVE', icon='bag-check', tag='string'),
                ]),
                sac.MenuItem('Threats', icon='award', tag='list_object', children=[
                    sac.MenuItem('Name', icon='bag-check', tag='string'),
                    sac.MenuItem('Description', icon='bag-check', tag='string'),
                    sac.MenuItem('Likelihood', icon='bag-check', tag='string'),
                    sac.MenuItem('Impact', icon='bag-check', tag='string'),
                    sac.MenuItem("Origin", icon='bag-check', tag='string'),
                    sac.MenuItem('Risk', icon='bag-check', tag='string'),
                ]),
                sac.MenuItem('Mitigations', icon='award', tag='list_object', children=[
                    sac.MenuItem('Name', icon='bag-check', tag='string'),
                    sac.MenuItem('Description', icon='bag-check', tag='string'),
                    sac.MenuItem("Security Level", icon='bag-check', tag='string'),
                    sac.MenuItem("Origin", icon='bag-check', tag='string'),
                ]),               
            ]),
        ], format_func='title', open_index=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
