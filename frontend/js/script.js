// cargar los datos del json en la tabla


function validarFecha() {
    var fechaDesde = document.getElementById('fecha-desde');
    var fechaHasta = document.getElementById('fecha-hasta');

    if (!fechaDesde.value || !fechaHasta.value) {
        alert("Por favor ingrese ambas fechas");
        return false;
    }

    if (new Date(fechaDesde.value) >= new Date(fechaHasta.value)) {
        alert("La fecha desde debe ser menor que la fecha hasta");
        return false;
    }
    return true;
}


const cargarDatos = async () => {
    try {
        console.log('cargando datos');
        if (validarFecha()) {

            const data = await fetch('http://127.0.0.1:5000/')
            const ranking = await data.json();


            const tabla = document.getElementById('lista-ranking');
            tabla.innerHTML = '';

            ranking.forEach((vino) => {

                const tr = `
                    <tr>
                        <td>${vino[0].nombre}</td>
                        <td>${vino[1]}</td>
                        <td>${vino[2]}</td>
                        <td>$${vino[0].precio}</td>
                        <td>${vino[0].bodega.nombre}</td>
                        <td>${vino[0].varietal.descripcion}</td>
                        <td>${vino[0].bodega.region.nombre}</td>
                        <td>${vino[0].bodega.region.provincia.pais.nombre}</td>
                    </tr>`;

                tabla.innerHTML += tr;
            });
        }
    } catch (error) {
        console.log(error);
    }

}
