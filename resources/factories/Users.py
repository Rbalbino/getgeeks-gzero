from faker import Faker
fake = Faker()

import bcrypt

def get_hashed_pass(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(8))
    return hashed

def factory_user(target):

    data = {
        'faker':{
            'name': fake.first_name(),
            'lastname': fake.last_name(),
            'email': fake.free_email(),
            'password': 'pwd123' 
        },

        'wrong_email':{
            'name': 'Decio',
            'lastname': 'Petinine',
            'email': 'decio*msn.com',
            'password': 'abc123'  
        },

        'login':{
            'name': 'Rafael',
            'lastname': 'Balbino',
            'email': 'rafael@msn.com',
            'password': 'pwd123'
        },

        'be_geek':{
            'name': 'Kim',
            'lastname':  'Dotcom',
            'email': 'kim@dot.com',
            'password': 'pwd123',
            'geek_profile':{
                'whats': '11999999999',
                'desc': 'Seu computador está lento? Reiniciando do nada? Posso fazer a manutenção no seu PC, formatando, reinstalando o Sistema Operacional, trocando algum componente físico e porque não remover o baidú ou qualquer outro malware.',
                'printer_repair': 'Sim',
                'work': 'Remoto',
                'cost': '100'
            }     
        }
    }
    
    return data[target]
