"""
Build a PyTorch model that can be used for prediction served out via FastAPI
"""

import io
import json

from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
import fastapi
from fastapi import File, UploadFile
import uvicorn

app = fastapi.FastAPI()

model = models.densenet121(weights="DenseNet121_Weights.IMAGENET1K_V1")
model.eval()
imagenet_class_index = json.load(open("imagenet_class_index.json", encoding="utf-8"))


def transform_image(image_bytes):
    my_transforms = transforms.Compose(
        [
            transforms.Resize(255),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    )
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    print(len(image_bytes))
    class_id, class_name = get_prediction(image_bytes=image_bytes)
    return {"class_id": class_id, "class_name": class_name}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
