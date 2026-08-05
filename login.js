const loginForm = document.getElementById("loginForm");
const mensaje = document.getElementById("mensaje");


loginForm.addEventListener("submit", async function(event){

    event.preventDefault();


  const email = document.getElementById("email").value;
const password = document.getElementById("password").value;

console.log("EMAIL:", email);
console.log("PASSWORD:", password);


    try {

        const respuesta = await fetch(
            "http://127.0.0.1:5000/login",
            {
                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({
                    email: email,
                    password: password
                })
            }
        );


        const datos = await respuesta.json();


    if(respuesta.ok){

    mensaje.style.color="green";
    mensaje.textContent="Login correcto";

    localStorage.setItem("token", datos.token);

    setTimeout(() => {
        window.location.href = "RedSocial.html";
    }, 1000);

}else{

    mensaje.style.color="red";
    mensaje.textContent = datos.error;

}


    }catch(error){

        mensaje.textContent=
        "Error conectando con el servidor";

        console.log(error);

    }


});