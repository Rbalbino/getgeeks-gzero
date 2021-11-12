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
        },

        'short_desc':{
            'name': 'Zé',
            'lastname':  'Das Cove',
            'email': 'ze@cove.com',
            'password': 'pwd123',
            'geek_profile':{
                'whats': '21999999999',
                'desc': 'Formato o seu PC',
                'printer_repair': 'Não',
                'work': 'Ambos',
                'cost': '200' 
            } 
        },

        'long_desc':{
            'name': 'Dio',
            'lastname':  'Lixux',
            'email': 'dio@linux.com',
            'password': 'pwd123',
            'geek_profile':{
                'whats': '31999999999',
                'desc': 'Instalo Distros Ubunto, Debian, ElementaryOS, POpOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, Red Hat, CentOS, Slackware, Gentoo, Archilnux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, Big Linux, ZorinOS, Unity',
                'printer_repair': 'Não',
                'work': 'Remoto',
                'cost': '150'
            }
        } 
    }

    return data[target]
