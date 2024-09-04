class ControleAlunos {

    public double calcularMediaIdade(Aluno[] alunos) {
        int somaIdade = 0;
        for (Aluno aluno : alunos) {
            somaIdade += aluno.idade;
        }
        return (double) somaIdade / alunos.length;
    }

    public void encontrarDoisMaisJovens(Aluno[] alunos) {
        int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;
        String aluno1 = "", aluno2 = "";

        for (Aluno aluno : alunos) {
            if (aluno.idade < min1) {
                min2 = min1;
                aluno2 = aluno1;
                min1 = aluno.idade;
                aluno1 = aluno.nome;
            } else if (aluno.idade < min2) {
                min2 = aluno.idade;
                aluno2 = aluno.nome;
            }
        }

        System.out.println("Os dois alunos mais jovens são: " + aluno1 + " e " + aluno2);
    }

    public double calcularPercentualMaisDe16Anos(Aluno[] alunos) {
        int contador = 0;
        for (Aluno aluno : alunos) {
            if (aluno.idade > 16) {
                contador++;
            }
        }
        return (double) contador / alunos.length * 100;
    }

    public int contarAlunosMenoresComAlturaSuperiorAMedia(Aluno[] alunos) {
        double somaAltura = 0;
        for (Aluno aluno : alunos) {
            somaAltura += aluno.altura;
        }
        double mediaAltura = somaAltura / alunos.length;

        int contador = 0;
        for (Aluno aluno : alunos) {
            if (aluno.idade < 16 && aluno.altura > mediaAltura) {
                contador++;
            }
        }
        return contador;
    }
}

public class Main {
    public static void main(String[] args) {
        Aluno[] alunos = {
            new Aluno(1, "Joao", 14, 1.75),
            new Aluno(2, "Maria", 18, 1.54),
            new Aluno(3, "Pedro", 15, 1.62),
            new Aluno(4, "Clara", 16, 1.60),
            new Aluno(5, "Jose", 17, 1.56),
            new Aluno(6, "Carla", 16, 1.62),
            new Aluno(7, "Fabio", 16, 1.65),
            new Aluno(8, "Mara", 17, 1.62),
            new Aluno(9, "Cesar", 14, 1.74),
            new Aluno(10, "Ana", 17, 1.68)
        };

        ControleAlunos controle = new ControleAlunos();

        System.out.println("Média de idade dos alunos: " + controle.calcularMediaIdade(alunos));

        controle.encontrarDoisMaisJovens(alunos);

        System.out.println("Percentual de alunos com mais de 16 anos: " + controle.calcularPercentualMaisDe16Anos(alunos) + "%");

        System.out.println("Alunos com menos de 16 anos e altura superior à média: " + controle.contarAlunosMenoresComAlturaSuperiorAMedia(alunos));
    }
}
