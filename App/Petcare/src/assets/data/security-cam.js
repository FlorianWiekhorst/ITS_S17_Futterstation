$(document).ready(function(){
  let base64_encoded = $("#base64").html();

  let image = "data:image/png;base64,"+base64_encoded;
  // image.src = "data:image/png;base64,"+base64_encoded;

  $("#security-cam").attr("src",image);
});
