import json
import os

def load_templates():
    path = os.path.join(os.path.dirname(__file__), 'templates', 'cxr_templates.json')
    if not os.path.exists(path):
        return {'default': "Findings:\n{findings}\n\nImpression:\n..."}
    with open(path, 'r') as f:
        return json.load(f) 