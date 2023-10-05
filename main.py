import streamlit as st
from st_cytoscape import cytoscape
from PIL import Image

st.set_page_config(layout="wide")


import streamlit_antd_components as sac
from streamlit_card import card
from derive_system_model import system_model
from digitilize import digitilize_information
from mapping import mapping




with st.sidebar:
    st.header("Steps for deriving a digitalized information system")
    step = sac.steps(
    items=[
        sac.StepsItem(title='Derive system model'),
        sac.StepsItem(title='Digitilize available data'),
        sac.StepsItem(title="Map system assets to data"),
        sac.StepsItem(title='Implement information system'),
        sac.StepsItem(title="Manage next steps"),
    ], format_func='title')
    st.write(step)



    hasClicked = card(
    title="Contact me",
    text= "David Hoffmann",
    url="https://www.linkedin.com/in/david-hoffmann-2b7993222/"
    )

elements = [
    {
        "data": {"id": "edge1", "parent": "background"},
        "position": {"x": 0, "y": 0},
        "classes": "corner",
    },
    {
        "data": {"id": "edge2", "parent": "background"},
        "position": {"x": 0, "y": 200},
        "classes": "corner",
    },
    {
        "data": {"id": "edge3", "parent": "background"},
        "position": {"x": 450, "y": 0},
        "classes": "corner",
    },
    {
        "data": {"id": "edge4", "parent": "background"},
        "position": {"x": 450, "y": 200},
        "classes": "corner",
    },
    {
        "data": {"id": "RTC Clock", "parent": "background"},
        "pannable": False,
        "selectable": True,
        "position": {"x": 74, "y": 105},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "GPS Sensor", "parent": "background"},
        "pannable": False,
        "selectable": True,
        "position": {"x": 88, "y": 60},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "Central Gateway", "parent": "background"},
        "pannable": False,
        "selectable": True,
        "position": {"x": 187, "y": 80},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "V2X HeadUnit", "parent": "background"},
        "pannable": False,
        "selectable": True,
        "position": {"x": 260, "y": 80},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "Break Controller", "parent": "background"},
        "pannable": False,
        "selectable": True,
        "position": {"x": 74, "y": 150},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "ESP Controller", "parent": "background"},
        "pannable": False,
        "selectable": True,
        "position": {"x": 150, "y": 137},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "Odometer Controller", "parent": "background"},
        "pannable": False,
        "selectable": True,
        "position": {"x": 224, "y": 133},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "Airbag Actuator", "parent": "background"},
        "pannable": False,
        "selectable": True,
        "position": {"x": 287, "y": 133},
        "style": {"color": "white"},
    },
    {
        "data": {"id": "Engine Control", "parent": "background"},
        "pannable": False,
        "selectable": True,
        "position": {"x": 372, "y": 114},
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

    left_header_column, right_header_column = st.columns(2)
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
            min_zoom=1
        )

    if len(selected["nodes"]) > 0:
        with left_header_column:
            st.header(selected["nodes"][0])

        with right_header_column:
            security_info_tab = sac.segmented(
                items=[
                    sac.SegmentedItem(label='Classification'),
                    sac.SegmentedItem(label='Vulnerabilities'),
                    sac.SegmentedItem(label='Threats'),
                    sac.SegmentedItem(label='Requirements'),
                ], format_func='title', align='start'
            )

        with detail_column:
            if security_info_tab == "Classification":
                sac.tags([
                    sac.Tag(label='tag'),
                    sac.Tag(label='blue', icon='gear', color='blue', bordered=False),
                    sac.Tag(label='orange', icon='google', color='orange', closable=True),
                    sac.Tag(label='link', icon='twitter', color='cyan', link='https://ant.design/components/tag'),
                ], format_func='title', align='center')

    else:
        with detail_column:
            st.info("Select a car element to see its security considerations")

elif step == "Derive system model":
    system_model()
elif step == "Digitilize available data":
    digitilize_information()
elif step == "Map system assets to data":
    mapping()