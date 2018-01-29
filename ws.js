var amqp = require('amqp');
var WebSocketServer = require('ws').Server

var connection = amqp.createConnection({host: 'localhost'});
var wss = new WebSocketServer({port:8000});

wss.on('connection',function(ws){

    ws.on('open', function() {
        console.log('connected');
        ws.send(Date.now().toString());
    });

    ws.on('message',function(message){
            console.log('Received: %s',message);
            ws.send(Date.now().toString());
    });
});

connection.on('ready', function(){
    connection.queue('MYQUEUE', {durable:true,autoDelete:false},function(queue){
            console.log(' [*] Waiting for messages. To exit press CTRL+C')
            queue.subscribe(function(msg){
                    console.log(" [x] Received from MYQUEUE %s",msg.data.toString('utf-8'));
                    payload = msg.data.toString('utf-8');
                    // HOW DOES THIS NOW GET SENT VIA WEBSOCKETS ??
            });
    });
});