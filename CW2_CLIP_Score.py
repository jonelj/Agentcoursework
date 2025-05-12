import torch
from PIL import Image
import requests
from transformers import CLIPProcessor, CLIPModel

'''
This file designed to demonstrate 
the CLIP score between text and generated image
'''

# load pre-trained CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


def calculate_clip_score(image, text):
    """
    calculate CLIP Score
    :param image: PIL.Image
    :param text: text description
    :return: CLIP Score (range [-1, 1]，The higher the value, the stronger the correlation.)
    """
    if isinstance(image, str):
        image = Image.open(image)

    inputs = processor(text=text, images=image, return_tensors="pt", padding=True)

    with torch.no_grad():
        outputs = model(**inputs)

    image_features = outputs.image_embeds
    text_features = outputs.text_embeds

    clip_score = torch.cosine_similarity(image_features, text_features, dim=1).item()
    return clip_score


# test
if __name__ == "__main__":
    url = "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba"
    image = Image.open(requests.get(url, stream=True).raw)
    text = "a cat on a grassy field"
    score = calculate_clip_score(image, text)
    print(f"CLIP Score : {score:.4f}")
