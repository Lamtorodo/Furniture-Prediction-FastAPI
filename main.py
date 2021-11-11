from fastapi import FastAPI , Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn
from schemas import Furniture
import pickle
import numpy as np 

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
model = pickle.load(open('model.pkl','rb'))
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.post('/predict')
async def predict(request: Request,form_data: Furniture = Depends(Furniture.as_form)):

    '''
    pour l'affichage sur html
    '''
    prediction =model.predict(
				[
				[
				form_data.category,
				form_data.sellable_online,
				form_data.other_colors,
				form_data.depth,
                form_data.height,
                form_data.width,

				]])
    prediction_text='Furniture prediction price is : $ {}'.format(prediction)
    return templates.TemplateResponse("index.html", {"request": request,"prediction_text":prediction_text })
if __name__ == '__main__':
		uvicorn.run("app:app",
		 host="0.0.0.0",
		 port =8080 ,
		 reload = True)	