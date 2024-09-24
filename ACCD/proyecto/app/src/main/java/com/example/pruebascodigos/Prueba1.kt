package com.example.pruebascodigos



fun main() {
    var paises: MutableMap<String, String> = mutableMapOf()

    paises.put("España", "Europa")
    paises.put("Francia", "Europa")
    paises.put("Venezuela", "Latinoamérica")
    paises.put("USA", "América")

    println(paises)  // Resultado: {España=Europa}

    val pais: String = "España"

    when (pais) {
        "España" -> println("Europa")
        "Francia" -> println("Europa")
        "USA" -> println("América")
        "Colombia" -> println("Latinoamérica")
    }
}

