const loginForm = document.getElementById("loginForm");
const mensaje = document.getElementById("mensaje");

loginForm.addEventListener("submit", async function(event) {

    // Evitar que la página se recargue
    event.preventDefault();

    // Obtener los datos del formulario
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    // Validación básica
    if (!email || !password) {
        mensaje.textContent = "Completa todos los campos.";
        return;
    }

    try {

        // Enviar datos al backend
        const respuesta = await fetch("http://127.0.0.1:5000/login", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        // Convertir respuesta a JSON
        const datos = await respuesta.json();

        // Comprobar respuesta
        if (respuesta.ok) {

            mensaje.textContent = "Inicio de sesión exitoso.";

            // Guardar el token
            localStorage.setItem("token", datos.token);

            // Redirigir a la página principal
            setTimeout(() => {
                window.location.href = "RedSocial.html";
            }, 1000);

        } else {

            mensaje.textContent =
                datos.mensaje || "Correo o contraseña incorrectos.";

        }

    } catch (error) {

        console.error("Error:", error);

        mensaje.textContent =
            "No se pudo conectar con el servidor.";

    }

});