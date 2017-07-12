let foodClick = 0;
let waterClick = 0;

$(document).ready(function(){

  // Choose the resource
  $("#food-button").click(function(){
    $(".food-amount").toggleClass("button-active");
    $(".water-amount").removeClass("button-active");
    foodClick++;
    if(foodClick%2==1 || waterClick%2==1){
      $(".scroll-content").animate({ scrollTop: $(document).height() }, 1000);
    }
  });
  $("#water-button").click(function(){
    waterClick++;
    if(foodClick%2==1 || waterClick%2==1){
      $(".scroll-content").animate({ scrollTop: $(document).height() }, 1000);
    }
    $(".water-amount").toggleClass("button-active");
    $(".food-amount").removeClass("button-active");
  });


  //Amount of food to be deployed
  $("#smallFood-btn").click(function(){
    message = new Paho.MQTT.Message("00");
    message.destinationName = "haw/dmi/mt/its/petcare";
    client.send(message);
    $(".food-amount").toggleClass("button-active");
  });
  $("#bigFood-btn").click(function(){
    message = new Paho.MQTT.Message("01");
    message.destinationName = "haw/dmi/mt/its/petcare";
    client.send(message);
    $(".food-amount").toggleClass("button-active");
  });

  //Amount of water to be deployed
  $("#smallWater-btn").click(function(){
    message = new Paho.MQTT.Message("10");
    message.destinationName = "haw/dmi/mt/its/petcare";
    client.send(message);
    $(".water-amount").toggleClass("button-active");
  });
  $("#bigWater-btn").click(function(){
    message = new Paho.MQTT.Message("11");
    message.destinationName = "haw/dmi/mt/its/petcare";
    client.send(message);
    $(".water-amount").toggleClass("button-active");
  });


});

// Create a client instance
client = new Paho.MQTT.Client("diginet.mt.haw-hamburg.de", Number(80), "clientId-hyLO51dLlK");
// client.username_pw_set('haw', password='schuh+-0');
// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;
var options = {
  timeout: 3,
  userName: "haw",
  password: "schuh+-0",
  onSuccess: onConnect,
  onFailure: function (message) {
    console.log("Connection failed: " + message.errorMessage);
  }
};
// connect the client
client.connect(options);


// called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription and send a message.
  console.log("onConnect");
  client.subscribe("haw/dmi/mt/its/petcare");
  // message = new Paho.MQTT.Message("Hello");
  // message.destinationName = "haw/dmi/mt/its/petcare";
  // client.send(message);
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
  if(message.payloadString != "00" && message.payloadString != "01" && message.payloadString != "10" && message.payloadString != "11"){
    let base64_encoded = message.payloadString;
    let image = "data:image/png;base64,"+base64_encoded;

    $("#security-cam").attr("src",image);
  }
}
