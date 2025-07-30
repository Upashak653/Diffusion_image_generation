import os
import replicate
from dotenv import load_dotenv
from PIL import Image as PILImage

load_dotenv()
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

output = replicate.run(
    "ideogram-ai/ideogram-v3-turbo",
    input={
        "prompt": "A 35 mm color film–style portrait of an young metal musician playing guitar under a single spotlight on a smoky stage. The shallow depth of field softly blurs the background, emphasizing the weathered textures of his face and the gleam of the brass instrument. Fine film grain and warm tones evoke a vintage documentary feel.",
        "resolution": "None",
        "style_type": "None",
        "aspect_ratio": "3:2",
        "magic_prompt_option": "Auto"
    }
)

try:
    output_path = "my-image1.png"
    with open(output_path, "wb") as f:
        f.write(output.read())  

    print(f" Image saved as '{output_path}'")
    try:
        img = PILImage.open(output_path)
        img.show() 
    except Exception as view_error:
        print(" Could not preview image:", view_error)

except Exception as e:
    print(" Error saving FileOutput:", e)
