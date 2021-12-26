class Combiner:
    def __init__(self, que):
        self.que = que
        self.text = self.get_text()

    def get_text(self):
        text = ""
        
        current = 1

        while current < 4:
            aux = self.que
            while not aux.empty():
                result = aux.get()
                if result[0] == current:
                    text += result[1]
                    current += 1
        
        return text

    def write_to_file(self, file_name):
        with open(file_name, 'a') as f:
            f.write(self.text)
            f.close()
    
    def print(self):
        print(self.text)
