# -*- coding: utf-8 -*-
import base64
import os
import json

base_dir = r"C:\Users\HP\.gemini\antigravity\scratch\wedding-invitation"
assets_dir = os.path.join(base_dir, "assets")
brain_dir = r"C:\Users\HP\.gemini\antigravity\brain\ef83a52c-d4e8-43ee-a994-00aba285c933"

def get_b64(name):
    p = os.path.join(assets_dir, name)
    with open(p, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")

print("Reading images to base64...")
envelope_img = get_b64("envelope-cover.jpg")
couples_img = get_b64("couples-art.jpg")
details_img = get_b64("card-details-ref.jpg")

print("Image sizes: envelope=", len(envelope_img), "couples=", len(couples_img))

# Save image data to a small json file so HTML generator can load it cleanly
with open(os.path.join(base_dir, "images.json"), "w", encoding="utf-8") as f:
    json.dump({
        "envelope": envelope_img,
        "couples": couples_img,
        "details": details_img
    }, f)

print("images.json successfully created.")
