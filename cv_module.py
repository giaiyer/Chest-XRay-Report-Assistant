import torchxrayvision as xrv
import torch
from PIL import Image
import numpy as np
import torchvision.transforms as T

def analyze_cxr(image_file):
    model = xrv.models.DenseNet(weights="densenet121-res224-all")
    model.eval()
    
    image = Image.open(image_file).convert('L')  
    transform = T.Compose([
        T.Resize((224, 224)),
        T.ToTensor(),
    ])
    img_tensor = transform(image)
    img_tensor = img_tensor.unsqueeze(0)  
    
    if img_tensor.shape[1] != 1:
        img_tensor = img_tensor.mean(dim=1, keepdim=True)
    
    with torch.no_grad():
        preds = model(img_tensor)
    preds = preds[0].cpu().numpy()
    
    labels = np.array(model.pathologies)
    top_indices = preds.argsort()[-3:][::-1]
    findings = [f"{labels[i]}: {preds[i]*100:.1f}%" for i in top_indices]
    return "\n".join(findings) 