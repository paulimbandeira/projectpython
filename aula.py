#!/usr/bin/env python
# coding: utf-8

# In[1]:


def temletrau():
    frase=input('Entre com uma frase: ')
    if 'u' in frase:
        print('vc usou a letra U')
    else:
        print('vc não usou a letra U')
        


# In[2]:


temletrau()


# In[3]:


def soma(a,b):
        soma=a+b
        return soma


# In[4]:


soma(5,10)


# In[9]:


def media(a,b):
    media=soma(a,b)/2
    return media


# In[14]:


media(8,10)


# In[31]:


def aprovacao(a,b):
    mediafinal = media(a,b)
    if mediafinal >= 7:
        print('aprovado')
    else:
        print('reprovado')
    return


# In[32]:


aprovacao(10,8)


# In[33]:


def convertetempo(f):
    c=(5*(f-32))/9
    return c


# In[34]:


convertetempo(212)


# In[43]:


def salario ():
    salario=int(input('Digite qual o seu salário: ',))
    if salario >= 5000:
        x = 0.27*salario
        salarioliquido = salario-x
        print (salarioliquido)
    elif salario > 2000 and salario < 5000:
        x = 0.15*salario
        print (salario)
    else:
        print('Você é isento')

    print (x)

    


# In[44]:


salario()


# In[45]:


def ano():
    atual=int(input('Digite o ano atual: '))
    nascimento=int(input('Digite o ano que vc nasceu: '))
    idade=atual-nascimento
    if idade >= 16:
        print('Pode votar')
    else:
        print('Não pode votar')
    


# In[46]:


ano()


# In[55]:


def aprovacao(a,b,c,d):
    media=(a+b+c+d)/4
    return media


# In[56]:


aprovacao(10,8,5,9)
    


# In[61]:


s = 'Olá, Mundo'
print(s[0])
print(s[2])
print(s[5])
print(s[0:3])


# In[63]:


s = 'Olá, Mundo'
print(s[:3])#retorna da posição 0 até a 2º, pois ele começa na posição 0
print(s[5:])#retorna a partir da 5º posição
print(s[:]) #retor toda a string


# In[1]:


cpf='013456789-01'
print(len(cpf))


# In[2]:


te='aula@gmail.com'
print(te[10])
print(len(te))


# In[2]:


texto = "aula@gmail.com"
x=texto.find("@")
print(x)


# In[3]:


texto = "aula@gmail.com"
x=texto.find('@')
print(x)


# In[4]:


texto = "aula@gmail.com"
posicao=texto.find('@')
print(texto[posicao:1])


# In[5]:


texto='testegmail.com'
posicao= texto.find('@')
print(texto[:posicao])


# In[6]:


texto='aula1@gmail.com'
achou=texto.endswith('gmail.com')
if achou:
    print('testo desejado encontrado')
else:
    print('não achou')


# In[7]:


salario=200
print('O salario é R${} reais' .format(salario))


# In[25]:


texto='joao123'
print(texto.isalnum())


# In[18]:


texto='joao123'
print(texto.isalpha())


# In[13]:


texto= input('entre apenas com numero! ')
if texto.isnumeric():
    print('ok , vc entrou apenas com numeros')
else:
    print('Invalido')
    


# In[14]:


texto='820.00'
novosalario=texto.replace('.',',')
print(novosalario)


# In[15]:


texto='paulo@gmail.com'
print(texto.split('@'))


# In[23]:


texto = 'paulo@gmail.com'
print(texto.startswith('paulo'))


# In[2]:


texto=input('Digite o seu e-mail com no maximo 25 caracteres: ').lower().strip()
if len(texto)<=25:
    if texto.endswith('gmail.com'):
        print(texto.replace('gmail.com','hotmail.com'))
    else:
        if texto.endswith('hotmail.com'):
            print(texto)
        else:
            print('E-mail não aceito')
else:
    print('e-mail maior que o permitido')


# In[1]:


email = input('Digite um e-mail válido:' ).lower().strip()
if len(email) <= 25:
    if email.endswith('gmail.com'):
        print(email.replace('gmail.com', 'hotmail.com'))
    else:
        print('E-mail inválido')
else:
    print('Email inválido, máximo 25 caracteres')


# In[ ]:




