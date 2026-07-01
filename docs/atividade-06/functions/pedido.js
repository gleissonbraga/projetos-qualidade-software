function calcularTotalPedido(itens, valorMinimo) {
    const total = itens.reduce((soma, item) => soma + item.preco, 0);

    if (total < valorMinimo) {
        throw new Error("Valor mínimo do pedido não atingido");
    }

    return total;
}

module.exports = { calcularTotalPedido };