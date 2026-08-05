const formulario = document.getElementById("registroForm");
const mensaje = document.getElementById("mensaje");

formulario.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const usuario = document.getElementById("usuario").value;
    const password = document.getElementById("password").value;
    const confirmar = document.getElementById("confirmPassword").value;

    if (password !== confirmar) {
        mensaje.textContent = "Las contraseñas no coinciden.";
        return;
    }

    try {

        const respuesta = await fetch("http://127.0.0.1:5000/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        const datos = await respuesta.json();

        if (respuesta.ok) {

            mensaje.style.color = "green";
            mensaje.textContent = datos.mensaje;

            formulario.reset();

        } else {

            mensaje.style.color = "red";
            mensaje.textContent = datos.error;

        }

    } catch (error) {

        mensaje.style.color = "red";
        mensaje.textContent = "No se pudo conectar con el servidor.";

    }
});