# -*- coding: utf-8 -*-
import base64
import os
import json

base_dir = r'C:\Users\HP\.gemini\antigravity\scratch\wedding-invitation'
assets_dir = os.path.join(base_dir, 'assets')
brain_dir = r'C:\Users\HP\.gemini\antigravity\brain\ef83a52c-d4e8-43ee-a994-00aba285c933'

def get_b64(name):
    with open(os.path.join(assets_dir, name), 'rb') as f:
        return 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

envelope_img = get_b64('envelope-cover.jpg')
couples_img = get_b64('couples-art.jpg')
card_img = get_b64('card-details-ref.jpg')

print('Images converted to base64 successfully.')
