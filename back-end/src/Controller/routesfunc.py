from Model.basic import check
from Object.calc import compute


def compute_one(cn, nextc):
    err = check.contain(cn.pr, ["pv", "nb_clients"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    use = compute([cn.pr])
    err = use.calc()

    return cn.call_next(nextc, err)

def compute_multi(cn, nextc):
    err = check.contain(cn.pr, ["data"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    cn.pr = err[1]

    for i in cn.pr["data"]:
        err = check.contain(i, ["pv", "nb_clients"])
        if not err[0]:
            return cn.toret.add_error(err[1], err[2])

    use = compute(cn.pr["data"])
    err = use.calc()

    return cn.call_next(nextc, err)
