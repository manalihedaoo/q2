import streamlit as st
import pandas as pd 
import numpy as np
import base64
import xlrd
import openpyxl
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64
from PIL import Image
import time
from selenium.webdriver.support.ui import Select



# def take_screenshot():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     driver = webdriver.Chrome(options=chrome_options)
    
#     # Replace 'YOUR_STREAMLIT_APP_URL' with the URL of your Streamlit app
#     driver.get('http://localhost:8501/')
#     # vertical="POCL"
#     driver.set_window_size(1200, 1250)  # Set the desired window size
#     time.sleep(5)
    # drop_down_element = driver.find_element_by_id("vertical-dropdown")  # Replace 'vertical-dropdown' with the actual ID of your drop-down
    # dropdown_element = driver.find_element_by_xpath('//*[@id="vertical-dropdown"]')
    # dropdown_element=driver.find_element("xpath", '//*[@name="input"]')
    # select = Select(dropdown_element)

# Select an option by its value
    # select.select_by_value("POCL")  # Replace 'AUTO' with the value of the option you want to select
# Remember to replace 'vertical-dropdown' with the actual ID you used for your drop-down in Streamlit. Additionally, if your drop-down is inside an iframe or some other context, you might need to switch to that context using driver.switch_to.frame before finding the drop-down element.
    # time.sleep(10)
    
    # Save screenshot
    # screenshot_path = "screenshot.png"
    # driver.save_screenshot(screenshot_path)
    # driver.quit()
    # return screenshot_path

# def excel_to_datetime(excel_date):
#     dt = xlrd.xldate_as_datetime(excel_date, 0)  # 0 indicates the date system is 1900-based
#     return dt.strftime('%m-%d-%Y')

date_columns = ['Week Start', 'Week End']
daily = pd.read_excel('C:/Users/manalihedaoo/gamification/Dashboard/2023-07-23.xlsx',
                      parse_dates=['Week Start','Week End'],
                    #   date_parser=excel_to_datetime,
                      dtype={'Week Start': str, 'Week End': str})

# def set_margin(margin_size):
    # st.markdown(f"<style>div.stButton>button {{ margin: {margin_size}px; }}</style>", unsafe_allow_html=True)

# def function_from_app():

st.set_page_config(page_title="Landing Page", page_icon="🚀",layout="wide")   
    # st.header("Challengers")

def main():
    image = Image.open('background2.png')
    st.image(image)
    # set_margin(0)
    # Set page title and favicon
    # st.set_page_config(page_title="Landing Page", page_icon="🚀",layout="wide")
#     st.markdown(
    custom_css="""
    <style>
    .stApp {
         background-color: #f0f0f0; /* Dark Grey color *
        
    }
    </style>
    """
   
    
