const TAXA_FIXA = 5.00;
const LIMITE_DISTANCIA_FIXA = 3.0;
const VALOR_POR_KM_ADICIONAL = 2.00;

function calcularTaxaEntrega(distanciaKm) {
    if (distanciaKm < 0) {
        throw new Error("Distância não pode ser negativa");
    }

    if (distanciaKm <= LIMITE_DISTANCIA_FIXA) {
        return TAXA_FIXA;
    }

    const kmAdicionais = distanciaKm - LIMITE_DISTANCIA_FIXA;
    return TAXA_FIXA + (kmAdicionais * VALOR_POR_KM_ADICIONAL);
}

module.exports = { calcularTaxaEntrega };