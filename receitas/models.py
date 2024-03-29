from django.db import models
from datetime import datetime
import requests
from random import randint

from faker import Faker
# Create your models here.

# Faker Biblioteca que gera e simula dados 

def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')

class Receita():

    def montar_objeto(self,data,i):          

        self.id = data.json()[i]['id']
        self.title = data.json()[i]['title']
        self.description = data.json()[i]['description']
        self.slug =  i
        self.preparation_time = data.json()[i]['preparation_time']
        self.preparation_time_unit =  'Minutos'
        self.servings = data.json()[i]['servings']
        self.servings_unit = data.json()[i]['servings_unit']
        self.preparation_steps = data.json()[i]['preparation_steps']
        self.created_at_date = data.json()[i]['created_at_date'] 
        self.created_at_hour = data.json()[i]['created_at_hour'] 
        self.cover = data.json()[i]['cover'] 
        self.category = data.json()[i]['category']['name']
        self.author_first_name = data.json()[i]['author']['first_name']
        self.author_last_name = data.json()[i]['author']['last_name']
                                
        return (self)

    def criar(self,data_form,data):    
                   
        receita = {    
        
        'id': self.auto_increment(data),
        'title': data_form['title'][0],
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at_date': datetime.now().strftime("%d/%m/%Y"),
        'created_at_hour': datetime.now().strftime("%H:%M") ,
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%i/%i/food,cook' % rand_ratio(),
        }
    }

        return (receita)
    
    def atualizar(self,data_form,data,nome):
    
                   
        receita = {
            "id": data.json()[nome]['id'],
            'title': data_form['title'],
            'description': fake.sentence(nb_words=12),
            'preparation_time': fake.random_number(digits=2, fix_len=True),
            'preparation_time_unit': 'Minutos',
            'servings': fake.random_number(digits=2, fix_len=True),
            'servings_unit': 'Porção',
            'preparation_steps': fake.text(3000),
            'created_at_date': data.json()[nome]['created_at_date'],
            'created_at_hour': data.json()[nome]['created_at_hour'] ,
            'author': {
                'first_name': data_form['author'],
                'last_name': fake.last_name(),
            },
            'category': {
                'name': fake.word()
            },
            'cover': {
                'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
            }
                
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