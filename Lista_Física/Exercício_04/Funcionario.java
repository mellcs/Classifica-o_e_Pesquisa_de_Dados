class Funcionario {
    int codigo;
    float quantidadeHoras;
    float valorHora;
    float quantidadeHorasExtras;

    // Construtor
    Funcionario(int codigo, float quantidadeHoras, float valorHora, float quantidadeHorasExtras) {
        this.codigo = codigo;
        this.quantidadeHoras = quantidadeHoras;
        this.valorHora = valorHora;
        this.quantidadeHorasExtras = quantidadeHorasExtras;
    }

    // Calcular hora extra
    float calcularHoraExtra() {
        return quantidadeHorasExtras * valorHora * 1.5f;
    }

    // Calcular salário
    float calcularSalario() {
        return (quantidadeHoras * valorHora) + calcularHoraExtra();
    }

    // Exibir informações do funcionário
    void exibir() {
        System.out.println("Código: " + codigo);
        System.out.println("Salário: R$" + calcularSalario());
    }
}
