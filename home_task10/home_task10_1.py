def oops():
    raise IndexError("Oops! An IndexError occurred.")

def catch_error():
    try:
        oops()
    except IndexError as e:
        print(f"Caught an IndexError: {e}")
    except KeyError as e:
        print(f"Caught a KeyError: {e}")

catch_error()
