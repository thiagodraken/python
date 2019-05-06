const Product = require('./product.model.js');

//Create new Product
exports.create = (req, res) => {
    // Request validation
    if(!req.body) {
        return res.status(400).send({
            message: "O conteúdo do produto não pode estar vazio"
        });
    }

    // Create a Product
    const product = new Product({
        title: req.body.title || "Nenhum título de produto", 
        description: req.body.description,
        price: req.body.price,
        company: req.body.company
    });

    // Save Product in the database
    product.save()
    .then(data => {
        res.send(data);
    }).catch(err => {
        res.status(500).send({
            message: err.message || "Algo errado ao recuperar produtos."
        });
    });
};

// Retrieve all products from the database.
exports.findAll = (req, res) => {
    Product.find()
    .then(products => {
        res.send(products);
    }).catch(err => {
        res.status(500).send({
            message: err.message || "Algo errado ao recuperar produtos."
        });
    });
};

// Find a single product with a productId
exports.findOne = (req, res) => {
    Product.findById(req.params.productId)
    .then(product => {
        if(!product) {
            return res.status(404).send({
                message: "Produto não encontrado com id " + req.params.productId
            });            
        }
        res.send(product);
    }).catch(err => {
        if(err.kind === 'ObjectId') {
            return res.status(404).send({
                message: "Produto não encontrado com id " + req.params.productId
            });                
        }
        return res.status(500).send({
            message: "Algo errado ao recuperar o produto com o id " + req.params.productId
        });
    });
};

// Update a product
exports.update = (req, res) => {
    // Validate Request
    if(!req.body) {
        return res.status(400).send({
            message: "O conteúdo do produto não pode estar vazio"
        });
    }

    // Find and update product with the request body
    Product.findByIdAndUpdate(req.params.productId, {
        title: req.body.title || "Nenhum título de produto", 
        description: req.body.description,
        price: req.body.price,
        company: req.body.company
    }, {new: true})
    .then(product => {
        if(!product) {
            return res.status(404).send({
                message: "Produto não encontrado com id " + req.params.productId
            });
        }
        res.send(product);
    }).catch(err => {
        if(err.kind === 'ObjectId') {
            return res.status(404).send({
                message: "Produto não encontrado com id " + req.params.productId
            });                
        }
        return res.status(500).send({
            message: "Algo errado ao atualizar nota com o id " + req.params.productId
        });
    });
};

// Delete a note with the specified noteId in the request
exports.delete = (req, res) => {
    Product.findByIdAndRemove(req.params.productId)
    .then(product => {
        if(!product) {
            return res.status(404).send({
                message: "Produto não encontrado com id " + req.params.productId
            });
        }
        res.send({message: "Produto excluído com sucesso!"});
    }).catch(err => {
        if(err.kind === 'ObjectId' || err.name === 'NotFound') {
            return res.status(404).send({
                message: "Produto não encontrado com id " + req.params.productId
            });                
        }
        return res.status(500).send({
            message: "Não foi possível excluir o produto com o ID " + req.params.productId
        });
    });
};