from openai import OpenAI
import streamlit as st 
from apikey import apikey
from streamlit_carousel import carousel

client = OpenAI(api_key=apikey)

single_image = dict(
        title = "",
        text = "",
        interval = None,
        img = "",
    )

def generate_images(image_description, num_of_images):
    image_gallery = []
    for i in range(num_of_images):
        image_response = client.images.generate(
            model= "dall-e-3",
            prompt= image_description,
            size = "1024x1024",
            quality= "standard",
            n=1
        )
        
        image_url = image_response.data[0].url
        new_image=single_image.copy()
        new_image["title"]=f"Image {i+1}"
        new_image["text"]=image_description
        new_image["img"]=image_url
        image_gallery.append(new_image)
    return image_gallery

st.set_page_config(page_title="Dalle-Image-Generation", page_icon=":picture:", layout="wide")
st.title("Image Generation Tool")
image_description = st.text_input("Please enter a description for the image that you would like to generate!")
num_of_images = st.number_input("Please select the number of images that will be generated",min_value=1, value=1, max_value=10)

if st.button("Generate Image"):
    generate_image = generate_images(image_description, num_of_images)

    carousel(items=generate_image,width=1)