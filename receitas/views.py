from django.http import HttpResponse,QueryDict
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from receitas.models import Receita



@csrf_exempt  
def receitas(request):         
    data = requests.get('https://receitas-7953c-default-rtdb.firebaseio.com/receitas.json')
   
    if request.method == 'GET': #Obter todos os registros de receitas.
        receitas=[]
      
        for i in dict(data.json()):
            receita = Receita()
            receitas.append(receita.montar_objeto(data,i))


        return render(request, 'receitas/pages/home.html', context={
        'receitas': receitas,
    })
        
                            
                            
    elif request.method == 'POST': #Insere uma nova receita.

        data_form = request.POST
        
        receita = Receita()
        arquivo = receita.criar(dict(data_form), data)        


        requisicao = requests.post("https://receitas-7953c-default-rtdb.firebaseio.com/receitas.json", json= arquivo)
        
        return HttpResponse(requisicao)



@csrf_exempt  
def receita(request,id): 
    data = requests.get('https://receitas-7953c-default-rtdb.firebaseio.com/receitas.json')
    
    
    for i in dict(data.json()):
        if int(data.json()[i]['id']) == int(id):                
                receita = Receita()
                receita.montar_objeto(data,i) 

    if request.method == 'GET': #Obter a receita pelo id.   
                                     
        return render(request, 'receitas/pages/recipe-view.html', context={
        'recipe': receita,
    })
    
    elif request.method == 'POST': #Edita a receita pelo id          

        data_form = request.POST

                
        arquivo = receita.atualizar(data_form, data,receita.slug)

        requisicao = requests.put("https://receitas-7953c-default-rtdb.firebaseio.com/receitas/"+ receita.slug +".json", json=dict(arquivo))
                                   
        return render(request, 'receitas/pages/recipe-view.html', context={
        'recipe': receita,
    })
    
    elif request.method == 'DELETE': #Deleta a receita

        requisicao = requests.delete("https://receitas-7953c-default-rtdb.firebaseio.com/receitas/"+ receita.slug +".json")
    
        return HttpResponse(requisicao.status_code)# Envia a mensagem 200 se foi deletado com sucesso


    
        