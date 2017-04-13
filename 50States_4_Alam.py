class FiftyStates():

    def __init__(self, states, colors, neighbors):
        self.states = states
        self.colors = colors
        self.neighbors = neighbors
        self.curr_colors = None

    def assignval(self, var, val, colormap):
        colormap[var] = val

    def unassignval(self, var, colormap):
        if var in colormap:
            del colormap[var]

    def numberofconflicts(self, var, val, colormap):
        def conflicts(var):
            return (var in colormap and not val!=colormap[var])
        count = 0;
        for v in self.neighbors[var]:
            count+=conflicts(v)
        return count

    def removals(self, var, value):
        if self.curr_colors == None:
            self.curr_colors = {v: list(self.colors[v]) for v in self.states}
        removals = [(var, a) for a in self.curr_colors[var] if a != value]
        self.curr_colors[var] = [value]
        return removals

    def remove(self, var, value, removals):
        self.curr_colors[var].remove(value)
        if removals is not None:
            removals.append((var, value))

    def actions(self, state):
        if len(state) == len(self.states):
            return []
        else:
            colormap = dict(state)
            for v in self.states:
                if(v not in colormap):
                    var = v
            return [(var, val) for val in self.colors[var] if self.numberofconflicts(var, val, colormap) == 0]

    def getChoices(self, var):
        return self.colors[var]

    def restore(self, removals):
        for B, b in removals:
            self.curr_colors[B].append(b)

    def goal_test(self, state):
        colormap = dict(state)
        return (len(colormap) == len(self.states)
                and all(self.numberofconflicts(states, colormap[states], colormap) == 0
                        for states in self.states))    

def get_unassigned_variable(colormap, fiftystates): #gets the next state that doesn't have a color
    for var in fiftystates.states:
        if var not in colormap:
            return var

def least_constrained_variable(var, colormap, fiftystates): #picks state with least number of constraints
    return sorted(fiftystates.getChoices(var), key=lambda val: fiftystates.numberofconflicts(var, val, colormap))

def forward_checking(fiftystates, var, value, colormap, removals): #forward checking
    for i in fiftystates.neighbors[var]:
        if i not in colormap:
            for j in fiftystates.curr_colors[i][:]:
                if not value!=j:
                    fiftystates.remove(i, j, removals)
            if not fiftystates.curr_colors[i]:
                return False
    return True

def recurbtsearch(fiftystates, colormap):
    if len(colormap) == len(fiftystates.states):
        return colormap
    var = get_unassigned_variable(colormap, fiftystates)
    for value in least_constrained_variable(var, colormap, fiftystates):
        if fiftystates.numberofconflicts(var, value, colormap) == 0:
            fiftystates.assignval(var, value, colormap)
            removals = fiftystates.removals(var, value)
            if forward_checking(fiftystates, var, value, colormap, removals)==True: #if result is reached
                result = recurbtsearch(fiftystates, colormap)
                if result != None:
                    return result
            fiftystates.restore(removals)
    fiftystates.unassignval(var, colormap)
    return None

class Dictionary:

    def __init__(self, value): 
        self.value = value

    def __getitem__(self, key): 
        return self.value

neighboringstates = {"WA": ["ID", "OR"], "DE": ["MD", "NJ", "PA"], "DC": ["MD", "VA"], "WI": ["IA", "IL", "MI", "MN"], "WV": ["KY", "MD", "OH", "PA", "VA"], "FL": ["AL", "GA"], "WY": ["CO", "ID", "MT", "NE", "SD", "UT"], "NH": ["MA", "ME", "VT"], "NJ": ["DE", "NY", "PA"], "NM": ["AZ", "CO", "OK", "TX", "UT"], "TX": ["AR", "LA", "NM", "OK"], "LA": ["AR", "MS", "TX"], "NC": ["GA", "SC", "TN", "VA"], "ND": ["MN", "MT", "SD"], "NE": ["CO", "IA", "KS", "MO", "SD", "WY"], "TN": ["AL", "AR", "GA", "KY", "MO", "MS", "NC", "VA"], "NY": ["CT", "MA", "NJ", "PA", "VT"], "PA": ["DE", "MD", "NJ", "NY", "OH", "WV"], "RI": ["CT", "MA"], "NV": ["AZ", "CA", "ID", "OR", "UT"], "VA": ["DC", "KY", "MD", "NC", "TN", "WV"], "CO": ["AZ", "KS", "NE", "NM", "OK", "UT", "WY"], "CA": ["AZ", "NV", "OR"], "AL": ["FL", "GA", "MS", "TN"], "AR": ["LA", "MO", "MS", "OK", "TN", "TX"], "VT": ["MA", "NH", "NY"], "IL": ["IA", "IN", "KY", "MO", "WI"], "GA": ["AL", "FL", "NC", "SC", "TN"], "IN": ["IL", "KY", "MI", "OH"], "IA": ["MN", "MO", "NE", "SD", "WI", "IL"], "MA": ["CT", "NH", "NY", "RI", "VT"], "AZ": ["CA", "CO", "NM", "NV", "UT"], "ID": ["MT", "NV", "OR", "UT", "WA", "WY"], "CT": ["MA", "NY", "RI"], "ME": ["NH"], "MD": ["DC", "DE", "PA", "VA", "WV"], "OK": ["AR", "CO", "KS", "MO", "NM", "TX"], "OH": ["IN", "KY", "MI", "PA", "WV"], "UT": ["AZ", "CO", "ID", "NM", "NV", "WY"], "MO": ["AR", "IA", "IL", "KS", "KY", "NE", "OK", "TN"], "MN": ["IA", "ND", "SD", "WI"], "MI": ["IN", "OH", "WI"], "KS": ["CO", "MO", "NE", "OK"], "MT": ["ID", "ND", "SD", "WY"], "MS": ["AL", "AR", "LA", "TN"], "SC": ["GA", "NC"], "KY": ["IL", "IN", "MO", "OH", "TN", "VA", "WV"], "OR": ["CA", "ID", "NV", "WA"], "SD": ["IA", "MN", "MT", "ND", "NE", "WY"], "HI": [], "AK": []}

solution = FiftyStates(list(neighboringstates.keys()), Dictionary(['Red', 'Green', 'Blue', 'Yellow']), neighboringstates)

statesmap = {}
print(recurbtsearch(solution, statesmap))