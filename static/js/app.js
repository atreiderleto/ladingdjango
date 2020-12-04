const formulario = document.getElementById('formulario');
const formulario2 = document.getElementById('formulario2');

formulario.addEventListener('submit', validarForm);
formulario.addEventListener('submit', validarForm2);

//valida el formulario  del modal.html
function validarForm (e) {
	e.preventDefault();

	const nombre = document.getElementById('nombre').value;
	const correo = document.getElementById('correo').value;
	const telefono = document.getElementById('telefono').value;
	const pais = document.getElementById('pais').value;

	if (nombre.trim() === '' || correo.trim() === '' || telefono.trim() === '' || pais.trim() =='' ) {

		alerta('Todos los campos son requeridos');
		formulario.appendChild(alerta);

		setTimeout(function(){ 
			alerta.remove(); 
		}, 4000);	

		return;
	}

	this.submit();
}



// crea un alerta para el formulario
function alerta(mensaje){
	alerta = document.createElement('p');
	alerta.classList.add('alert', 'alert-danger', 'text-center', 'mt-2');
	alerta.textContent = mensaje;
}