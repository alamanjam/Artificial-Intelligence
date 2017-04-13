def btsearch(csp): #returns solution/failure
return recurbtsearch({ }, csp)

def recurbtsearch(assignment, csp): #returns soln/failure
	if assignment is complete then return assignment
	var = select_unassigned_var(Variables[csp], assignment, csp)
	for each value in Order-Domain-Values(var, assignment, csp) do
	if value is consistent with assignment given Constraints[csp] then
	add {var = value} to assignment
	result ← Recursive-Backtracking(assignment, csp)
	if result 6= failure then return result
	remove {var = value} from assignment
	return failure