#     """
#     <style>
#     .centered-title {
#         text-align: center;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
    # Landing page content
    # st.markdown("<h1 class='centered-title';color: #800000;>Q2 CHAMPIONS LEAGUE</h1>", unsafe_allow_html=True)
    # st.title("Q2 CHAMPIONS LEAGUE")
    # st.write("17th July 2023 - 30th September 2023")
   
    # Add widgets and content to the sidebar
    # st.sidebar.title("Daily Tracker")
    # st.sidebar.write("This is the sidebar content of the Streamlit app.")
    # st.sidebar.markdown("You can add widgets, text, images, and other elements here.")

    # Add clickable buttons to the sidebar
    st.sidebar.title("Contender")
    if st.sidebar.button("Challengers"):
        st.write("You clicked 'Challengers' button!")
    # if st.sidebar.button("Warriors"):
    #     st.write("You clicked 'Warriors' button!")
    # if st.sidebar.button("Titans DMT SOT"):
    #     st.write("You clicked 'Titans DMT SOT' button!")
    # if st.sidebar.button("Titans SME"):
    #     st.write("You clicked 'Titans SME' button!")

    # if st.button('Save as JPEG'):

    # Capture the screenshot and save as 'streamlit_app_screenshot.jpg'
        # pyautogui.screenshot('streamlit_app_screenshot.jpg',region=(0, 0, 1200, 1250))
        # st.write('Screenshot saved as streamlit_app_screenshot.jpg')
    vertical_column_names = {
        "AUTO": {"Parameter1":"BUS.NO", 
                 "Parameter2":"BUS.NO Ach",
                "Parameter3":"CDCE%",
                "Parameter4":"CDCE% Ach",
                "Parameter5":"Combined Ach%"},
         "POCL": {"Parameter1":"BUS.NO", 
                 "Parameter2":"BUS.NO Ach",
                "Parameter3":"CDCE%",
                "Parameter4":"CDCE% Ach",
                "Parameter5":"Combined Ach%"},
        "CAR": {"Parameter1":"BUS.NO", 
                 "Parameter2":"BUS.NO Ach",
                "Parameter3":"CDCE%",
                "Parameter4":"CDCE% Ach",
                "Parameter5":"Combined Ach%"},
        "CV": {
            "Parameter1": "Bus.Fin Amt",
            "Parameter2": "BUS.Fin Amt Ach",
            "Parameter3": "%CD Coll Agst.CD Due",
            "Parameter4": "%CD Coll Agst. CD Due-Ach",
            "Parameter5": "Combined Ach%"
            },
        "FES": {
            "Parameter1": "BUS.NO",
            "Parameter2": "BUS.NO Ach",
            "Parameter3": "%CD Coll Agst.CD Due",
            "Parameter4": "%CD Coll Agst.CD Due-Ach",
            "Parameter5": "Combined Ach%"
        }
}

    #dropdown for verticals
    options = ["AUTO", "POCL", "FES", "CAR", "CV"]
    all_green=[]
    all_red=[]
    selected_option = st.selectbox("Select a vertical:", options, key='vertical-dropdown')
    st.write("You selected:", selected_option)

    # def download_csv():
        # csv = pd.read_csv('output.csv',dtype=str, header=None)
        # b64 = base64.b64encode(csv.encode()).decode()
        # transposed_df = df.T
        # output_file = 'output_challengers.csv'
        # transposed_df.to_csv(output_file, index=False)
        # b64 = base64.b64encode(open(output_file, "rb").read()).decode()
        # href = f'<a href="C:/Users/manalihedaoo/gamification/Dashboard/output_challengers.csv;base64,{b64}" download="output.csv">Download CSV file</a>'
        # return href

    def show_challengers_page():
        st.subheader("Challengers Landing Page")
        st.write("This is the Challengers Landing Page.")

    def highlight_color(val):
        print (val)
        if val in all_green:
            return 'background-color: green; color: white'
        elif val in all_red :
            return 'background-color: red; color: white'
        elif val.startswith("Match-") or val == "Leading":
             return "background-color: red; color: white"

        
    # def highlight_red_cells(val):
    #     # Check if the cell content is "Match-1", "Match-2", "Match-3", or "Leading"
    #     if val.startswith("Match-") or val == "Leading":
    #         return "background-color: blue; color: white"
    #     else:
    #         return ""
        
    def remove_element(arr, element_to_remove):
        # Use list comprehension to create a new array without the specified element
        new_array = [x for x in arr if x != element_to_remove]
        return new_array
    
    def GetCircleDetailforHtmlTable(data,vertical):
        html_table=[]
        # for eachCircle in data:
        #     data3= {
        #             "Circle": [eachCircle[0]],
        #             "BUS NO.": [eachCircle[1]],
        #             "BUS.NO ACH": [eachCircle[2]],
        #             "CDCDE%": [eachCircle[3]],
        #             "CDCE% Ach": [eachCircle[4]],
        #             "Combined Ach %": [eachCircle[5]],
        #             }
        column_names = vertical_column_names.get(vertical, {})
        for eachCircle in data:
            data3 = {
            column_names.get("Circle","Circle"):[eachCircle[0]],
            column_names.get("Parameter1"): [eachCircle[1]],
            column_names.get("Parameter2"): [eachCircle[2]],
            column_names.get("Parameter3"): [eachCircle[3]],
            column_names.get("Parameter4"): [eachCircle[4]],
            column_names.get("Parameter5"): [eachCircle[5]],
        }
            df3 = pd.DataFrame(data3) 
            writetoCsv(df3)
            df4=df3.T
            df4=df4.reset_index()
            df4.columns=df4.iloc[0]
            df4=df4[1:]
            html_table.append(df4) 
        return html_table

    def writetoCsv(df):
        # Save the DataFrames to a CSV files
        transposed_df = df.T
        transposed_df=transposed_df.reset_index()
        transposed_df.columns = transposed_df.iloc[0]
        transposed_df = transposed_df[1:]
        # transposed_df.columns=['a']
        output_file = 'output_challengers.csv'
        # Use 'index=False' to exclude the index column from being written to the CSV
        transposed_df.to_csv(output_file, mode='a', index=False)

    def getOneMatchDetails(df):
        df=df[1]
        main_array = df['Match'].split("vs")
        disb_target=df['METRIC 1 Target'].split("|")
        disb_ach=df['METRIC 1'].split("|")
        coll_target=df['METRIC 2 Target'].split("|")
        coll_ach=df['METRIC 2'].split("|")
        comb_target_ach=df['Combined % Target Achieved'].split("|")
        # comb_target_ach=float(comb_target_ach)
        comb_target_ach = [round(float(x),1) for x in comb_target_ach]
        comb_target_ach = [round(x) for x in comb_target_ach]
        # comb_target_ach = [round(float(x), 2) for x in comb_target_ach]
        # formatted_numbers = [f"{x:.2f}" for x in comb_target_ach]
        # comb_target_ach = [f"{x:.2f}" for x in comb_target_ach]
        # formatted_numbers = [format(x, ".2f") for x in comb_target_ach]
        # all_red.append(min(comb_target_ach))
        all_green.append(max(comb_target_ach))
        for each_element in remove_element(comb_target_ach,max(comb_target_ach)):
             all_red.append(each_element)

        final_array=[]
        for index in range(len(main_array)):
            # final_array.append([main_array[index],disb_target[index],disb_ach[index],coll_target[index],coll_ach[index],comb_target_ach[index],df['Match'],df['Leading']])
            match_data = [
            main_array[index],
            disb_target[index],
            disb_ach[index],
            coll_target[index],
            coll_ach[index],
            comb_target_ach[index],
            df['Match'],
            df['Leading']
            ]
            final_array.append(match_data)
            all_green.append(df['Leading'])
        return final_array

    vertical = selected_option #dropdown 
    auto_match=daily[(daily.Vertical==vertical)] 
    final_array =[]
    for each_row in auto_match.iterrows():
        new_array=getOneMatchDetails(each_row)
        final_array.append(new_array)
    
    def getStartEndWeek(df,vertical):
        df_vertical=df[df.Vertical==vertical]
        start_date=pd.to_datetime(df_vertical['Week Start'].iloc[0]).strftime('%m-%d-%Y')
        end_date=pd.to_datetime(df_vertical['Week End'].iloc[0]).strftime('%m-%d-%Y')
        return start_date,end_date
    
    start_date,end_date=getStartEndWeek(daily,vertical)
    data = {
        "Week-1": ["Week Start", "Week End"],
        vertical: [start_date,end_date],
    }
    
    # df = pd.DataFrame(data)
    # writetoCsv(df)
    # df = pd.DataFrame(df, index=[0])
    # st.table(df)
    # print(start_date)

    counter = 1
    num_matches = len(final_array)
    columns = st.columns(num_matches)
    # col_width = int(12 / num_matches)

    for eachCircle in final_array:
        match='Match - '+ str(counter)
        counter=counter+1
        data2= {
        match: [eachCircle[0][6]],
        "Leading": [eachCircle[0][7]]}
        df2 = pd.DataFrame(data2)
        writetoCsv(df2)
        df6=df2.T
        df6=df6.reset_index()
        df6.columns=df6.iloc[0]
        df6=df6[1:]
        # html_table.append(df6) 
    # df2 = pd.DataFrame(df2, index=None)
        # print(eachCircle[0])

        with columns[counter - 2]:  # Subtract 2 to make the counter zero-indexed
            # st.table(df2)
            styled_df = df2.style.applymap(highlight_color)

                # Display the styled DataFrame
            # styled_df = styled_df.reset_index(drop=True)
            st.write(styled_df, unsafe_allow_html=True)    
        # st.table(df2)
        # html_table2 = create_html_table(df2)
        # st.components.v1.html(html_table2)

        html_content=GetCircleDetailforHtmlTable(eachCircle,vertical)
        for each_table in html_content:
            with columns[counter - 2]:
                # st.table(each_table)
                styled_df = each_table.style.applymap(highlight_color)
                
                # st.DataFrame(df.style.format("{:.2}"))
                # Display the styled DataFrame
                # styled_df.format("{:.2}").write(st)
                st.write(styled_df, unsafe_allow_html=True)
            # html_table=create_html_table(each_table)
            # st.components.v1.html(html_table,height=150)
            
        # print(html_content)
        # st.markdown("<hr>", unsafe_allow_html=True)

    # st.table(df.style.hide_index())
    
    st.markdown(custom_css, unsafe_allow_html=True)

    # st.markdown(download_csv(), unsafe_allow_html=True)
    # Take a screenshot of the Streamlit app page
    # screenshot_path = take_screenshot()
   
    # Display the screenshot
    # st.subheader("Screenshot of the Streamlit App")
    # st.image(Image.open(screenshot_path), use_column_width=True)
    # if st.button('Take screenshot'):
        # take_screenshot()
   
if __name__ == "__main__":
    main()

    



