class compute:
    def __init__(self, data = None):
        self.data = data
        self.gain = {
            "36": 17,
            "55": 27,
            "87": 40,
            "125": 60,
            "144": 70
        }
        self.bonus = {
            "0": 0,
            "1000": 7,
            "2000": 14,
            "3000": 21
        }
        self.compret = {
            "data": [],
            "bonus": None,
            "totalpv": 0,
            "totalgain": 0
        }

    def calc(self):
        ret = self.compret
        for n, d in enumerate(self.data):
            ret["data"].append(d)
            if str(d["pv"]) not in self.gain:
                return [False, "Invalid PV value: " +  str(d["pv"]), 401]
            gain = self.gain[str(d["pv"])] * int(d["nb_clients"])
            pv = int(d["pv"]) * int(d["nb_clients"])
            ret["data"][n]["totalpv"] = pv
            ret["data"][n]["totalgain"] = gain
            ret["totalpv"] += pv
            ret["totalgain"] += gain

        bonus = self.getbonus(ret["totalpv"])
        ret["bonus"] = {
            "ref": self.bonus,
            "your_bonus": bonus
        }
        ret["totalgain"] = ret["totalgain"] * (100 + bonus) / 100
        return [True, ret, None]

    def getbonus(self, pv):
        bonus = None
        for n, i in self.bonus.items():
            if pv < int(n):
                break
            else:
                bonus = i
        return bonus
