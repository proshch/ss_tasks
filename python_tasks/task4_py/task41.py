"""This module is for creating script with html decorator"""


def htmlbase(func):
    """Decorator for base html tags"""
    
    def wrapped():
        return "<!DOCTYPE html>\n<html>\n<head>\n\t<title>Decorate me!</title>\n</head>\n<body>\n" + func() + "\n</body>\n</html>"
    return wrapped

def makebold(func):
    """Decorator for making text bold"""

    def wrapped():
        return "<b>" + func() + "</b>"
    return wrapped

def make_paragraph(func):
    """Decorator for wrap text int <p> tag"""
    
    def wrapped():
        return "\t<p>" + func() + "</p>"
    return wrapped

@htmlbase
@make_paragraph
@makebold
def hello():
    """Method for saying Hi to my amigo"""
    
    return "Hello, amigo!"

print hello()
