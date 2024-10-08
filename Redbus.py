
import pandas as pd
import mysql.connector
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import time
from PIL import Image

# kerala bus
lists_kerala=[]
df_kerala=pd.read_csv("df_kerala.csv")
for i,r in df_kerala.iterrows():
    lists_kerala.append(r["Route_name"])

#Andhra bus
lists_Aandhra=[]
df_Aandhra=pd.read_csv("df_Aandhra.csv")
for i,r in df_Aandhra.iterrows():
    lists_Aandhra.append(r["Route_name"])

#Telungana bus
lists_Telungana=[]
df_Telungana=pd.read_csv("df_Telungana.csv")
for i,r in df_Telungana.iterrows():
    lists_Telungana.append(r["Route_name"])

#Goa bus
lists_Goa=[]
df_Goa=pd.read_csv("df_Goa.csv")
for i,r in df_Goa.iterrows():
    lists_Goa.append(r["Route_name"])

#Rajastan bus
lists_Rajastan=[]
df_Rajastan=pd.read_csv("df_Rajastan.csv")
for i,r in df_Rajastan.iterrows():
    lists_Rajastan.append(r["Route_name"])


# South bengal bus 
lists_South_Bengal=[]
df_South_Bengal=pd.read_csv("df_South_Bengal.csv")
for i,r in df_South_Bengal.iterrows():
    lists_South_Bengal.append(r["Route_name"])

# Haryana bus
lists_Haryana=[]
df_Haryana=pd.read_csv("df_Haryana.csv")
for i,r in df_Haryana.iterrows():
    lists_Haryana.append(r["Route_name"])

#Assam bus
lists_Assam=[]
df_Assam=pd.read_csv("df_Assam.csv")
for i,r in df_Assam.iterrows():
    lists_Assam.append(r["Route_name"])

#Uttra_pradesh bus
lists_Uttra_pradesh=[]
df_Uttra_pradesh=pd.read_csv("df_Uttra_pradesh.csv")
for i,r in df_Uttra_pradesh.iterrows():
    lists_Uttra_pradesh.append(r["Route_name"])

#West bengal bus
lists_West_bengal=[]
df_West_bengal=pd.read_csv("df_West_bengal.csv")
for i,r in df_West_bengal.iterrows():
    lists_West_bengal.append(r["Route_name"])

# # Home page setting
st.set_page_config(page_title="Streamlit Home Page", layout="wide")

# Sidebar with columns
with st.sidebar:
    st.title("Navigation")
    choice = st.radio("Go to", ("🏠Home", "🚌Booking"))

# Main page content based on sidebar selection
if choice == "🏠Home":
    st.title("🏠Welcome to the Home Page")
    st.image("C:/Users/Surenthiran/OneDrive/Desktop/Redbus_Project/redbus new.png",width=500)
    st.title("Redbus Data Scraping with Selenium & Streamlit")
    st.subheader(":blue[Domain:]  Transportation")
    st.subheader(":blue[Skill-take:]")
    st.markdown("Selenium, Python, Pandas, XAMPP,mysql-connector-python, Streamlit.")
    st.subheader(":blue[Developed-by:]  Surenthiran S")

elif choice == "🚌Booking":
    st.title("Routes Information")
    st.write("This section can be used to display information about Bus routes,Bus Type, Bus Timing.")

# Footer or any additional content
st.markdown("---")

# # States and Routes page setting
if choice  == "🚌Booking":
    S = st.selectbox("Lists of States", ["Kerala", "Aandhra", "Telungana", "Goa", "Rajastan", 
                                          "South_Bengal", "Haryana", "Assam", "Uttra_pradesh", "West_bengal"])
    
    col1,col2=st.columns(2)
    with col1:
        select_type = st.radio("Choose bus type", ("sleeper", "semi-sleeper", "others"))
    with col2:
        select_fare = st.radio("Choose bus fare range", ("50-1000", "1000-2000", "2000 and above"))
    TIME=st.time_input("select the time")

    # Kerala bus fare filtering
    if S == "Kerala":
        K = st.selectbox("List of routes",lists_kerala)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",port = 4000,user = "27BWX9vSyueH94y.root",password = "q1GlXoLTU7A9BpHQ")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM red_bus.bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

        # Aandhra bus fare filtering
    if S == "Aandhra":
        K = st.selectbox("List of routes",lists_Aandhra)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",port = 4000,user = "27BWX9vSyueH94y.root",password = "q1GlXoLTU7A9BpHQ")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM red_bus.bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

        #Telungana bus fare filtering
    if S == "Telungana":
        K = st.selectbox("List of routes",lists_Telungana)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",port = 4000,user = "27BWX9vSyueH94y.root",password = "q1GlXoLTU7A9BpHQ")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM red_bus.bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

        #Goa bus fare filtering
    if S == "Goa":
        K = st.selectbox("List of routes",lists_Goa)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",port = 4000,user = "27BWX9vSyueH94y.root",password = "q1GlXoLTU7A9BpHQ")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM red_bus.bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

     #Rajastan bus fare filtering
    if S == "Rajastan":
        K = st.selectbox("List of routes",lists_Rajastan)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",port = 4000,user = "27BWX9vSyueH94y.root",password = "q1GlXoLTU7A9BpHQ")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM red_bus.bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

        #South_Bengal bus fare filtering
    if S == "South_Bengal":
        K = st.selectbox("List of routes",lists_South_Bengal)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",port = 4000,user = "27BWX9vSyueH94y.root",password = "q1GlXoLTU7A9BpHQ")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM red_bus.bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

     #Haryana bus fare filtering
    if S == "Haryana":
        K = st.selectbox("List of routes",lists_Haryana)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",port = 4000,user = "27BWX9vSyueH94y.root",password = "q1GlXoLTU7A9BpHQ")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM red_bus.bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

     # Assam bus fare filtering
    if S == "Assam":
        K = st.selectbox("List of routes",lists_Assam)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",port = 4000,user = "27BWX9vSyueH94y.root",password = "q1GlXoLTU7A9BpHQ")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM red_bus.bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

     # Uttra_pradesh bus fare filtering
    if S == "Uttra_pradesh":
        K = st.selectbox("List of routes",lists_Uttra_pradesh)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",port = 4000,user = "27BWX9vSyueH94y.root",password = "q1GlXoLTU7A9BpHQ")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM red_bus.bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)

     # West_bengal bus fare filtering
    if S == "West_bengal":
        K = st.selectbox("List of routes",lists_West_bengal)

        def type_and_fare(bus_type, fare_range):
            mydb = mysql.connector.connect(host="localhost",user="root",password="")
            connection = mysql.connector.connect(host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",port = 4000,user = "27BWX9vSyueH94y.root",password = "q1GlXoLTU7A9BpHQ")
            mycursor = mydb.cursor(buffered=True)
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM red_bus.bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            mydb.commit()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)
