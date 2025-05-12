import random

'''
There are 4 different kinds of agent.
Each one has special enhancing functions.
'''

# base agent class
class BaseAgent:
    def enhance(self, prompt):
        raise NotImplementedError("Subclasses must implement this method")


# Animal Agent - add the environment,action ...
class AnimalAgent(BaseAgent):
    def enhance(self, prompt):
        environments = [
            "in a lush jungle", "on snowy terrain", "in a desert", "deep in the forest",
            "swimming in the ocean", "in a zoo habitat", "in the wild savannah"
        ]
        actions = [
            "hunting its prey", "resting peacefully", "running freely", "playing with others",
            "howling to the sky", "roaring loudly", "camouflaged among trees"
        ]
        detail = random.choice(actions) + " " + random.choice(environments)
        return f"{prompt}, {detail}"


# Portrait Agent - intensify characteristic emotion, position and mood
class PortraitAgent(BaseAgent):
    def enhance(self, prompt):
        expressions = [
            "with a serene expression", "smiling softly", "with deep-set eyes",
            "looking confidently into the camera", "gazing into the distance",
            "laughing with joy", "in thoughtful silence"
        ]
        lighting = [
            "under natural light", "with cinematic lighting", "with a blurry background",
            "in a moody setting", "against a dark backdrop"
        ]
        accessories = [
            "wearing a vintage hat", "in elegant clothing", "with windblown hair",
            "holding a flower", "with a stylish jacket"
        ]
        return f"{prompt} {random.choice(expressions)}, {random.choice(lighting)}, {random.choice(accessories)}"


# Landscape Agent - add time, clime, vision elements
class LandscapeAgent(BaseAgent):
    def enhance(self, prompt):
        time_of_day = [
            "at sunrise", "during golden hour", "at dusk", "under a starry night", "in broad daylight"
        ]
        weather = [
            "with mist rolling in", "under a clear blue sky", "with storm clouds gathering",
            "bathed in sunlight", "covered in fog"
        ]
        elements = [
            "with a flowing river", "surrounded by pine trees", "featuring distant peaks",
            "with birds flying overhead", "with wildflowers blooming"
        ]
        return f"{prompt} {random.choice(time_of_day)}, {random.choice(weather)}, {random.choice(elements)}"


# Others Agent - intensify the style by using abstract descriptions
class OthersAgent(BaseAgent):
    def enhance(self, prompt):
        styles = [
            "in a minimalistic composition", "as an abstract artwork", "with surreal elements",
            "with glitch aesthetics", "as a conceptual piece"
        ]
        lighting = [
            "with high contrast shadows", "under neon lighting", "in black and white", "with vivid colors"
        ]
        perspective = [
            "seen from above", "in a close-up view", "with distorted proportions", "from a tilted angle"
        ]
        return f"{prompt}, {random.choice(styles)}, {random.choice(lighting)}, {random.choice(perspective)}"


# return corresponding agent according to labels
def get_agent(label):
    return {
        'animal': AnimalAgent(),
        'portrait': PortraitAgent(),
        'landscape': LandscapeAgent(),
        'others': OthersAgent()
    }.get(label, OthersAgent())


if __name__ == "__main__":
    label = 'portrait'
    prompt = "a young woman"
    agent = get_agent(label)
    enhanced_prompt = agent.enhance(prompt)
    print(enhanced_prompt)
