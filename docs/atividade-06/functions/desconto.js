function aplicarDesconto(valorTotal, percentual) {
    if (percentual < 0 || percentual > 100) {
        throw new Error("Percentual de desconto inválido");
    }

    const valorDesconto = (valorTotal * percentual) / 100;
    const valorFinal = valorTotal - valorDesconto;

    return valorFinal < 0 ? 0 : valorFinal;
}

module.exports = { aplicarDesconto };