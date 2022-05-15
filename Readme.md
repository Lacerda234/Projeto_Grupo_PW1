## Miniprojeto Petshop
  Levando em consideração a utilização da tecnologia no dia a dia atual, é de grande importância a integração da tecnologia com o agendamento de consultas em serviços para o bem-estar animal. E pensando nisso, este projeto sugere o desenvolvimento de um sistema de cadastro e agendamento online, que facilita ao usuário agendar consultas e serviços de pet shop, auxiliando proprietários de pet shops, veterinários e clientes na organização das consultas dos bichos de estimação.

# Como rodar o projeto

- Clone o projeto, para isso você pode simplesmente baixar o arquivo ou usar o git, para clonar diretamente do repositório remoto :
```
git clone https://github.com/ifpb-cz-ads/pw1-2021-2-ac-s14-miniprojeto-petshop.git
```

- Dentro do repositório, agora local, você precisa criar um novo ambiente virtual. Seja ele qual for, o próximo passo é acessa-lo e partir para a próxima etapa.

- Para ativar o ambiente virtual, se estiver usando linux ou Mac,use o seguinte comando :
```
source venv/bin/activate
```
- Se estiver usando windows use:
```
./venv/Scripts/Activate.ps1
```

- Após ativado, instalar todas as bibliotecas necessárias :
```
python -m pip install -r requirements.txt
```

- Não esqueça de rodas as migrations :
```
python manage.py makemigrations
```

- E então :
```
python manage.py migrate
```

- Feito isso, você pode iniciar a qualquer momento com :
```
python manage.py runserver
```

Por fim, acesse o site neste link : [http://localhost:8000/](http://localhost:8000/)
