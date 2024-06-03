from bs4 import BeautifulSoup

class document:

    def __init__(self, document:str):
        with open(document, 'r') as file:
            file_content = file.read()
        self.htmlFile = BeautifulSoup(file_content, 'html.parser')
        self.fileName = document
    def getElementById(self, id:str='NaN'):
        doc = self.htmlFile
        elements = doc.find_all(id=id)
        return elements

    def getElementByClass(self, class_:str='NaN'):
        doc = self.htmlFile
        elements = doc.find_all(class_=class_)
        return elements
class element:

    def __init__(self):
        pass
    @staticmethod
    def src(element, value:str):
        for elements in range(len(element)):
            element[elements]["src"] = value
        return element

    @staticmethod
    def class_(element, value: str):
        for elements in range(len(element)):
            element[elements]["class"] = value
        return element

    @staticmethod
    def name(element, value: str):
        for elements in range(len(element)):
            element[elements].name = value
        return element
    @staticmethod
    def attrs(element, **kwargs):
        for key, value in kwargs.items():
            for elements in range(len(element)):
                element[elements][key] = value
        return element