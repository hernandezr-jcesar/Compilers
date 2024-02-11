import java.io.File

typealias vic = MutableList<Pair<String, String>>

class Automata {
    var states: MutableList<String> = mutableListOf()
    var finalStates: MutableList<String> = mutableListOf()
    var firstState: String = ""
    var alphabet: MutableList<String> = mutableListOf()
    var movements: MutableMap<String, vic> = mutableMapOf()
    var errorsManagement: vic = mutableListOf()
    var validated: Boolean = false

    init {
        val textFile = File("C:\\Users\\SAM\\Compiladores\\P2\\src\\main\\kotlin\\afTxt.txt")
        val dirtyText = textFile.readLines()
        states = cleanLine(dirtyText[0])
        finalStates = cleanLine(dirtyText[1])
        firstState = dirtyText[2]
        alphabet = cleanLine(dirtyText[3])
        movements = cleanMovements(dirtyText.subList(4, dirtyText.size))
    }

    private fun cleanLine(line: String): MutableList<String> {
        val listTemp: MutableList<String> = mutableListOf()
        line.split(",").forEach { listTemp.add(it) }
        return listTemp
    }

    private fun cleanMovements(
        movements: List<String>,
    ): MutableMap<String, vic> {
        var current: String
        var alpha: String
        var next: String

        val movementsTemp: MutableMap<String, vic> = mutableMapOf()
        for (i in movements.indices) {
            current = movements[i].split(",")[0]
            alpha = movements[i].split(",")[1]
            next = movements[i].split(",")[2]
            val pair = Pair(alpha, next)

            if (!movementsTemp.containsKey(current)) {
                movementsTemp[current] = mutableListOf(pair)
            } else {
                movementsTemp[current]?.add(pair)
            }
        }

        return movementsTemp
    }

    fun transitions(string: String, currentState: String, imp: String, errors: vic, me: Boolean) {

        var impTemp = imp
        if (!me) {
            impTemp += "q"
            impTemp += currentState
            impTemp += if (string.isEmpty()) {
                " "
            } else {
                "->"

            }

        }

        if (string.isEmpty()) {
            val ie = finalStates.find { it == (currentState) }

            if (ie.equals(finalStates.last())) {
                println("T:$impTemp")
                validated = true
                if (errorsManagement.isNotEmpty()) {
                    print("ME:")
                    errorsManagement.forEach {
                        print("q${it.first}(${it.second})->")
                    }
                    println()
                    errorsManagement.clear()
                }

            }

            return


        } else {

            val aux = string.substring(1)
            val c: String = string[0].toString()
            var exist = false

            movements[currentState]?.forEach {
                if (it.first == c) {
                    transitions(aux, it.second, impTemp, errors, false)
                    exist = true
                }
                // Aqui va el if para el epsilon
                else if (it.first == "E") {
                    transitions(string, it.second, impTemp, errors, false)
                    exist = true

                }
            }
            val ie2 = finalStates.find { it == string[0].toString() }
            if (!exist and (ie2 == alphabet.last())) {
                val pair = Pair(currentState, c)
                errors.add(pair)
                transitions(aux, currentState, impTemp, errors, true)
            }
        }
    }
}