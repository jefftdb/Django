import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCmHLvUg-bxNv6Ro8285rNStzLywVN45EM",
  "authDomain": "receitas-7953c.firebaseapp.com",
  "databaseURL": "https://receitas-7953c-default-rtdb.firebaseio.com",
  "projectId": "receitas-7953c",
  "storageBucket": "receitas-7953c.appspot.com",
  "messagingSenderId": "624983484703",
  "appId": "1:624983484703:web:dd45c4420777ff6de7e82a",
  "measurementId": "G-VCPEQKGEVN"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

def siginup():
    email = input("Digite seu email: ")
    password = input("Digite sua senha: ")

    try:

        usuario = auth.create_user_with_email_and_password(email,password)
    except:
        print("Email ja cadastrado!")

def login():
    email = input("Digite seu email: ")
    password = input("Digite sua senha: ")

    try: 
    
        login = auth.sign_in_with_email_and_pass(email,password)
        print("logou no firebase")
    except:
        print("Email ou senha inválido!")


login()