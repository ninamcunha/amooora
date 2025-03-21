import streamlit as st
import pandas as pd

st.title('**Am:rainbow[ooo]ra**')

tab1, tab2 = st.tabs(["Home", "About"])

marital_status = ['Single', 'Available', 'Seeing someone', 'Married']

with tab1:
    with st.form("my_form"):
        name = st.text_input('Name', value="Francis",
                             placeholder='Your name here')
        age = st.number_input("What's your age?", step=1, value=32)
        status = st.selectbox('Marital status ', marital_status, index=1)
        sex = st.selectbox('Gender', ['', 'Female', 'Male'], index=1)
        orientation = st.selectbox(
            'Orientation ', ['', 'Bisexual', 'Gay', 'Straight'], index=1)
        body_type = st.selectbox('Body type ', [
                                 '', 'Athletic', 'Average', 'Curvy', 'Fit', 'Thin', 'Other', 'Not Disclosed'], index=1)
        drinks = st.selectbox(
            'Drinks 🍺🍸🍷', ['', 'Not at all', 'Often', 'Rarely', 'Socially'], index=1)
        diet = st.selectbox(
            'Diet', ['', 'Anything', 'Other', 'Vegetarian'], index=1)
        height = st.number_input('Height', format="%.2f", value=1.78)
        have_kids = st.selectbox('Do you have 👶(s)?', [
                                 '', 'More than one', 'One', 'Zero'], index=1),
        want_kids = st.selectbox('Do you want 👶(s)?', [
                                 '', 'Maybe', 'No', 'Yes'], index=1)
        like_dogs = st.selectbox('Do you like 🐶s?', ['', 'Yes', 'No'], index=1)
        has_dogs = st.selectbox('Do you have 🐶s?', ['', 'Yes', 'No'], index=1)
        like_cats = st.selectbox('Do you like 😺s?', ['', 'Yes', 'No'], index=1)
        has_cats = st.selectbox('Do you have 😺s?', ['', 'Yes', 'No'], index=1)
        religion = st.selectbox('Religion 🙏', [
                                '', 'Agnosticism', 'Atheism', 'Catholicism', 'Christianity', 'Judaism', 'Other'], index=1)
        smoke = st.selectbox('Do you smoke 🚬?', ['', 'Yes', 'No'], index=1)

'''

features=[‘female’, ‘age_scaled’, ‘single’,‘height_scaled’,‘orientation_bisexual’, ‘orientation_gay’,
     ‘orientation_straight’, ‘education_type_college_univ’, ‘education_type_grad_or_professional_edu’,
  ‘education_type_not_disclosed’,‘education_type_two_year_college_or_less’, ‘education_status_graduated’,
     ‘education_status_not_disclosed’, ‘education_status_working’,  ‘speaks_english’, ‘speaks_spanish’,
     ‘speaks_other’,‘diet_type_vegetarian’, ‘has_dogs_yes’, ‘no_of_kids_more_than_one’,‘no_of_kids_one’,
     ‘text_length_scaled’]

'''

eassay0 = st.text_area(
    "Tell us a bit about yourself",
    placeholder='I would love to think that I was some kind of intellectual...',
    value='I would love to think that I was some kind of intellectual...',
    height=100)
essay1 = st.text_area(
    "What I'm doing with my life?",
    placeholder='Currently working as an international agent for an NGO...',
    value='Currently working as an international agent for an NGO...',
    height=100)
essay2 = st.text_area(
    "I'm really good at",
    placeholder="I'm really good at listening and being there for my friends. I'm very dependable, honest and a great communicator.",
    value="I'm really good at listening and being there for my friends. I'm very dependable, honest and a great communicator.",
    height=100)
essay3 = st.text_area(
    "The first thing people notice about me...",
    placeholder="My eyes are the first thing people notice when they look and my sense of humor is what they notice when they talk to me.",
    value="My eyes are the first thing people notice when they look and my sense of humor is what they notice when they talk to me.",
    height=100)
essay4 = st.text_area(
    "Favorite books, movies, show, music and food",
    placeholder="I'm die hard christopher moore fan. I don't really watch a lot of tv unless there is humor involved. I'm kind of stuck on 90's alternative music. I'm pretty much a fan of everything though...I do need to draw a line at most types of electronica.",
    value="I'm die hard christopher moore fan. I don't really watch a lot of tv unless there is humor involved. I'm kind of stuck on 90's alternative music. I'm pretty much a fan of everything though...I do need to draw a line at most types of electronica.")
essay5 = st.text_area(
    "The six things I could never do without",
    placeholder='hot chocolate, running, a good meal, a good read, stimulating conversation, time alone to recharge, laughter, hope.... maybe 8 things...',
    value='hot chocolate, running, a good meal, a good read, stimulating conversation, time alone to recharge, laughter, hope.... maybe 8 things...'
)
essay6 = st.text_area(
    "I spend a lot of time thinking about",
    placeholder="my mind is always being distracted by planning some adventure out of the city, creating music and international travel.",
    value="my mind is always being distracted by planning some adventure out of the city, creating music and international travel."
)
essay7 = st.text_area(
    "On a typical friday night I am",
    placeholder='having dinner and drinks with friends and/or working',
    value='having dinner and drinks with friends and/or working'
)
essay8 = st.text_area(
    "The most private thing I am willing to admit",
    placeholder="when i was a kid i thought steven segal was really cool. please don't judge me.",
    value="when i was a kid i thought steven segal was really cool. please don't judge me."
)
essay9 = st.text_area(
    "You should message me if",
    placeholder="you want to be swept off your feet! you are tired of the norm. you want to catch a coffee or a bite. or if you want to talk philosophy.",
    value="you want to be swept off your feet! you are tired of the norm. you want to catch a coffee or a bite. or if you want to talk philosophy."
)
submitted = st.form_submit_button("Get recommendations!")
if submitted:
    params = dict(
        name=name,
        age=age,
        status=status,
        sex=sex,
        orientation=orientation,
        body_type=body_type,
        drinks=drinks,
        diet=diet,
        height=height,
        have_kids=have_kids,
        want_kids=want_kids,
        like_dogs=like_dogs,
        has_dogs=has_dogs,
        like_cats=like_cats,
        has_cats=has_cats,
        religion=religion,
        smoke=smoke,
        eassay0=eassay0,
        essay1=essay1,
        essay2=essay2,
        essay3=essay3,
        essay4=essay4,
        essay5=essay5,
        essay6=essay6,
        essay7=essay7,
        essay8=essay8,
        essay9=essay9,
    )
    st.markdown("### Submitted parameters:")
    st.write(params)
    st.write(pd.DataFrame(params))
with tab2:
    st.header("Le Wagon Data Science bootcamp final project")
