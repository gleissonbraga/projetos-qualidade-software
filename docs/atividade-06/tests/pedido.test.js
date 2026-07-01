const { calcularTotalPedido } = require('../functions/pedido');

describe('Cálculo do Total do Pedido (Integrante 1)', () => {
    test('Deve calcular corretamente o total quando o valor minimo é atingido', () => {
        const itens = [{ preco: 15.0 }, { preco: 14.0 }];
        const resultado = calcularTotalPedido(itens, 30.0);
        expect(resultado).toBe(35.0);
    });

    test('Deve lancar erro quando o total for menor que o valor minimo', () => {
        const itens = [{ preco: 10.0 }];
        expect(() => {
            calcularTotalPedido(itens, 20.0);
        }).toThrow("Valor mínimo do pedido não atingido");
    });
});