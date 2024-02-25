import streamlit as st
import pandas as pd
import datetime
import time
from PIL import Image
from PIL import ImageGrab
import subprocess
#from openpyxl.workbook import Workbook

def home():
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        p = Image.open("banoqabil.png")
        st.image(p, caption=' ', width = 150)

    with col2:
        st.title("Al Khidmat Bano Qabil")

    with col3:
        l = Image.open("pythonlogo1.png")
        st.image(l, caption=' ', width = 260)
    st.header('This is a header with a divider', divider='rainbow')
    st.header('_ Sir.Ghufran Kamal_ is :blue[cool] :sunglasses:')    

def dataentry():
    st.header("Welcome to Our Car Selling Web Page")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        i = Image.open("ferrariimage.jpeg")
        st.image(i, caption='Ferrari', width=160)

    with col2:
        g = Image.open("lamborghiniimage.jpeg")
        st.image(g, caption='Lamborghini', width=170)

    with col3:
        t = Image.open("audiimage.jpeg")
        st.image(t, caption='Audi', width=160)

    with col4:
        y = Image.open("mercedesimage.jpeg")
        st.image(y, caption='Mercedes', width=170)
    df = pd.DataFrame({'Car Name': ['None','Lamborghini', 'Mercedes', 'Audi', 'Ferrari']})
    sel = st.selectbox("Which car do you want to buy", df['Car Name'])
   # col1, col2, col3, col4= st.columns([1,3,1,3])
    
    if sel == 'Lamborghini':
        col1, col2, col3, col4= st.columns([1,3,1,3])
        with col1:
            dict1 = {'Model': 1990, 'Color': 'Yellow', 'Price': 8520000}
            for keys, values in dict1.items():
                st.write(f"{keys} : {values}")
        with col2:
            k = Image.open("yellowlamborghini.jpeg")
            st.image(k, caption='Yellow Lamborghini', width = 210)
        with col3:
            dict1 = {'Model': 2010, 'Color': 'Black', 'Price' : 3520000}
            for keys, values in dict1.items():
                st.write(f"{keys} : {values}")
        with col4:
            k = Image.open("blacklamborghini.jpeg")
            st.image(k, caption='Black Lamborghini',width = 210)        

        sel2 = st.checkbox('1990')
        sel3 = st.checkbox('2010')
        
        if sel2:
           # form = st.form("Basic Form")
            st.warning(" Enter Name")
            name = st.text_input("Please Enter Your Name:")
            if name    :
                st.success("Filled")
                
            st.warning(" Enter Age")    
            age = st.text_input("Please Enter Your Age:")
            if age    :
                st.success("Filled")

            st.warning(" Enter cnic")
            cnic = st.text_input("Please Enter Your CNIC Number:")
            if cnic    :
                st.success("Filled")

            st.warning(" Enter valid city name")
            city = st.text_input("Please Enter Your City Name:")
            if city    :
                st.success("Filled")

            st.warning(" Enter Address")
            address = st.text_input("Please Enter correct address:")
            if address    :
                st.success("Filled")

            st.warning(" Enter correcr phone number")
            number = st.text_input("Please Enter Your Phone Number:")
            if number    :
                st.success("Filled")    

            st.warning('Please Enter valid date otherwise your order will be canceled')    
            dt = st.date_input("Please Enter Date of Registration:", datetime.date(2024, 2, 20))
            if st.button("Next"):
                progress_text = "Loading. Your data is saving"
                my_bar = st.progress(0, text=progress_text)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                st.write("Go to Save Data page")
                if 'user_data' not in st.session_state:
                    st.session_state.user_data = []
                st.session_state.user_data.append({'name': name, 'address':address,'Color': 'Yellow', 'car name': sel, 'age': age, 'date': dt, 'cnic':cnic, 'city': city, 'num': number, 'Price': 8520000, 'model year': 1990})
        if sel3:
           # form = st.form("Basic Form")
            st.warning(" Enter Name")
            name = st.text_input("Please Enter Your Name:")
            if name    :
                st.success("Filled")
            st.warning(" Enter Age")    
            age = st.text_input("Please Enter Your Age:")
            if age    :
                st.success("Filled")
            st.warning(" Enter cnic")
            cnic = st.text_input("Please Enter Your CNIC Number:")
            if cnic    :
                st.success("Filled")
            st.warning(" Enter valid city name")
            city = st.text_input("Please Enter Your City Name:")
            if city    :
                st.success("Filled")
            st.warning(" Enter Address")
            address = st.text_input("Please Enter correct address:")
            if address    :
                st.success("Filled")
            st.warning(" Enter correcr phone number")
            number = st.text_input("Please Enter Your Phone Number:")
            if number    :
                st.success("Filled")    
            st.warning('Please Enter valid date otherwise your order will be canceled')    
            dt = st.date_input("Please Enter Date of Registration:", datetime.date(2024, 2, 20))
            if st.button("Next"):
                progress_text = "Loading. Your data is saving"
                my_bar = st.progress(0, text=progress_text)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                st.write("Go to Save Data page")
                if 'user_data' not in st.session_state:
                    st.session_state.user_data = []
                st.session_state.user_data.append({'name': name, 'address':address,'Color': 'Black','Price' : 3520000, 'car name': sel, 'age': age, 'date': dt, 'cnic':cnic, 'city': city, 'num': number, 'model year': 1990})
        
                
    
    
    elif sel == 'Mercedes':
        col1, col2, col3, col4= st.columns([1,3,1,3])
        with col1:
            dict1 = {'Model': 1990, 'Color': 'Green', 'Price': 1220000}
            for keys, values in dict1.items():
                st.write(f"{keys} : {values}")
        with col2:
            k = Image.open("greenmercedes.jpeg")
            st.image(k, caption='Green Mercedes')
        with col3:
            dict1 = {'Model': 2010, 'Color': 'Blue', 'Price' : 720000}
            for keys, values in dict1.items():
                st.write(f"{keys} : {values}")
        with col4:
            k = Image.open("bluemercedes.jpeg")
            st.image(k, caption='Blue Mercedes')        

        sel2 = st.checkbox('1990')
        sel3 = st.checkbox('2010')
        
        if sel2:
           # form = st.form("Basic Form")
            st.warning(" Enter Name")
            name = st.text_input("Please Enter Your Name:")
            if name    :
                st.success("Filled")
                
            st.warning(" Enter Age")    
            age = st.text_input("Please Enter Your Age:")
            if age    :
                st.success("Filled")

            st.warning(" Enter cnic")
            cnic = st.text_input("Please Enter Your CNIC Number:")
            if cnic    :
                st.success("Filled")

            st.warning(" Enter valid city name")
            city = st.text_input("Please Enter Your City Name:")
            if city    :
                st.success("Filled")

            st.warning(" Enter Address")
            address = st.text_input("Please Enter correct address:")
            if address    :
                st.success("Filled")

            st.warning(" Enter correcr phone number")
            number = st.text_input("Please Enter Your Phone Number:")
            if number    :
                st.success("Filled")    

            st.warning('Please Enter valid date otherwise your order will be canceled')    
            dt = st.date_input("Please Enter Date of Registration:", datetime.date(2024, 2, 20))
            if st.button("Next"):
                progress_text = "Loading. Your data is saving"
                my_bar = st.progress(0, text=progress_text)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                st.write("Go to Save Data page")
                if 'user_data' not in st.session_state:
                    st.session_state.user_data = []
                st.session_state.user_data.append({'name': name, 'address':address,'Color': 'Green','Price': 1220000, 'car name': sel, 'age': age, 'date': dt, 'cnic':cnic, 'city': city, 'num': number, 'model year': 1990})
        if sel3:
           # form = st.form("Basic Form")
            st.warning(" Enter Name")
            name = st.text_input("Please Enter Your Name:")
            if name    :
                st.success("Filled")
            st.warning(" Enter Age")    
            age = st.text_input("Please Enter Your Age:")
            if age    :
                st.success("Filled")
            st.warning(" Enter cnic")
            cnic = st.text_input("Please Enter Your CNIC Number:")
            if cnic    :
                st.success("Filled")
            st.warning(" Enter valid city name")
            city = st.text_input("Please Enter Your City Name:")
            if city    :
                st.success("Filled")
            st.warning(" Enter Address")
            address = st.text_input("Please Enter correct address:")
            if address    :
                st.success("Filled")
            st.warning(" Enter correcr phone number")
            number = st.text_input("Please Enter Your Phone Number:")
            if number    :
                st.success("Filled")    
            st.warning('Please Enter valid date otherwise your order will be canceled')    
            dt = st.date_input("Please Enter Date of Registration:", datetime.date(2024, 2, 20))
            if st.button("Next"):
                progress_text = "Loading. Your data is saving"
                my_bar = st.progress(0, text=progress_text)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                st.write("Go to Save Data page")
                if 'user_data' not in st.session_state:
                    st.session_state.user_data = []
                st.session_state.user_data.append({'name': name, 'address':address,'Color': 'Blue','Price' : 720000, 'car name': sel, 'age': age, 'date': dt, 'cnic':cnic, 'city': city, 'num': number, 'model year': 1990})
    elif sel == 'Audi':
        col1, col2, col3, col4= st.columns([1,3,1,3])
        with col1:
            dict1 = {'Model': 1990, 'Color': 'Brown', 'Price': 100000}
            for keys, values in dict1.items():
                st.write(f"{keys} : {values}")
        with col2:
            k = Image.open("brownaudi.jpeg")
            st.image(k, caption='Brown Audi')
        with col3:
            dict1 = {'Model': 2010, 'Color': 'Yellow', 'Price' : 150000}
            for keys, values in dict1.items():
                st.write(f"{keys} : {values}")
        with col4:
            k = Image.open("yellowaudi.jpeg")
            st.image(k, caption='Yellow Audi')        

        sel2 = st.checkbox('1990')
        sel3 = st.checkbox('2010')
        
        if sel2:
           # form = st.form("Basic Form")
            st.warning(" Enter Name")
            name = st.text_input("Please Enter Your Name:")
            if name    :
                st.success("Filled")
                
            st.warning(" Enter Age")    
            age = st.text_input("Please Enter Your Age:")
            if age    :
                st.success("Filled")

            st.warning(" Enter cnic")
            cnic = st.text_input("Please Enter Your CNIC Number:")
            if cnic    :
                st.success("Filled")

            st.warning(" Enter valid city name")
            city = st.text_input("Please Enter Your City Name:")
            if city    :
                st.success("Filled")

            st.warning(" Enter Address")
            address = st.text_input("Please Enter correct address:")
            if address    :
                st.success("Filled")

            st.warning(" Enter correcr phone number")
            number = st.text_input("Please Enter Your Phone Number:")
            if number    :
                st.success("Filled")    

            st.warning('Please Enter valid date otherwise your order will be canceled')    
            dt = st.date_input("Please Enter Date of Registration:", datetime.date(2024, 2, 20))
            if st.button("Next"):
                progress_text = "Loading. Your data is saving"
                my_bar = st.progress(0, text=progress_text)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                st.write("Go to Save Data page")
                if 'user_data' not in st.session_state:
                    st.session_state.user_data = []
                st.session_state.user_data.append({'name': name, 'address':address,'Color': 'Brown','Price': 100000, 'car name': sel, 'age': age, 'date': dt, 'cnic':cnic, 'city': city, 'num': number, 'model year': 1990})
        if sel3:
           # form = st.form("Basic Form")
            st.warning(" Enter Name")
            name = st.text_input("Please Enter Your Name:")
            if name    :
                st.success("Filled")
            st.warning(" Enter Age")    
            age = st.text_input("Please Enter Your Age:")
            if age    :
                st.success("Filled")
            st.warning(" Enter cnic")
            cnic = st.text_input("Please Enter Your CNIC Number:")
            if cnic    :
                st.success("Filled")
            st.warning(" Enter valid city name")
            city = st.text_input("Please Enter Your City Name:")
            if city    :
                st.success("Filled")
            st.warning(" Enter Address")
            address = st.text_input("Please Enter correct address:")
            if address    :
                st.success("Filled")
            st.warning(" Enter correcr phone number")
            number = st.text_input("Please Enter Your Phone Number:")
            if number    :
                st.success("Filled")    
            st.warning('Please Enter valid date otherwise your order will be canceled')    
            dt = st.date_input("Please Enter Date of Registration:", datetime.date(2024, 2, 20))
            if st.button("Next"):
                progress_text = "Loading. Your data is saving"
                my_bar = st.progress(0, text=progress_text)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                st.write("Go to Save Data page")
                if 'user_data' not in st.session_state:
                    st.session_state.user_data = []
                st.session_state.user_data.append({'name': name, 'address':address,'Color': 'Yellow','Price' : 150000, 'car name': sel, 'age': age, 'date': dt, 'cnic':cnic, 'city': city, 'num': number, 'model year': 1990})
    elif sel == 'Ferrari':
        col1, col2, col3, col4= st.columns([1,3,1,3])
        with col1:
            dict1 = {'Model': 1990, 'Color': 'Red', 'Price': 9990000}
            for keys, values in dict1.items():
                st.write(f"{keys} : {values}")
        with col2:
            k = Image.open("ferrariimage.jpeg")
            st.image(k, caption='Red Ferrari')
        with col3:
            dict1 = {'Model': 2010, 'Color': 'Black', 'Price' : 10000000}
            for keys, values in dict1.items():
                st.write(f"{keys} : {values}")
        with col4:
            k = Image.open("blackferrari.jpeg")
            st.image(k, caption='Black Ferrari')        

        sel2 = st.checkbox('1990')
        sel3 = st.checkbox('2010')
        
        if sel2:
           # form = st.form("Basic Form")
            st.warning(" Enter Name")
            name = st.text_input("Please Enter Your Name:")
            if name    :
                st.success("Filled")
                
            st.warning(" Enter Age")    
            age = st.text_input("Please Enter Your Age:")
            if age    :
                st.success("Filled")

            st.warning(" Enter cnic")
            cnic = st.text_input("Please Enter Your CNIC Number:")
            if cnic    :
                st.success("Filled")

            st.warning(" Enter valid city name")
            city = st.text_input("Please Enter Your City Name:")
            if city    :
                st.success("Filled")

            st.warning(" Enter Address")
            address = st.text_input("Please Enter correct address:")
            if address    :
                st.success("Filled")

            st.warning(" Enter correcr phone number")
            number = st.text_input("Please Enter Your Phone Number:")
            if number    :
                st.success("Filled")    

            st.warning('Please Enter valid date otherwise your order will be canceled')    
            dt = st.date_input("Please Enter Date of Registration:", datetime.date(2024, 2, 20))
            if st.button("Next"):
                progress_text = "Loading. Your data is saving"
                my_bar = st.progress(0, text=progress_text)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                st.write("Go to Save Data page")
                if 'user_data' not in st.session_state:
                    st.session_state.user_data = []
                st.session_state.user_data.append({'name': name, 'address':address,'Color': 'Red', 'Price': 9990000, 'car name': sel, 'age': age, 'date': dt, 'cnic':cnic, 'city': city, 'num': number, 'model year': 1990})
        if sel3:
           # form = st.form("Basic Form")
            st.warning(" Enter Name")
            name = st.text_input("Please Enter Your Name:")
            if name    :
                st.success("Filled")
            st.warning(" Enter Age")    
            age = st.text_input("Please Enter Your Age:")
            if age    :
                st.success("Filled")
            st.warning(" Enter cnic")
            cnic = st.text_input("Please Enter Your CNIC Number:")
            if cnic    :
                st.success("Filled")
            st.warning(" Enter valid city name")
            city = st.text_input("Please Enter Your City Name:")
            if city    :
                st.success("Filled")
            st.warning(" Enter Address")
            address = st.text_input("Please Enter correct address:")
            if address    :
                st.success("Filled")
            st.warning(" Enter correcr phone number")
            number = st.text_input("Please Enter Your Phone Number:")
            if number    :
                st.success("Filled")    
            st.warning('Please Enter valid date otherwise your order will be canceled')    
            dt = st.date_input("Please Enter Date of Registration:", datetime.date(2024, 2, 20))
            if st.button("Next"):
                progress_text = "Loading. Your data is saving"
                my_bar = st.progress(0, text=progress_text)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                st.write("Go to Save Data page")
                if 'user_data' not in st.session_state:
                    st.session_state.user_data = []
                st.session_state.user_data.append({'name': name, 'address':address,'Color': 'Black', 'Price' : 10000000, 'car name': sel, 'age': age, 'date': dt, 'cnic':cnic, 'city': city, 'num': number, 'model year': 1990})

        st.session_state.page += 1

