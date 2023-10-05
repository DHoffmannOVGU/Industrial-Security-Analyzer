import streamlit as st
import json
import streamlit.components.v1 as components
from google.cloud import firestore
# Create a reference to the projects

# Authenticate to Firestore with the JSON account key.

db = firestore.Client.from_service_account_json("firestore.json")

def load_system_asset_list(file):
    with open(file) as json_file:
        assets = json.load(json_file)
        asset_list = list(assets.keys())
        return asset_list


def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}'
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

def mapping():
    st.header("Map case assets to system assets")
    #Load mapping json
    with open('./mapping.json') as json_file:
        mapping_list = json.load(json_file)
        st.json(mapping_list, expanded=False)

    asset_list = load_system_asset_list("./asset_data.json")
    st.write(asset_list)

    cases_ref = db.collection("cases")
    cases = list(cases_ref.stream())  # Fetch data once and convert to a list
    case_list = []
    for case in cases:
        case_list.append(case.id)
    selected_case = st.selectbox("Select case", case_list)
    case_ref = db.collection("cases").document(selected_case)
    case = case_ref.get()

    if 'mapping_dict' not in st.session_state:
        st.session_state['mapping_dict'] = ""
        
    st.session_state['mapping_dict'] = case.to_dict()
    mapping_dict = st.session_state['mapping_dict']
    
    if 'updated_mapping_dict' not in st.session_state:
        st.session_state['updated_mapping_dict'] = st.session_state['mapping_dict']


    st.divider()  
    updated_mapping_dict = {}
    for key, value in mapping_dict.items():
        case_asset_colum, system_asset_column, delete_column = st.columns([2, 3, 1])
        with case_asset_colum:
            new_name = st.text_input("Asset name", key)
        with system_asset_column:
            new_selection = st.multiselect("System asset", asset_list, key = f"{key}_multiselect", default=value)
        
        updated_mapping_dict[new_name] = new_selection
        with delete_column:
            delete = st.button(f'Delete', key=f'{key}-b4')
            if delete:
                st.session_state['updated_mapping_dict'].pop(new_name)
                st.session_state['mapping_dict'].pop(new_name)
                # mapping_ref = db.collection("cases").document(selected_case)
                # mapping_ref.set(st.session_state['updated_mapping_dict'])
                st.success("Mapping deleted")
                st.rerun()
            ChangeButtonColour(f'Delete', 'white', 'red')
        #Create updated mapping dict

        st.session_state['updated_mapping_dict']= updated_mapping_dict

        st.divider()    
        
    add_button = st.button("Add mapping", use_container_width=True, type="secondary")

    if add_button:
        st.session_state['updated_mapping_dict']['New asset'] = []
        mapping_ref = db.collection("cases").document(selected_case)
        mapping_ref.set(st.session_state['updated_mapping_dict'])
        st.session_state['mapping_dict'] = st.session_state['updated_mapping_dict']
        st.success("Mapping added")
        st.rerun()


    save_button = st.button("Save mapping", use_container_width=True, type="primary")
    if save_button:
        mapping_ref = db.collection("cases").document(selected_case)
        mapping_ref.set(st.session_state['updated_mapping_dict'])
        st.session_state['mapping_dict'] = st.session_state['updated_mapping_dict']
        st.success("Mapping saved")
        st.rerun()

