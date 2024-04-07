class AppFactory:
    def create(appName: str):
        appdict = {
            "cat": cat.Cat(),
            "cd": cd.Cd(),
            "cut": cut.Cut(),
            "echo": echo.Echo(),
            "find": find.Find(),
            "grep": grep.Grep(),
            "head": head.Head(),
            "ls": ls.Ls(),
            "pwd": myPwd.Pwd(),
            "sort": sort.Sort(),
            "tail": tail.Tail(),
            "uniq": uniq.Uniq(),
        }

        if appName in appdict:
            return appdict[appName]
        elif appName.startswith("_") and appName[1:] in appdict:
            return UnsafeDecorator(appdict[appName[1:]])
        else:
            raise RuntimeError("Application " + appName + " not found.")