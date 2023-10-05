import streamlit as st
from st_cytoscape import cytoscape
from PIL import Image
from google.cloud import firestore
import json
import streamlit_nested_layout

st.set_page_config(layout="wide")


import streamlit_antd_components as sac
from derive_system_model import system_model
from digitize import digitize_information
from mapping import mapping
from uuid import uuid4
from next_steps import next_steps


db = firestore.Client.from_service_account_json("firestore.json")

if "mapping_selection" not in st.session_state:
    st.session_state["mapping_selection"] = []

if "case_dict" not in st.session_state:
    st.session_state["case_dict"] = {}


with open("./asset_data.json", "r") as file:
    asset_data = json.load(file)

with st.sidebar:
    st.header("Steps for deriving a digitalized information system")
    step = sac.steps(
    items=[
        sac.StepsItem(title='Derive system model'),
        sac.StepsItem(title='Digitize available data'),
        sac.StepsItem(title="Map generic assets to domain assets"),
        sac.StepsItem(title='Implement information system'),
        sac.StepsItem(title="Manage next steps"),
    ], format_func='title')
    st.write(step)


elements = [
    {
        "data": {"id": "edge1", "parent": "background", "domain_mappings":[]},
        "position": {"x": 0, "y": 0},
        "classes": "corner",
    },
    {
        "data": {"id": "edge2", "parent": "background", "domain_mappings":[]},
        "position": {"x": 0, "y": 200},
        "classes": "corner",
    },
    {
        "data": {"id": "edge3", "parent": "background", "domain_mappings":[]},
        "position": {"x": 450, "y": 0},
        "classes": "corner",
    },
    {
        "data": {"id": "edge4", "parent": "background", "domain_mappings":[]},
        "position": {"x": 450, "y": 200},
        "classes": "corner",
    },
    {
        "data": {"id": "RTC Clock", "parent": "background", "domain_mappings":[]},
        "pannable": False,
        "selectable": True,
        "position": {"x": 73, "y": 105},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "GPS Sensor", "parent": "background", "domain_mappings":[]},
        "pannable": False,
        "selectable": True,
        "position": {"x": 88, "y": 60},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "Central Gateway", "parent": "background", "domain_mappings":[]},
        "pannable": False,
        "selectable": True,
        "position": {"x": 187, "y": 79},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "V2X HeadUnit", "parent": "background", "domain_mappings":[]},
        "pannable": False,
        "selectable": True,
        "position": {"x": 260, "y": 80},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "Break Controller", "parent": "background", "domain_mappings":[]},
        "pannable": False,
        "selectable": True,
        "position": {"x": 73, "y": 152},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "ESP Controller", "parent": "background", "domain_mappings":[]},
        "pannable": False,
        "selectable": True,
        "position": {"x": 151, "y": 134},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "Odometer Controller", "parent": "background", "domain_mappings":[]},
        "pannable": False,
        "selectable": True,
        "position": {"x": 224, "y": 133},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "Airbag Actuator", "parent": "background", "domain_mappings":[]},
        "pannable": False,
        "selectable": True,
        "position": {"x": 287, "y": 133},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "Engine Control", "parent": "background", "domain_mappings":[]},
        "pannable": False,
        "selectable": True,
        "position": {"x": 371, "y": 114},
        "style": {"color": "white"},
    },
    # {"data": {"id": "Y", "parent": "background"}},
    # {"data": {"id": "Z", "parent": "background"}},
    {"data": {"id": "background"}, "classes": "image", "selectable": False},
    # {"data": {"source": "X", "target": "Y", "id": "X➞Y"}},
    # {"data": {"source": "Z", "target": "Y", "id": "Z➞Y"}},
    # {"data": {"source": "Z", "target": "X", "id": "Z➞X"}},
]

stylesheet = [

    {
        "selector": "node",
        "style": {
            "background-color": "grey",
            "label": "data(id)",
            "width": 48,
            "height": 30,
            "shape": "rectangle",
            "text-valign": "center",
            "text-halign": "center",
            "font-size": 10,
            "text-wrap": "wrap",  # Wrap the text
            "text-max-width": 48,  # Maximum width before text wraps
        },
    },
    {
        "selector": ".image",
        "style": {
            "label": "",
            "background-color": "#ffffff",
            "background-image": "https://i.imgur.com/74eSogS.png",
            # "background-image":
            "width": 200,
            "height": 500,
        },
    },
    {
        "selector": ".corner",
        "style": {
            "label": "",
            "background-color": "#ffffff",
        },
    },
    {
        "selector": "edge",
        "style": {
            "width": 3,
            "curve-style": "bezier",
            "target-arrow-shape": "triangle",
        },
    },
]

