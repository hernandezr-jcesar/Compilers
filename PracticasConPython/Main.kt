
fun main() {

    val automata = Automata()

    println("Ingresa cadena a procesar: ")
    val string = readLine()!!
    val it = automata.alphabet.find { it == string[0].toString() }

    println(it)
    var error = false
    val imp = " "
    if (it.equals(automata.alphabet.last())) {
        error = true
    }
    automata.transitions(string, automata.firstState, imp, automata.errorsManagement, error)
    if (!automata.validated) {
        println("La cadena no es valida")
    }

}

