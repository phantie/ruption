class RustObject:
    store = [None]

    def get_by_ref(self):
        return store[0]

ro = RustObject()