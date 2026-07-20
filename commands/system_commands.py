from subprocess import run

def lock(txt):
    txt = txt.lower()
    if "y" in txt:
        run("rundll32 user32.dll LockWorkStation")
        return True, "sure! locking."
    return False, ""

def shutdown_confirmation(txt):
    txt = txt.lower()
    if "shutdown" in txt:
        return True, "are you sure you want to shut down your computer?"
    return False, ""
    
def shutdown(txt):
    txt = txt.lower()

    if "yes" in txt:
        run("shutdown /s /t 0")
        return "shutting down"
    return None

def restart_confirmation(txt):
    txt = txt.lower()
    if "restart" in txt:
        return True, "are you sure you want to restart your computer?"
    return False, ""

def restart(txt):
    txt = txt.lower()

    if "yes" in txt:
        run("shutdown /r /t 0")
        return "restarting"
    return None

def log_out_confirmation(txt):
    txt = txt.lower()
    if "log out" in txt:
        return "are you sure you want to log out?"
    return None

def log_out(txt):
    txt = txt.lower()

    if "yes" in txt:
        run("shutdown /l")
        return "logging out"
    return None


def sleep(txt):
    txt = txt.lower()

    if "sleep" in txt:
        run("shutdown /l")
        return True, "sleeping"
    return False, ""


def hibernate(txt):
    txt = txt.lower()

    if "hibernate" in txt:
        run("shutdown /l")
        return True, "hibernating"
    return False, ""