def datadisplay():
    st.title("Your Information")

    if 'user_data' in st.session_state:
        j = pd.DataFrame(st.session_state.user_data)
        st.dataframe(j)
    # Save DataFrame to Excel file
    #    j.to_excel('D:/user_data.xlsx', index=False)

    # Display records on the screen
       # st.title("Saved Records")
       # st.dataframe(j)

    # Display a success message
       # st.success("Data saved successfully as 'user_data.xlsx' and 'user_data.csv'")             

    st.write("If you want to add more cars then go back to Data Entry")            
    st.write("Are you sure that given information is correct?")

    if st.button("Yes"):
        j.to_excel('user_data.xlsx', index=False)
        st.success("Data saved successfully")
        st.write("For Confirm this registration take the mouse cursor on the table and then download this information by click on top right corner of this table and go to Contact us page ")

    if st.button("No"):
        st.write("Refresh this page and enter new information")


def senddata():
    st.title("Sending Information")
    st.write("Please send the downloaded file in this Email: ")

# Gmail link
    gmail_link = '<a href="https://mail.google.com/mail/u/0/#inbox?compose=new" target="_blank">waleedkamal801@gmail.com</a>'

# Display the link
    st.markdown(gmail_link, unsafe_allow_html=True)

    st.write("For further information or any query, Please contact in this Number :")
    st.write("0324-2923319")

def about():
    st.title("About us")
    
# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 1    

# Display image
# st.image(image, caption='Example Image', width=200,)
# st.image(g, caption='Example Image', width=200)

# st.title("Welcome to Our Car Selling Web Page")
st.sidebar.success("Name of Pages")
page = st.sidebar.radio("Go to", options=["Home","Data Entry", "Save Data", "Contact us","About us"])

if page == "Home":
    home()

elif page == "Data Entry":
    dataentry()

elif page == "Save Data":
    datadisplay()

elif page == "Contact us":
    senddata()
    
elif page == "About us":
    about()    


footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>If you are interested in sports car, you can visit here <a style='display: block; text-align: center;' href="https://www.motortrend.com/style/sports-car/" target="_blank">MotorTrend </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)    
