import streamlit as st
from PIL import Image, ImageOps
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

def set_page_config():
    st.set_page_config(
        page_title='Caption an Image',
        page_icon=':camera:',
        layout='wide',
    )

def initialize_model():
    hf_model = "Salesforce/blip-image-captioning-large"
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    processor = BlipProcessor.from_pretrained(hf_model)
    model = BlipForConditionalGeneration.from_pretrained(hf_model).to(device)  # type: ignore
    return processor, model, device

def upload_image():
    return st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

def resize_image(image, max_width):
    width, height = image.size
    if width > max_width:
        ratio = max_width / width
        height = int(height * ratio)
        image = image.resize((max_width, height))
    return image

def apply_filter(image, filter_type):
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    if filter_type == 'Grayscale':
        return image.convert('L')
    elif filter_type == 'Posterize':
        return ImageOps.posterize(image, 3)
    return image

def generate_caption(processor, model, device, image):
    inputs = processor(image, return_tensors='pt').to(device)
    out = model.generate(**inputs, max_new_tokens=20)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def main():
    set_page_config()
    st.header("Caption an Image :camera:")

    # Initialize session state variables
    if "uploaded_images" not in st.session_state:
        st.session_state.uploaded_images = []
    if "captions" not in st.session_state:
        st.session_state.captions = []

    uploaded_image = upload_image()

    if uploaded_image is not None:
        image = Image.open(uploaded_image)

        # Filters from sidebar
        with st.sidebar:
            st.divider()
            filter_type = st.selectbox("Select a filter:", ["None", "Grayscale", "Posterize"])

        # Apply selected filter
        if filter_type != "None":
            image = apply_filter(image, filter_type)

        resized_image = resize_image(image, max_width=300)

        # Display image
        st.image(resized_image, caption='Your filtered image')

        # Generate caption
        with st.sidebar:
            if st.button('Generate Caption'):
                with st.spinner('Generating caption...'):
                    processor, model, device = initialize_model()
                    caption = generate_caption(processor, model, device, image)

                    # Add image and caption to the gallery
                    st.session_state.uploaded_images.append(resized_image)
                    st.session_state.captions.append(caption)

                    st.header("Caption:")
                    st.markdown(f'**{caption}**')

    # Display image gallery
    if st.session_state.uploaded_images:
        st.divider()
        st.subheader("Image Gallery")
        cols = st.columns(3)  # Create a grid of 3 columns
        for i, (img, cap) in enumerate(zip(st.session_state.uploaded_images, st.session_state.captions)):
            with cols[i % 3]:
                st.image(img, caption=cap, use_column_width=True)

if __name__ == '__main__':
    main()
