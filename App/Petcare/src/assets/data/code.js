

$(document).ready(function(){
  $("#food-button").click(function(){
    message = new Paho.MQTT.Message("4");
    message.destinationName = "haw/dmi/mt/its/petcare";
    client.send(message);
      $(".food-amount").toggleClass("button-active");
      $(".water-amount").removeClass("button-active");
  });
  $("#water-button").click(function(){
    message = new Paho.MQTT.Message("1");
    message.destinationName = "haw/dmi/mt/its/petcare";
    client.send(message);
      $(".water-amount").toggleClass("button-active");
      $(".food-amount").removeClass("button-active");
  });
});

// Create a client instance
client = new Paho.MQTT.Client("broker.mqttdashboard.com", Number(8000), "clientId-hyLO51dLlK");

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({onSuccess:onConnect});


// called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription and send a message.
  console.log("onConnect");
  client.subscribe("haw/dmi/mt/its/petcare");
  message = new Paho.MQTT.Message("Hello");
  message.destinationName = "haw/dmi/mt/its/petcare";
  client.send(message);
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:"+responseObject.errorMessage);
  }
}

// called when a message arrives
function onMessageArrived(message) {
  console.log("onMessageArrived:"+message.payloadString);
}
