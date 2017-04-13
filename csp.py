colors = ['Red', 'Blue', 'Green', 'Yellow']

WA = 'western australia'
NT = 'northwest territories'
SA = 'southern australia'
Q = 'queensland'
NSW = 'new south wales'
V = 'victoria'
T = 'tasmania'

states = {WA, NT, SA, Q, NSW, V, T}
neighbors = { T:   {             },
              WA:  {NT, SA         },
              NT:  {WA, Q, SA       },
              SA:  {WA, NT, Q, NSW, V},
              Q:   {NT, SA, NSW   },
              NSW: {Q, SA, V         },
              V:   {SA, NSW,      } }


def btsearch(csp): #returns solution/failure
    return recurbtsearch({ }, csp)
def recurbtsearch(mapcolors, csp): #returns soln/failure
    if goalTest(mapcolors):
        return mapcolors
    var = select_unassigned_var(Variables[csp], mapcolors, csp)
    for each value in Order-Domain-Values(var, mapcolors, csp) do
        if value is consistent with assignment given Constraints[csp] then
            add {var = value} to mapcolors
            result ← Recursive-Backtracking(mapcolors, csp)
            if result != failure then
                return result
            remove {var = value} from mapcolors
    return failure
def goalTest(map):
    for i in range(states):
        state = states[i]
        if map[state] is None:
            return False
    return True
def select_unassigned_var(map, ):


main()
