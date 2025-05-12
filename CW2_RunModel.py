from CW2_TextToImage import Generate_Image
from CW2_FuzzyMatch import correct_spelling
from CW2_AgentImplement import get_agent
from CW2_TestModelAccuracy import predict_text
from CW2_CLIP_Score import calculate_clip_score
from PIL import Image
import requests

'''
The all steps in this coursework.
'''

# 1. input the sentence
prompt = input("input sentence: ")

# 2. recognize the category
label = predict_text(prompt)
print("The category of sentence is:", label)

# 3. fuzzy match for correcting the incorrect words
prompt = correct_spelling(label, prompt)
print("Sentence corrected by fuzzy matching:", prompt)

# 4. use corresponding agent to enhance the prompt
agent = get_agent(label)
enhanced_prompt = agent.enhance(prompt)
print(enhanced_prompt)

# 5. generate the image
linkof_image = Generate_Image(enhanced_prompt)

# 6. CLIP socre
image = Image.open(requests.get(linkof_image, stream=True).raw)
CLIP_score = calculate_clip_score(image, prompt)
print(f"The clip score is:{CLIP_score:.2f}")

