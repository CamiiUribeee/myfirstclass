/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.myfirstclass;

import java.util.Scanner;

/**
 *
 * @author Camila Uribe
 */
public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese un número: ");
        int numero = sc.nextInt();

        if (numero <= 1) {
            System.out.println("No es primo");
            return;
        }
        if (numero == 2) {
            System.out.println("Es primo");
            return;
        }

        int limite = (int) Math.sqrt(numero);
        boolean esPrimo = true;

        for (int i = 2; i <= limite; i++) {
            if (numero % i == 0) {
                esPrimo = false;
                break;
            }
        }

        if (esPrimo) {
            System.out.println("Es primo");
        } else {
            System.out.println("No es primo");
        }
    }
}