if step == "Implement information system":

    st.header("Automotive Cybersecurity")

    left_header_column, right_header_column = st.columns([2, 1])
    figure_column, detail_column = st.columns([2, 1])
    with figure_column:
        selected = cytoscape(
            elements,
            stylesheet,
            key="graph",
            layout={"name": "preset"},
            user_panning_enabled=True,
            user_zooming_enabled=False,
            selection_type="single",
            min_zoom=1,
            height="50em"
        )

    if len(selected["nodes"]) > 0:
        with left_header_column:
            st.header(selected["nodes"][0])

        with right_header_column:
            security_info_tab = sac.segmented(
                items=[
                    sac.SegmentedItem(label='Classification'),
                    sac.SegmentedItem(label='Threats'),
                    sac.SegmentedItem(label='Requirements'),
                ], format_func='title', align='start', grow=True, size="lg"
            )

        with detail_column:
            if security_info_tab == "Classification":

                cases_ref = db.collection("cases")
                cases = list(cases_ref.stream())  # Fetch data once and convert to a list
                case_list = []
                for case in cases:
                    case_list.append(case.id)
                selected_case = st.selectbox("Select case", case_list)
                case_ref = db.collection("cases").document(selected_case)
                case = case_ref.get()
                case_dict = case.to_dict()
                st.session_state["case_dict"] = case_dict

                domain_option_list = list(case_dict.keys())

                mapping_selection = st.multiselect(label="Choose fitting domain elements", options=domain_option_list)
                st.session_state["mapping_selection"] = mapping_selection

            if security_info_tab =="Threats":
                for domain_asset in st.session_state["mapping_selection"]:
                    with st.expander(f"Treats for {domain_asset}"):
                        general_asset_list = st.session_state["case_dict"][domain_asset]
                        for general_asset in general_asset_list:
                            threat_dict = asset_data[general_asset]["Threats"]
                            for threat in threat_dict:
                                with st.expander(f"{threat['ThreatName']}"):
                                    id_column, name_column = st.columns([1,2])
                                    with id_column:
                                        st.info(f"{threat['ThreatID']}")
                                    with name_column:
                                        st.info(f"{threat['ThreatName']}")
                                    threat_name_column, threat_description_column = st.columns([1,2])
                                    with threat_name_column:
                                        st.warning("Description:")
                                    with threat_description_column:
                                        st.warning(f"{threat['Description']}")
                                    threat_name_column, threat_description_column = st.columns([1,2])
                                    with threat_name_column:
                                        st.error("Risk:")
                                    with threat_description_column:
                                        st.error(f"{threat['Implications']}")
                                    vector_column, impactcolumn = st.columns([1,2])
                                    with vector_column:
                                        st.multiselect("Attack Vectors", threat['AttackVectors'], default=threat['AttackVectors'], key=str(uuid4()) )
                                    with impactcolumn:
                                        st.metric("Impact", threat['ImpactLevel'])

                                
            if security_info_tab == "Requirements":
                for domain_asset in st.session_state["mapping_selection"]:
                    with st.expander(f"Requirements for {domain_asset}"):
                        general_asset_list = st.session_state["case_dict"][domain_asset]
                        for general_asset in general_asset_list:
                            requirement_dict = asset_data[general_asset]["Requirements"]
                            for requirement in requirement_dict:
                                with st.expander(f"{requirement['RequirementName']}"):
                                    id_column, name_column = st.columns([1, 2])
                                    with id_column:
                                        st.info(f"{requirement['RequirementID']}")
                                    with name_column:
                                        st.info(f"{requirement['RequirementName']}")
                                    
                                    description_name_column, description_value_column = st.columns([1, 2])
                                    with description_name_column:
                                        st.warning("Description:")
                                    with description_value_column:
                                        st.warning(f"{requirement['Description']}")
                                    
                                    responsible_name_column, responsible_value_column = st.columns([1, 2])
                                    with responsible_name_column:
                                        st.error("Responsible Roles:")
                                    with responsible_value_column:
                                        st.error(f"{', '.join(requirement['ResponsibleRoles'])}")
                                    
                                    priority_column, action_column = st.columns([1, 2])
                                    with priority_column:
                                        st.metric("Priority", requirement['Priority'])
                                    with action_column:
                                        st.multiselect("Action Type", requirement['ActionType'], default=requirement['ActionType'], key=str(uuid4()))
                                    
                                    affected_column, control_column = st.columns([1, 2])
                                    with affected_column:
                                        st.metric("Security Control Type", requirement['SecurityControlType'])
                                    with control_column:
                                        st.multiselect("Affected Components", requirement['AffectedComponents'], default=requirement['AffectedComponents'], key=str(uuid4()))



    else:
        with detail_column:
            st.info("Select a car element to see its security considerations")

elif step == "Derive system model":
    system_model()
elif step == "Digitize available data":
    digitize_information()
elif step == "Map generic assets to domain assets":
    mapping()
elif step == "Manage next steps":
    next_steps()