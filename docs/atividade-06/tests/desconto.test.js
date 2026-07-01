const { aplicarDesconto } = require('../functions/desconto');

describe('Aplicação de Desconto Percentual (Integrante 2)', () => {
    test('Deve aplicar desconto percentual válido corretamente', () => {
        const resultado = aplicarDesconto(100.0, 15); // 15% de 100
        expect(resultado).toBe(85.0);
    });

    test('Deve lancar erro se o desconto for maior que 100%', () => {
        expect(() => {
            aplicarDesconto(50.0, 105);
        }).toThrow("Percentual de desconto inválido");
    });
});