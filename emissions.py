import pickle
import streamlit as st
import azureml.train.automl

# loading the trained model
pickle_in = open('forecaster.pkl', 'rb') 
forecaster = pickle.load(pickle_in)

# Defining country options
countries = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", 
             "Antigua and Barbuda", "Arab World", "Argentina", "Armenia", "Aruba", "Australia", 
             "Austria", "Azerbaijan", "Bahamas, The", "Bahrain", "Bangladesh", "Barbados", 
             "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", 
             "Bosnia and Herzegovina", "Botswana", "Brazil", "British Virgin Islands", 
             "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", 
             "Cambodia", "Cameroon", "Canada", "Caribbean small states", "Cayman Islands", 
             "Central African Republic", "Central Europe and the Baltics", "Chad", "Channel Islands", 
             "Chile", "China", "Colombia", "Comoros", "Congo, Dem. Rep.", "Congo, Rep.", 
             "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Curacao", "Cyprus", "Czech Republic", 
             "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Early-demographic dividend", 
             "East Asia & Pacific", "East Asia & Pacific (excluding high income)", 
             "East Asia & Pacific (IDA & IBRD)", "Ecuador", "Egypt, Arab Rep.", "El Salvador", 
             "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Euro area", 
             "Europe & Central Asia", "Europe & Central Asia (excluding high income)", 
             "Europe & Central Asia (IDA & IBRD)", "European Union", "Faroe Islands", "Fiji", 
             "Finland", "Fragile and conflict affected situations", "France", "French Polynesia", 
             "Gabon", "Gambia, The", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", 
             "Greenland", "Grenada", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", 
             "Haiti", "Heavily indebted poor countries (HIPC)", "High income", "Honduras", 
             "Hong Kong SAR, China", "Hungary", "IBRD only", "Iceland", "IDA & IBRD total", 
             "IDA blend", "IDA only", "IDA total", "India", "Indonesia", "Iran, Islamic Rep.", 
             "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jordan", 
             "Kazakhstan", "Kenya", "Kiribati", "Korea, Dem. People's Rep.", "Korea, Rep.", 
             "Kosovo", "Kuwait", "Kyrgyz Republic", "Lao PDR", "Late-demographic dividend", 
             "Latin America & Caribbean", "Latin America & Caribbean (excluding high income)", 
             "Latin America & Caribbean (IDA & IBRD)", "Latvia", 
             "Least developed countries: UN classification", "Lebanon", "Lesotho", "Liberia", 
             "Libya", "Liechtenstein", "Lithuania", "Low & middle income", "Low income", 
             "Lower middle income", "Luxembourg", "Macao SAR, China", "Madagascar", "Malawi", 
             "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", 
             "Mauritius", "Mexico", "Micronesia, Fed. Sts.", "Middle East & North Africa",
             "Middle East & North Africa (excluding high income)", 
             "Middle East & North Africa (IDA & IBRD)", "Middle income", "Moldova", "Monaco", 
             "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru",
             "Nepal", "Netherlands", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria",
             "North America", "North Macedonia", "Northern Mariana Islands", "Norway", "OECD members", 
             "Oman", "Other small states", "Pacific island small states", "Pakistan", "Palau", 
             "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", 
             "Post-demographic dividend", "Pre-demographic dividend", "Puerto Rico", "Qatar", 
             "Romania", "Russian Federation", "Rwanda", "Samoa", "San Marino", "Sao Tome and Principe", 
             "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", 
             "Sint Maarten (Dutch part)", "Slovak Republic", "Slovenia", "Small states", 
             "Solomon Islands", "Somalia", "South Africa", "South Asia", "South Asia (IDA & IBRD)", 
             "South Sudan", "Spain", "Sri Lanka,St. Kitts and Nevis", "St. Lucia", 
             "St. Martin (French part)", "St. Vincent and the Grenadines", "Sub-Saharan Africa",
             "Sub-Saharan Africa (excluding high income)", "Sub-Saharan Africa (IDA & IBRD)",
             "Sudan", "Suriname", "Sweden", "Switzerland", "Syrian Arab Republic", "Tajikistan", 
             "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia",
             "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", 
             "United Arab Emirates", "United Kingdom", "United States", "Upper middle income", 
             "Uruguay", "Uzbekistan", "Vanuatu" ,"Venezuela, RB", "Vietnam", "Virgin Islands (U.S.)", 
             "West Bank and Gaza", 'World', "Yemen, Rep.", "Zambia", "Zimbabwe"]

@st.cache()

# defining the function which will make the 
# prediction using the data which the user inputs 
def prediction(country, year):   

    # pre-process user input
    year = str(year)+'-01-01T00:00:00.000Z'

    # make predictions
    prediction = forecaster.predict([[country, year]])

    return prediction


# the main function in which we define our webpage

def main():       
    #front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:lightblue;padding:13px"> 
    <h1 style ="color:black;text-align:center;">CO2 Emissions ML Prediction App</h1> 
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

    # following lines create boxes in which user can enter data 
    # required to make prediction 
    country = st.selectbox("Country", countries, help="Please choose the country for prediction")
    year = st.slider("Year", min_value=2019, max_value=2040, value=None, step=1, 
                     help="Please enter year for prediction between 2019 and 2040")
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"): 
        result = prediction(country, year)
        st.success('The CO2 emissions are {} metric tons per capita'.format(result))
        print(prediction)

if __name__=='__main__': 
    main()