import java.util.Scanner;

public class Menu {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int interaccion;

        System.out.println("Opciones: \n 1 = Personas \n 2 = Vehiculos \n 3 = Universidades \n 4 = Notas \n 5 = Salir");
        System.out.print("Digite una de las opciones: ");
        interaccion = scanner.nextInt();

        switch (interaccion) {
            case 1:
                System.out.println("Usted ha seleccionado la opción Personas");
                break;
            case 2:
                System.out.println("Usted ha seleccionado la opción Vehiculos");
                break;
            case 3:
                System.out.println("Usted ha seleccionado la opción Universidades");
                break;
            case 4:
                System.out.println("Usted ha seleccionado la opción Notas");
                break;
            case 5:
                System.out.println("Usted ha seleccionado la opción Salir");
                break;
            default:
                System.out.println("Gracias por haber utilizado el menú");
                break;
        }
        scanner.close();
    }
}