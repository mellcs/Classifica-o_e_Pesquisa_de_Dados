class FolhaPagamento {
    Funcionario[] funcionarios;

    // Construtor
    FolhaPagamento(Funcionario[] funcionarios) {
        this.funcionarios = funcionarios;
    }

    // Ordenar funcionários por salário decrescente
    void ordenar() {
        for (int i = 0; i < funcionarios.length - 1; i++) {
            for (int j = i + 1; j < funcionarios.length; j++) {
                if (funcionarios[i].calcularSalario() < funcionarios[j].calcularSalario()) {
                    Funcionario temp = funcionarios[i];
                    funcionarios[i] = funcionarios[j];
                    funcionarios[j] = temp;
                }
            }
        }
    }

    // Exibir informações de todos os funcionários
    void exibir() {
        for (Funcionario funcionario : funcionarios) {
            funcionario.exibir();
            System.out.println("-------------------");
        }
    }

    // Método main
    public static void main(String[] args) {
        Funcionario[] funcionarios = {
            new Funcionario(1, 160, 20, 10),
            new Funcionario(2, 170, 18, 5),
            new Funcionario(3, 150, 22, 8)
        };

        FolhaPagamento folha = new FolhaPagamento(funcionarios);
        folha.exibir();
        folha.ordenar();
        System.out.println("Após ordenação por salário decrescente:");
        folha.exibir();
    }
}
