import numpy as np
import matplotlib.pyplot as plt


def plotFunction(values:dict):
    lists=sorted(values.items())
    x,y=zip(*lists)
    plt.plot(x,y)
    plt.ylabel('I Intenisty')
    plt.xlabel('Angle')
    plt.show()


valeur_Helium_Glass={
    90:10.0429,
    85.4:9.4050,
    80.3:8.11,
    75.3:6.3802,
    70.8:4.588,
    65.7:2.66,
    60:1.2749,
    56.6:1,
    54.3:1.1228,
    49.3:2.133,
    45.2:3.5306,
    40.6:5.3620,
    34.7:7.5750,
    30:8.9387,
    25:9.9217,
    20:10.4953,
    15:10.7886,
    10:10.9208,
    5:10.9734,
    0:10.9920
}

valeur_flint_air={
    90:10.0429,
    85.4:9.2257,
    80.3:7.84,
    75.3:6.0524,
    70.8:4.2482,
    65.7:2.3863,
    60:1.1374,
    56.6:1.0182,
    54.3:1.2257,
    49.3:2.3896,
    45.2:3.8572,
    40.6:5.7011,
    34.7:7.8517,
    30:9.1385,
    25:10.0444,
    20:10.5610,
    15:10.8195,
    10:10.9336,
    5:10.9782,
    0:10.9936,
}

valeur_topaz_CO2={
    90:9.9586,
    85.4:9.0924,
    80.3:7.6568,
    75.3:5.8200,
    70.8:4.0140,
    65.7:2.2060,
    60:1.0803,
    56.6:1.0496,
    54.3:1.3150,
    49.3:2.5794,
    45.2:4.0894,
    40.6:5.9348,
    34.7:8.0368,
    30:9.2694,
    25:10.1232,
    20:10.6024,
    15:10.8387,
    10:10.9414,
    5:10.9810,
    0:10.9945,
}


plotFunction(valeur_topaz_CO2)
plotFunction(valeur_flint_air)
plotFunction(valeur_Helium_Glass)
