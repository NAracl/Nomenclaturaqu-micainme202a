import pandas as pd
#Ignora la carga, nomas la puse porque me daba hueva y el chatgpt me lo puso asi
cationes = {
    "Aluminio": {"Carga": 3, "Fórmula": "Al+3"},
    "Amonio": {"Carga": 1, "Fórmula": "NH4+"},
    "Bario": {"Carga": 2, "Fórmula": "Ba+2"},
    "Cadmio": {"Carga": 2, "Fórmula": "Cd+2"},
    "Calcio": {"Carga": 2, "Fórmula": "Ca+2"},
    "Cesio": {"Carga": 1, "Fórmula": "Cs+"},
    "Zinc": {"Carga": 2, "Fórmula": "Zn+2"},
    "Cobalto (II)": {"Carga": 2, "Fórmula": "Co+2"},
    "Cobre (I)": {"Carga": 1, "Fórmula": "Cu+"},
    "Cobre (II)": {"Carga": 2, "Fórmula": "Cu+2"},
    "Cromo (III)": {"Carga": 3, "Fórmula": "Cr+3"},
    "Estaño (II)": {"Carga": 2, "Fórmula": "Sn+2"},
    "Estroncio": {"Carga": 2, "Fórmula": "Sr+2"},
    "Hidrógeno": {"Carga": 1, "Fórmula": "H+"},
    "Hierro (II)": {"Carga": 2, "Fórmula": "Fe+2"},
    "Hierro (III)": {"Carga": 3, "Fórmula": "Fe+3"},
    "Litio": {"Carga": 1, "Fórmula": "Li+"},
    "Magnesio": {"Carga": 2, "Fórmula": "Mg+2"},
    "Manganeso (II)": {"Carga": 2, "Fórmula": "Mn+2"},
    "Mercurio (I)": {"Carga": 1, "Fórmula": "Hg+"},
    "Mercurio (II)": {"Carga": 2, "Fórmula": "Hg+2"},
    "Plata": {"Carga": 1, "Fórmula": "Ag+"},
    "Plomo (II)": {"Carga": 2, "Fórmula": "Pb+2"},
    "Potasio": {"Carga": 1, "Fórmula": "K+"},
    "Sodio": {"Carga": 1, "Fórmula": "Na+"},
}

aniones = {
    "Bromuro": {"Carga": -1, "Fórmula": "Br-"},
    "Carbonato": {"Carga": -2, "Fórmula": "CO3-2"},
    "Carbonato ácido o bicarbonato": {"Carga": -1, "Fórmula": "HCO3-"},
    "Cianuro": {"Carga": -1, "Fórmula": "CN-"},
    "Clorato": {"Carga": -1, "Fórmula": "ClO3-"},
    "Cloruro": {"Carga": -1, "Fórmula": "Cl-"},
    "Cromato": {"Carga": -2, "Fórmula": "CrO4+2"},
    "Dicromato": {"Carga": -2, "Fórmula": "Cr2O7-2"},
    "Fosfato": {"Carga": -3, "Fórmula": "PO4-3"},
    "Fosfato ácido": {"Carga": -2, "Fórmula": "HPO4-2"},
    "Fosfato diácido": {"Carga": -1, "Fórmula": "H2PO4-"},
    "Fluoruro": {"Carga": -1, "Fórmula": "F-"},
    "Hidróxido": {"Carga": -1, "Fórmula": "OH-"},
    "Hidruro": {"Carga": -1, "Fórmula": "H-"},
    "Nitrato": {"Carga": -1, "Fórmula": "NO3-"},
    "Nitrito": {"Carga": -1, "Fórmula": "NO2-"},
    "Nitruro": {"Carga": -3, "Fórmula": "N-3"},
    "Óxido": {"Carga": -2, "Fórmula": "O-2"},
    "Permanganato": {"Carga": -1, "Fórmula": "MnO4-"},
    "Peróxido": {"Carga": -2, "Fórmula": "O2-2"},
    "Sulfato": {"Carga": -2, "Fórmula": "SO4-2"},
    "Sulfato ácido": {"Carga": -1, "Fórmula": "HSO4-"},
    "Sulfito": {"Carga": -2, "Fórmula": "SO3-2"},
    "Sulfuro": {"Carga": -2, "Fórmula": "S-2"},
    "Tiocianato": {"Carga": -1, "Fórmula": "SCN-"},
    "Yoduro": {"Carga": -1, "Fórmula": "I-"},
}
#Almacena todos los datos para después exportalos
todo_alv = []
def obtener_formula(cation, anion):
    formula = cation["Fórmula"] + anion["Fórmula"]
    return formula

def obtener_nomenclatura(cation, anion):
    nomenclatura = f"{anion} de {cation}"
    return nomenclatura
#Repetir toda la madre
for cation in cationes:
    for anion in aniones:
        formula_terminal = obtener_formula(cationes[cation], aniones[anion])
        nombre = obtener_nomenclatura(cation, anion)
        data = {
            "Fórmula" : formula_terminal,
            "Nombre" : nombre
        }
        todo_alv.append(data)
        print(f"La molécula del catión {cation} con el anión {anion} es: {nombre} y la fórmula es {formula_terminal}")
#Ahora si lo de excel
writer = pd.ExcelWriter("1.11.xlsx", engine="openpyxl")
df = pd.DataFrame(todo_alv)
df.to_excel(writer, sheet_name="Sheet1",index=False)
writer.close()


