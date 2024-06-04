// cargar los datos del json en la tabla
class PantallaAdmReporteRanking {

    constructor(datePickerDesde, datePickerHasta, btnConfirmar, comboTipoResena, comboVisualizacion, listaRanking) {
        this.datePickerDesde = datePickerDesde;
        this.datePickerHasta = datePickerHasta;
        this.btnConfirmar = btnConfirmar;
        this.comboTipoResena = comboTipoResena;
        this.comboVisualizacion = comboVisualizacion;
        this.listaRanking = listaRanking;
    }

    validarFecha() {
        
        if (!this.datePickerDesde.value || !this.datePickerHasta.value) {
            alert("Por favor ingrese ambas fechas");
            return false;
        }

        if (new Date(this.datePickerDesde.value) >= new Date(this.datePickerHasta.value)) {
            alert("La fecha desde debe ser menor que la fecha hasta");
            return false;
        }
        return true;
    }

    async cargarDatos(req, res) {
        try {
            console.log('cargando datos');
            if (this.validarFecha()) {
                const fechaDesde = this.datePickerDesde.value;
                const fechaHasta = this.datePickerHasta.value;
                const url = `http://0.0.0.0:5000/?fechaDesde=${fechaDesde}&fechaHasta=${fechaHasta}`;
                const data = await fetch(url);
                const ranking = await data.json();
                

                const tabla = this.listaRanking;
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
    
}

// Exportar la clase PantallaAdmReporteRanking
export { PantallaAdmReporteRanking };
