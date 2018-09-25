cijferICOR = 7.5
cijferPROG = 6.5
cijferCSN = 7

gemiddelde = (cijferCSN + cijferICOR + cijferPROG)/3

beloning = (cijferCSN*30)+(cijferICOR*30)+(cijferPROG*30)

string1 = str(gemiddelde)
string2 = str(beloning)

overzicht = ('Mijn cijfers (gemiddeld een {}), leveren een beloning van €{} op!'.format(gemiddelde, beloning))

print(overzicht)