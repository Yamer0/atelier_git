def moyenne(notes):
return sum(notes) / len(notes)
notes = [12, 15, 9, 18]
def note_max(notes):
return max(notes)
def mediane(notes):
tri = sorted(notes)
n = len(tri)
return tri[n // 2]
def note_min(notes):
return min(notes)
notes = [12, 15, 9, 18]
print("Médiane :", mediane(notes))
print("Moyenne :", moyenne(notes))
print("Note maximale :", note_max(notes))
print("Note minimale :", note_min(notes))