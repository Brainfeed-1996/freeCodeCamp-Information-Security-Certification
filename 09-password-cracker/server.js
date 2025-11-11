const express = require('express');
const helmet = require('helmet');
const app = express();

app.use(helmet.noSniff());
app.use(helmet.xssFilter());
app.use(helmet.noCache());
app.use(helmet.hidePoweredBy({ setTo: 'PHP 7.4.3' }));

app.use(express.static('public'));

const server = require('http').createServer(app);
const io = require('socket.io')(server);

// ton code socket.io ici

server.listen(3000, () => console.log('Running on 3000'));
