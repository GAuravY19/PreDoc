
document.addEventListener("DOMContentLoaded", function() {
    const navbar = document.getElementById("navextend");
    const ham = document.getElementById("hamburgerbtn");
    const cross = document.getElementById("cross");

    ham.addEventListener("click", function(){
        navbar.classList.toggle("show");
    });

    cross.addEventListener("click", function(){
        navbar.classList.toggle("show");
    });
});

// const navbar = document.getElementById("navextend");

// function ShowingBurger() {
//     alert("function activated")
//     navbar.classList.toggle('show');
// }


