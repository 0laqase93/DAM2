/**
 * You can edit, run, and share this code.
 * play.kotlinlang.org
 */
fun main() {
    /**
     * Ejercicio 1
     */

    //a)
    val pi = 3.141592653589793
    val lightspeed = 299792458 //m/s

    //b)
    var nombre = "Vicente"
    var edad = 21

    /**
     * Ejercicio 2
     */

    //a)
    println("Me llamo Vicente y tengo 21 años")

    //b)
    println("Me llamo $nombre y tengo $edad años")

    /**
     * Ejercicio 4
     */

    //a)
    val num1 = 5
    val num2 = 13
    val suma = num1 + num2

    if (suma > 20) {
        println("Los números NO están en el rango :(")
    } else {
        println("$suma está en el rango")
    }

    /**
     * Ejercicio 5
     */

    //a)
    val pais = "Francia"

    when (pais) {
        "España", "Francia", "Portugal" -> println("Europa")
        "USA", "Canada" -> println("América")
        "Colombia", "Venezuela", "Chile" -> println("Latinoamérica")
        "Corea del Norte", "Corea del Sur" -> println("Asia")
    }
}