def arrangeWords(self, text: str) -> str:
        arr = []
        for i,x in enumerate(text.split()):
            arr.append((len(x),i,x.lower()))
        r= [x[2] for x in sorted(arr)]
        r[0] = r[0][0].upper() + r[0][1:]
        return " ".join(r)