import { PantallaAdmReporteRanking } from './PantallaAdmReporteRanking.js';

const tabla = document.getElementById('lista-ranking');
const fechaDesde = document.getElementById('fecha-desde');
const fechaHasta = document.getElementById('fecha-hasta');
const btnConfirmar = document.getElementById('btn-confirmar');
const comboTipoResena = document.getElementById('tipo-reseña').value;
const comboVisualizacion = document.getElementById('tipo-visualizacion').value;


const pantalla = new PantallaAdmReporteRanking(fechaDesde,fechaHasta, btnConfirmar, comboTipoResena, comboVisualizacion, tabla);

btnConfirmar.addEventListener('click', async () => {
    pantalla.cargarDatos();
    console.log('cargando datos');
    console.log(fechaDesde.value, fechaHasta.value);
});
