// cargar los datos del json en la tabla
// function validarFecha() {
//     var fechaDesde = document.getElementById('fecha-desde');
//     var fechaHasta = document.getElementById('fecha-hasta');

//     if (!fechaDesde.value || !fechaHasta.value) {
//         alert("Por favor ingrese ambas fechas");
//         return false;
//     }

//     if (new Date(fechaDesde.value) >= new Date(fechaHasta.value)) {
//         alert("La fecha desde debe ser menor que la fecha hasta");
//         return false;
//     }
//     return true;
// }


const cargarDatos = async () => {
    try {
        console.log('cargando datos');
        // if (validarFecha()) {
        const data = await fetch('http://127.0.0.1:5000')
        const ranking = await data.json();
        console.log(ranking);

        const tabla = document.getElementById('lista-ranking');
        tabla.innerHTML = '';

        ranking.forEach((vino) => {

            console.log(vino);
            const tr = `
                    <tr>
                        <td>${vino.Vino.nombre}</td>
                        <td>${vino.promedio}</td>
                        <td>${vino.promedioGeneral}</td>
                        <td>$${vino.Vino.precio}</td>
                        <td>${vino.Vino.bodega.nombre}</td>
                        <td>${vino.Vino.varietal.descripcion}</td>
                        <td>${vino.Vino.bodega.region.nombre}</td>
                        <td>${vino.Vino.bodega.region.provincia.pais.nombre}</td>
                    </tr>`;

            tabla.innerHTML += tr;
        });
        // }
    } catch (error) {
        console.log(error);
    }

}

cargarDatos();