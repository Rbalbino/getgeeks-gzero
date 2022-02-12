from faker import Faker
fake = Faker()

import bcrypt

def get_hashed_pass(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(8))
    return hashed


def users_to_insert_db():
    return [
        factory_user('login'),
        factory_user('be_geek'),
        factory_user('attempt_be_geek'),
        factory_user('field_alert'),
        factory_user('search_alien'),
        factory_user('search_common'),
        factory_user('searcher')
    ]


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

        'attempt_be_geek':{
            'name': 'Dio',
            'lastname':  'Lixux',
            'email': 'dio@linux.com',
            'password': 'pwd123',
            'geek_profile':{
                'whats': '31999999999',
                'desc': 'Instalo Distros Ubunto, Debian, ElementaryOS, POpOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, Red Hat, CentOS, Slackware, Gentoo, Archilnux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, Big Linux, ZorinOS, Unit',
                'printer_repair': 'Não',
                'work': 'Remoto',
                'cost': '150'
            }
        },

        'field_alert':{
            'name': 'Tony',
            'lastname': 'Stark',
            'email': 'tony@starkind.com',
            'password': 'pwd123',
        },
        'searcher':{
            'name': 'Jose',
            'lastname': 'Silva',
            'email': 'jose@silva.com.br',
            'password': 'pwd123'
        },
        'search_alien': {
            'name': 'Doctor',
            'lastname': 'Ocktavius',
            'email': 'doc.ock@oscorp.com',
            'password': 'pwd123',
            'geek_profile':{
                'whatsapp': '11999999999',
                'desc': 'Faço conserto de qualquer impressora. Matricial a fita, Matricial a fita colorida, a laser, a jato de tinta e também impressora 3D.',
                'printer_repair': 'Sim',
                'work': 'Presencial',
                'cost': '250'
            } 
        },
        'search_common': {
            'name': 'Petter',
            'lastname': 'Parker',
            'email': 'parker2@oscorp.com',
            'password': 'pwd123',
            'geek_profile':{
                'whatsapp': '11999998888',
                'desc': 'Faço instalação de distribuções Linux no seu computador PC X86 ou X64 com processadores Intel ou AMD. Pode ser o Linux Debian, Ubuntu, Mint, Fedora etc...',
                'printer_repair': 'Não',
                'work': 'Remoto',
                'cost': '200'
            } 
        },

    }

    return data[target]
