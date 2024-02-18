import tkinter as tk
import customtkinter as ctk 

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

from PIL import ImageTk

from authtoken import auth_token


app = tk.Tk()
app.geometry("532x632")
app.title("Text to Image app")
app.configure(bg='black')
ctk.set_appearance_mode("dark") 

prompt = ctk.CTkEntry(app, height=40, width=512, text_color="white", fg_color="black") 
prompt.place(x=10, y=10)
prompt.configure(font=("Arial", 15))
img_placeholder = ctk.CTkLabel(app, height=512, width=512, text="")
img_placeholder.place(x=10, y=110)

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
stable_diffusion_model = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token) 
stable_diffusion_model.to(device) 

def generate_image(): 
 
    with autocast(device): 
        image = stable_diffusion_model(prompt.get(),guidance_scale=8.5)["sample"][0]
    
    image.save('generatedimage.png')
    
    img = ImageTk.PhotoImage(image)
    img_placeholder.configure(image=img) 


trigger = ctk.CTkButton(height=40, width=120, text_font=("Arial", 15), text_color="black", fg_color="white",
                         command=generate_image) 
trigger.configure(text="Generate")
trigger.place(x=206, y=60) 

app.mainloop()