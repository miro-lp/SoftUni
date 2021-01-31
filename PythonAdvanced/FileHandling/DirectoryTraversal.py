import os

d_info = [i for i in os.listdir() if os.path.isfile(i)]

report = {os.path.splitext(j)[-1]: [k for k in d_info if j.split(".")[-1] in k] for j in d_info}

report = dict(sorted(report.items(), key=lambda x: (x[0], x[1])))

path_desktop = os.path.join(os.path.join(os.environ["USERPROFILE"], "Desktop"), "report.txt")

with open(path_desktop, "w") as f:
    for k in report:
        print(k, file=f)
        print("\n".join([f"- - - {name}" for name in report[k]]), file=f)
