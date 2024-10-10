import { PantallaAdmReporteRanking } from './PantallaAdmReporteRanking.js';


const pantalla = new PantallaAdmReporteRanking();

pantalla.pedirFechasReseña();
pantalla.pedirTipoResena();
pantalla.pedirTipoVisualizacion();
const [btnConfirmar, btnFin] = pantalla.pedirConfirmacionReporte();


btnConfirmar.addEventListener('click', async () => {
    await pantalla.tomarConfirmacionReporte();
});

btnFin.addEventListener('click', () => {
    pantalla.finCU();
});
