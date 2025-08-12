/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.myfirstclass;

/**
 *
 * @author Camila Uribe
 */
public class Ejercicio2 {
    public static void main(String[] args) {
	int[] numeros = {42, 7, 19, 3, 25};
        
	for (int i = 0; i < numeros.length - 1; i++) {
            int numMenor = i;
            for (int j = i + 1; j < numeros.length; j++) {
                if (numeros[j] < numeros[numMenor]) {
                    numMenor = j;
                }
            }
            
            if (numMenor != i) {
                int temp = numeros[i];
                numeros[i] = numeros[numMenor];
                numeros[numMenor] = temp;
            }
	}
		
	System.out.print("Orden de menor a mayor: ");
        for (int num : numeros) {
            System.out.print(num + " ");
        }
        
        
        
        for (int i = 0; i < numeros.length - 1; i++) {
            int numMayor = i;
            for (int j = i + 1; j < numeros.length; j++) {
                if (numeros[j] > numeros[numMayor]) { 
                    numMayor = j;
                }
            }
            if (numMayor != i) {
                int temp = numeros[i];
                numeros[i] = numeros[numMayor];
                numeros[numMayor] = temp;
            }
        }

        System.out.print("Orden de mayor a menor: ");
        for (int num : numeros) {
            System.out.print(num + " ");
        }
    }
}
