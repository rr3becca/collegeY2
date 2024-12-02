class WizCoinPurse:

    def __init__(self, knuts, sickles, galleons):
        self.knuts = knuts
        self.sickles = sickles
        self.galleons = galleons

    #b
    def currency_knuts(self):
        currency = 0
        currency += self.knuts + (self.sickles * 29) + (self.galleons * 493)
        print("\nTOTAL:\nTotal in knuts is: ", currency)

    #c
    def weight(self):
        knuts_weight = 5.0
        sickle_weight = 11.34
        galleons_weight = 31.103
        weight_total = (self.knuts * knuts_weight) + (self.sickles * sickle_weight) + (self.galleons * galleons_weight)
        print("\nWEIGHT:\nTotal weight in grams is : {:0.3f}".format(weight_total))



    #a
    def __str__(self):
        return "CURRENCY:\n{} knuts\n{} sickles (worth 29 knuts)\n{} galleons (worth 17 sickles or 493 knuts)".format(self.knuts, self.sickles, self.galleons)


p1 = WizCoinPurse(22, 15, 10)
print(p1)
p1.currency_knuts()
p1.weight()



