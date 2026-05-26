const { calcularTaxaEntrega } = require('../functions/entrega');

describe('Cálculo de Taxa de Entrega (Integrante 3)', () => {
    test('Deve cobrar taxa fixa para distancia ate 3km', () => {
        const resultado = calcularTaxaEntrega(2.5);
        expect(resultado).toBe(5.00);
    });

    test('Deve cobrar taxa adicional proporcional por km acima de 3km', () => {
        const resultado = calcularTaxaEntrega(5.0); // 3km fixo (5.0) + 2km adicionais (4.0)
        expect(resultado).toBe(9.00);
    });

    test('Deve lancar erro para distancia negativa', () => {
        expect(() => {
            calcularTaxaEntrega(-1.5);
        }).toThrow("Distância não pode ser negativa");
    });
});