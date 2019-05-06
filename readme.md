Installe as dependências com o comando:
npm install

Inicie o servidor com o comando:
node server

Para testar use a URL:
http://localhost:3000/

Para requisições Post use: (JSON)

{
    "title": "teste",
    "description": "oi teste teste",
    "price": "50",
    "company": "faculdade"
}

OBS: Será necessário ESLint Extension para validar códigos para o conceito Clean Code.
Apenas 1 false positive foi detectado em:

module.exports = {
    url: 'mongodb+srv://thiagodraken:Shinryu1990!@cluster0-vg9fz.mongodb.net/test?retryWrites=true',
    serverport: 3000 
}

Ele informa que module não esta definido, é normal.