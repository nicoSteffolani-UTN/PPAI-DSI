// cargar los datos del json en la tabla
class PantallaAdmReporteRanking {


    constructor(datePickerDesde, datePickerHasta, comboTipoReseña, comboVisualizacion, listaRanking) {
        this.datePickerDesde = datePickerDesde;
        this.datePickerHasta = datePickerHasta;
        this.comboTipoReseña = comboTipoReseña;
        this.comboVisualizacion = comboVisualizacion;
        this.listaRanking = listaRanking;     
    }

    pedirFechasReseña() {
        const fechaDesde = document.getElementById('fecha-desde');
        const fechaHasta = document.getElementById('fecha-hasta');
        this.datePickerDesde = fechaDesde;
        this.datePickerHasta = fechaHasta;
    }

    pedirTipoResena() {
        const tipoReseña = document.getElementById('tipo-reseña');
        this.comboTipoReseña = tipoReseña;
        tipoReseña.addEventListener('change', () => {
            this.cambiarTexto();
        });
    }

    pedirTipoVisualizacion() {
        const tabla = document.getElementById('lista-ranking');
        const comboVisualizacion = document.getElementById('tipo-visualizacion');
        this.listaRanking = tabla;
        this.comboVisualizacion = comboVisualizacion;
    }

    pedirConfirmacionReporte() {
        const btnConf = document.getElementById('btn-confirmar');
        const btnFin = document.getElementById('btn-fin');
        return [btnConf, btnFin];
    }

    opcionGenerarRankingDeVinos() {
        window.open('../ranking.html', '_self'); // Esto es el metodo habilitarPantalla()
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
                    <td style="text-align: center;">${vino[0]}</td>
                    <td style="text-align: center;">${vino[1]}</td>
                    <td style="text-align: center;">${vino[2]}</td>
                    <td style="text-align: center;">$${vino[3]}</td>
                    <td style="text-align: center;">${vino[4]}</td>
                    <td style="text-align: center;">${vino[5]}</td>
                    <td style="text-align: center;">${vino[6]}</td>
                    <td style="text-align: center;">${vino[7]}</td>
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

    cambiarTexto() {
        var menu = document.getElementById('tipo-reseña');
        var textoCambiante = document.getElementById('tipo-calificacion');
        if (menu.value === 'sommelier') {
            textoCambiante.textContent = 'Calificación de Sommelier';
        } else if (menu.value === 'amigos') {
            textoCambiante.textContent = 'Calificación de Amigos';
        } else {
            textoCambiante.textContent = 'Calificación Normal';
        }
    }

    finCU() {
        window.open('../index.html', '_self');
    }
}

// Exportar la clase PantallaAdmReporteRanking
export { PantallaAdmReporteRanking };
