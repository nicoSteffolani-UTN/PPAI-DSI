// cargar los datos del json en la tabla
class PantallaAdmReporteRanking {


    constructor(datePickerDesde, datePickerHasta, comboTipoReseña, comboVisualizacion, listaRanking) {
        this.datePickerDesde = datePickerDesde;
        this.datePickerHasta = datePickerHasta;
        this.comboTipoReseña = comboTipoReseña;
        this.comboVisualizacion = comboVisualizacion;
        this.listaRanking = listaRanking;
    }

    opcionGenerarRankingDeVinos() {
        window.open('../ranking.html', '_blank');
    }

    tomarFechaDesde() {
        return this.datePickerDesde.value;
    }

    tomarFechaHasta() {
        return this.datePickerHasta.value;
    }

    tomarTipoReseña() {
        return this.comboTipoReseña.value;
    }

    tomarTipoVisualizacion() {
        return this.comboVisualizacion.value;
    }


    validarFecha() {
        
        if (!this.tomarFechaDesde() || !this.tomarFechaHasta()) {
            alert("Por favor ingrese ambas fechas");
            return false;
        }

        if (new Date(this.tomarFechaDesde()) >= new Date(this.tomarFechaHasta())) {
            alert("La fecha desde debe ser menor que la fecha hasta");
            return false;
        }
        return true;
    }


    informarGeneracion(ranking) {
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


    async tomarConfirmacionReporte() {
        try {
            if (this.validarFecha()) {
                const fechaDesde = this.tomarFechaDesde();
                const fechaHasta = this.tomarFechaHasta();
                const tipoReseña = this.tomarTipoReseña();
                const tipoVisualizacion = this.tomarTipoVisualizacion();
                const url = `http://127.0.0.1:5000/?fechaDesde=${fechaDesde}&fechaHasta=${fechaHasta}&tipoReseña=${tipoReseña}&tipoVisualizacion=${tipoVisualizacion}`;
                const data = await fetch(url);
                const ranking = await data.json();

                this.informarGeneracion(ranking);
                
            }
        } catch (error) {
            console.log(error);
        }
    }
}

// Exportar la clase PantallaAdmReporteRanking
export { PantallaAdmReporteRanking };
