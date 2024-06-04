import { PantallaAdmReporteRanking } from './PantallaAdmReporteRanking.js';


const btnOpcionRanking = document.getElementById('btn-opt-rank');

const pantalla = new PantallaAdmReporteRanking();

btnOpcionRanking.addEventListener('click', async () => {
    pantalla.opcionGenerarRankingDeVinos();
});