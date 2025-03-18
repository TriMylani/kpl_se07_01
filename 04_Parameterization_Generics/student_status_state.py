from enum import Enum

class StudentStatusState(Enum):
    TERDAFTAR = "Terdaftar"
    CUTI = "Cuti"
    AKTIF = "Aktif"
    LULUS = "Lulus"

# Trigger input
class TriggerInputState(Enum):
    CATAK_KSM = "Cetak KSM"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"
    LULUS = "Lulus"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"

#Transition
state_transitions = {
    StudentStatusState.TERDAFTAR: {
        TriggerInputState.CATAK_KSM: StudentStatusState.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    },
    StudentStatusState.CUTI: {
        TriggerInputState.MENYELESAIKAN_CUTI: StudentStatusState.TERDAFTAR
    },
    StudentStatusState.AKTIF: {
        TriggerInputState.LULUS: StudentStatusState.LULUS,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    }
}

def change_state(current_state, trigger_input):
    cond_1 = current_state in state_transitions #Return True atau False
    cond_2 = trigger_input in state_transitions[current_state] # Return True atau False
    if cond_1 and cond_2:
        #TERDAFTAR, AKTIF, LULUS, CUTI
        return state_transitions[current_state][trigger_input]
    return "Transisi Tidak Valid"

current_state = StudentStatusState.TERDAFTAR
trigger_input = TriggerInputState.CATAK_KSM

next_state = change_state(current_state, trigger_input)
print(next_state)