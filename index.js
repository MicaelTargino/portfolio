const express = require('express');
const app = express();

app.listen(3000, () => {
    console.log('server up and running on port 3000')
})

app.use(express.static(__dirname + '/public/'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html')
})

app.get('/sent', (req, res) => {
    res.sendFile(__dirname + '/sentEmail.html')
})