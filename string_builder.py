class StringBuilder(object):
    def symbol_replace(self, old_string, symbol, replacement_text):
        newstring = old_string.replace(symbol, replacement_text)
        return newstring

    def complex_replacement(self, old_string, symbol_list, replacement_text_list):
        new_string = old_string
        for index in range(len(symbol_list)):
            new_string = self.symbol_replace(new_string, symbol_list[index], replacement_text_list[index])
        return new_string
