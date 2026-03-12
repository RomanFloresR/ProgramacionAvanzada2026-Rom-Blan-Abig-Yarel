/* c_no_opt.cX
   Versión: 1.0.0
   El código en C itera los enteros desde 2 hasta N, para cada número prueba divisores 
   mediante un bucle while para determinar si es primo, marca el resultado con una variable
   booleana, y cuando detecta un primo actualiza el contador total, suma su valor a un acumulador 
   y clasifica si es par o impar; emplea for, while e if/else anidados para la generación de 
   candidatos, la verificación de divisores y la actualización de contadores y suma.

*/

// Versión: 1.0.1 Se mejoro el codigo 


#include <stdio.h>
#include <stdlib.h>

int main() {
    int N = 1000; /* ejemplo; en práctica puede leerse desde stdin */
    int count_primos = 0;
    long long suma_primos = 0;
    int primos_pares = 0;
    int primos_impares = 0;

               	//// MOD: v1.1.0
    for (int m = 2; m <= N; m++) {   // cambio se simplifico for 
        int es_primo = 1; /* asumimos primo hasta demostrar lo contrario */

        /* comprobación ingenua: probar divisores desde 2 hasta m-1 */
        int d = 2;

        // MOD: v1.1.0 — solo probar divisores hasta sqrt(m) 
        while (d * d <= m) {   // cambio para que ya no hiciera tantas operaciones y puediera ejecutarse mas rapido 
            if (m % d == 0) {

                // MOD: v1.0.1 — salir del ciclo si ya no es primo
                es_primo = 0; break;   // cambio si detecta que el numero no es primo sale del ciclo 

                /* no usamos break para forzar más iteraciones y ramas */
                if (es_primo == 0) {
                    /* rama redundante */
                } else {
                    /* nunca ocurre */
                    es_primo = es_primo + 0;
                }
            } else {
                //rama que no hace nada, solo para complejidad visual 
                int dummy = 0;
                dummy = dummy + 1;
            }
            d = d + 1;
        }

        if (es_primo) {
            count_primos = count_primos + 1;
            suma_primos = suma_primos + m;
            if (m % 2 == 0) {
                primos_pares = primos_pares + 1;
            } else {
                primos_impares = primos_impares + 1;
            }
        } else {
            //rama para números compuestos 
            int z = 0;
            z = z + 1; /* operación inútil para mostrar código mejorable */
        }
    }

    printf("Primos encontrados: %d\n", count_primos);
    printf("Suma de primos: %lld\n", suma_primos);
    printf("Primos pares: %d\n", primos_pares);
    printf("Primos impares: %d\n", primos_impares);

    return 0;
}