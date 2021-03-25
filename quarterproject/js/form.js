function formvalidation() {   
    var entirePage = document.getElementById("contact")
    //Generate thank you message
    entirePage.style.opacity = "0.2";
    //var div = document.createElement("div");
    //div.classList.add("fixedformmessage");
    //document.body.appendChild(div);
    //alert("your message has been received");

}

var entirePage = document.getElementById("contact")
var submitbutton = document.getElementById("submitbutton");

submitbutton.addEventListener('click', function(){
    var email = document.getElementById("email").value;
    var name = document.getElementById("name").value;
    var phone = document.getElementById("phonenumber").value; 
    var message= document.getElementById("message").value; 
    formvalidation();
    alert(`Thank you, ${name}, your response has been recorded`);
},false)