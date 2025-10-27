import os
import torch
from torch import nn as nn
import torchvision
from torchvision import transforms
from torchvision import models
from PIL import Image

efficient_net = models.efficientnet_b3(weights = None)

def dermat_predictions(image, model):
    transform = transforms.Compose([
        transforms.Resize((320, 320)),
        transforms.CenterCrop((300, 300)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])
    ])

    model.classifier = nn.Sequential(
        nn.Linear(1536, 512),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(512, 5)
    )

    model.load_state_dict(torch.load(r'D:\Final_Projects\Health_Project\PreDoc\predoc_app\models\efficient_net_dermat_model.pth'))

    transformed_image = transform(image).unsqueeze(0)

    with torch.inference_mode():
        output = model(transformed_image)
        _, preds = torch.max(output, 1)

    pred_disease = ['eczema', 'fungal_infections', 'melanocytic_nevi', 'psoriasis_lichen_planus', 'seborrheic_keratoses']
    return pred_disease[preds]





def oral_health_predictions(image, model):
    model.classifier = nn.Sequential(
        nn.Linear(1536, 512),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(512, 6)
    )

    transform = transforms.Compose([
        transforms.Resize((320, 320)),
        transforms.CenterCrop((300, 300)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])
    ])

    model.load_state_dict(torch.load(r'D:\Final_Projects\Health_Project\PreDoc\predoc_app\models\efficient_net_oral_model.pth'))

    transformed_image = transform(image).unsqueeze(0)

    with torch.inference_mode():
        output = model(transformed_image)
        _, preds = torch.max(output, 1)

    pred_disease = ['calculus', 'data caries', 'gingivitis', 'hypodontia', 'mouth ulcer', 'tooth discoloration']
    return pred_disease[preds]

def make_predictions(source, image, model = efficient_net):
    image = Image.open(image)

    if source == 'D':
        return dermat_predictions(image, model)

    elif source == 'O':
        return oral_health_predictions(image, model)
