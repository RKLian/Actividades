import java.util.Date;

public class Animal {
    private String nombre;
    private int numeroDePatas;
    private String propietario;
    private Date fechaDeVacunacion;

    public Animal(String nombre, int numeroDePatas, String propietario, Date fechaDeVacunacion) {
        this.nombre = nombre;
        this.numeroDePatas = numeroDePatas;
        this.propietario = propietario;
        this.fechaDeVacunacion = fechaDeVacunacion;
    }

    public String getNombre() {
        return nombre;
    }

    public int getNumeroDePatas() {
        return numeroDePatas;
    }

    public String getPropietario() {
        return propietario;
    }

    public Date getFechaDeVacunacion() {
        return fechaDeVacunacion;
    }

    public void mostrarInformacion() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Número de Patas: " + numeroDePatas);
        System.out.println("Propietario: " + propietario);
        System.out.println("Fecha de Vacunación: " + fechaDeVacunacion);
    }

    public static void main(String[] args) {
        Animal miMascota = new Animal("Rocky", 4, "Yulian", new Date());
        miMascota.mostrarInformacion();
    }
}
