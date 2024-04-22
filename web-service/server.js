//SERVER.JS--
const express = require('express');
const mongoose = require('mongoose');
const app = express();
//para conectar a MongoDB
mongoose.connect('mongodb://mongo-db:27017/mydatabase', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch(err => console.error('Error connecting to MongoDB', err));
app.get('/', (req, res) => {
    res.send("Welcome to my awesome app v2!");
});
app.listen(3000, function() {
    console.log("Web service listening on port 3000");
});
