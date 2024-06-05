import { PantallaAdmReporteRanking } from './PantallaAdmReporteRanking.js';

const tabla = document.getElementById('lista-ranking');
const fechaDesde = document.getElementById('fecha-desde');
const fechaHasta = document.getElementById('fecha-hasta');
const btnConfirmar = document.getElementById('btn-confirmar');
const comboTipoResena = document.getElementById('tipo-reseña');
const comboVisualizacion = document.getElementById('tipo-visualizacion');


const pantalla = new PantallaAdmReporteRanking(fechaDesde,fechaHasta, comboTipoResena, comboVisualizacion, tabla);


btnConfirmar.addEventListener('click', async () => {
    await pantalla.tomarConfirmacionReporte();
});
