import java.util.Scanner;

public class CalculadoraSimples {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        float numero1 = scanner.nextFloat();

        System.out.print("Digite o segundo número: ");
        float numero2 = scanner.nextFloat();

        System.out.print("Digite o operador (+, -, *, /): ");
        char operador = scanner.next().charAt(0);

        float resultado = 0;
        boolean erroDivisao = false;

        switch (operador) {
            case '+':
                resultado = numero1 + numero2;
                break;
            case '-':
                resultado = numero1 - numero2;
                break;
            case '*':
                resultado = numero1 * numero2;
                break;
            case '/':
                if (numero2 != 0) {
                    resultado = numero1 / numero2;
                } else {
                    erroDivisao = true;
                }
                break;
            default:
                System.out.println("Operador inválido.");
                return;
        }

        if (erroDivisao) {
            System.out.println("Erro: divisão por zero.");
        } else {
            System.out.println("Resultado: " + resultado);
        }

        scanner.close();
    }
}
