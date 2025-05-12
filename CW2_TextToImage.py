import requests

'''
In this file, I rent a api from deepai,
just for the final step of generating image
because my own computer doesn't have enough computing ability.
'''

def Generate_Image(sentence):
    # DeepAI API for text to image processing
    API_URL = "https://api.deepai.org/api/text2img"

    # My personal API key -- only valid for one month
    API_KEY = "5ea09b5f-5d88-4ec7-9828-9fc3188afc0c"

    # set request header
    headers = {
        'api-key': API_KEY
    }

    # describing sentence
    data = {
        'text': f'{sentence}'
    }

    # send POST
    response = requests.post(API_URL, headers=headers, data=data)

    # check whether it works
    if response.status_code == 200:
        result = response.json()
        image_url = result['output_url']
        print(f"The link of generated image: {image_url}")
        # download the pic then save it
        img_response = requests.get(image_url)
        with open('generated_image.png', 'wb') as f:
            f.write(img_response.content)
        print("saved as generated_image.png")
        return image_url
    else:
        print(f"request failed, state code: {response.status_code}")
        print(response.text)
        return None

