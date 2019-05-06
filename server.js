// get dependencies
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// parse requests
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

//Enable CORS for all HTTP methods
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE, OPTIONS");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });

// Configuring the database
const config = require('./config.js');
const mongoose = require('mongoose');
require('./product.routes.js')(app);

mongoose.Promise = global.Promise;

// Connecting to the database
mongoose.connect(config.url, {
    useNewUrlParser: true
}).then(() => {
    console.log("Conexão com o banco de dados foi bem sucedida.");    
}).catch(err => {
    console.log('Não foi possível conectar ao banco de dados. Saindo agora ...', err);
    process.exit();
});

// default route
app.get('/', (req, res) => {
    res.json({"message": "Bem vindo à API para cadastrar produtos"});
});

// listen on port 3000
app.listen(config.serverport, () => {
    console.log("O servidor está escutando na porta 3000");
});