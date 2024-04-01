/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.vectoresjava;
    import java.util.ArrayList;
    import java.util.Collections;
/**
 *
 * @author Yulian
 */

// Ejercicio de Array en Java.
public class VectoresJava {

    public static void main(String[] args) {
        // Declarar una lista vacia de enteros
        ArrayList<Integer> listaVacia = new ArrayList<>();

        // Declarar una lista con mas de 5 elementos de enteros
        ArrayList<Integer> listaConElementos = new ArrayList<>();
        listaConElementos.add(10);
        listaConElementos.add(200);
        listaConElementos.add(75);
        listaConElementos.add(40);
        listaConElementos.add(100);

        // Encuentra la longitud de las dos listas
        System.out.println("Longitud de listaVacia: " + listaVacia.size());
        System.out.println("Longitud de listaConElementos: " + listaConElementos.size());

        // Obtener el primer elemento, el elemento central y el ultimo elemento de la lista
        System.out.println("Primer elemento de listaConElementos: " + listaConElementos.get(0));
        System.out.println("Elemento central de listaConElementos: " + listaConElementos.get(listaConElementos.size() / 2));
        System.out.println("Ultimo elemento de listaConElementos: " + listaConElementos.get(listaConElementos.size() - 1));

        // Crear una lista de Datos_personales con enteros
        ArrayList<Integer> datosPersonales = new ArrayList<>();
        datosPersonales.add(19); // Edad
        datosPersonales.add(180); // Altura en cm

        // Crear la lista it_companies con enteros
        ArrayList<Integer> itCompanies = new ArrayList<>();
        itCompanies.add(1); // Facebook
        itCompanies.add(2); // Google
        itCompanies.add(3); // Microsoft
        itCompanies.add(4); // Apple
        itCompanies.add(5); // IBM
        itCompanies.add(6); // Oracle
        itCompanies.add(7); // Amazon

        // Añadir una empresa a la lista it_companies
        itCompanies.add(1, 8); // Añadir Tesla en la posicion 1

        // Comprobar si una empresa existe en la lista it_companies
        if (itCompanies.contains(3)) {
            System.out.println("Microsoft esta en la lista.");
        } else {
            System.out.println("Microsoft no esta en la lista.");
        }

        // Ordenar la lista it_companies
        Collections.sort(itCompanies);

        // Invertir la lista en orden descendente
        Collections.reverse(itCompanies);

        // Eliminar la primera empresa informatica de la lista
        itCompanies.remove(0);

        // Eliminar todas las empresas de la lista it_companies
        itCompanies.clear();
    }
}