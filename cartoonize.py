import os
import PIL
import sys
import glob
import imageio
import logging
import argparse
import numpy as np
from tqdm import tqdm
from datetime import datetime
from style_transfer.cartoongan import cartoongan
import gradio as gr

STYLES = ["shinkai", "hayao", "hosoda", "paprika"]


parser = argparse.ArgumentParser(description="transform real world images to specified cartoon style(s)")

parser.add_argument("--keep_original_size", action="store_true",
                    help="by default the input images will be resized to reasonable size to prevent potential large "
                         "computation and to save file sizes. Enable this if you want the original image size.")

parser.add_argument("--max_resized_height", type=int, default=300,
                    help="specify the max height of a image after resizing. the resized image will have the same"
                         "aspect ratio. Set higher value or enable `keep_original_size` if you want larger image.")
args = parser.parse_args()




def image_mod(image,style):
    
    input_image = pre_image_processing(image,STYLES[style])
    model = (cartoongan.load_model(STYLES[style]))
    transformed_image = model.predict(input_image, use_multiprocessing=True)
    output_image = post_image_processing(transformed_image, style=STYLES[style])
    image = PIL.Image.fromarray(output_image.astype("uint8"))
    return image


iface = gr.Interface(image_mod, [gr.inputs.Image(type="pil"),gr.inputs.Dropdown(STYLES, type="index")], "image")
iface.launch()

def pre_image_processing(input_image, style, expand_dim=True):
    #input_image = PIL.Image.open(image_path).convert("RGB")

    if not args.keep_original_size:
        width, height = input_image.size
        aspect_ratio = width / height
        resized_height = min(height, args.max_resized_height)
        resized_width = int(resized_height * aspect_ratio)
        if width != resized_width:
            input_image = input_image.resize((resized_width, resized_height))

    input_image = np.asarray(input_image)
    input_image = input_image.astype(np.float32)

    input_image = input_image[:, :, [2, 1, 0]]

    if expand_dim:
        input_image = np.expand_dims(input_image, axis=0)
    return input_image



def post_image_processing(transformed_image, style):
    if not type(transformed_image) == np.ndarray:
        transformed_image = transformed_image.numpy()
    transformed_image = transformed_image[0]
    transformed_image = transformed_image[:, :, [2, 1, 0]]
    transformed_image = transformed_image * 0.5 + 0.5
    transformed_image = transformed_image * 255
    return transformed_image






