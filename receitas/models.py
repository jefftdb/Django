from django.db import models
from datetime import datetime
import requests
# Create your models here.

class Receita():
    def criar(self,data_form,data):
    
                   
        receita = {
            "id": self.auto_increment(data),
            "ingredientes":data_form['ingrediente'],
            "nome": data_form['nome'][0],
            "data_publicacao": datetime.now().strftime("%d/%m/%Y"),
            "hora": datetime.now().strftime("%H:%M")
        }

        return (receita)
    
    def atualizar(self,data_form,data,nome):
    
                   
        receita = {
            "id": data.json()[nome]['id'],
            "ingredientes":data_form['ingrediente'],
            "nome": data_form['nome'][0],
            "data_publicacao": data.json()[nome]['data_publicacao'],
            "hora": data.json()[nome]['hora']
        }

        return (receita)
    
    def auto_increment(self,data):
        if data.json() == None:
            id = 0
        else:
            for nome in data.json():
                ultimo = requests.get('https://receitas-7953c-default-rtdb.firebaseio.com/receitas/'+ nome +'.json')
                id = ultimo.json()['id'] + 1
        return id