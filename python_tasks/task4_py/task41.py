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
    """Decorator for wrap text in <p> tag"""
    
    def wrapped():
        return "\t<p>" + func() + "</p>"
    return wrapped

def own_tag(tag):
    def tag_decorator(func):
        """Decorator for wrap text in own tag"""
     
        def wrapped():
            return "<" + tag + ">" + func() + "<" + tag+ "/>"
        return wrapped
    return tag_decorator

@htmlbase
@make_paragraph
@makebold
@own_tag('o')  
def say_hello():
    """Method for saying Hi to my amigo"""
    
    return "Hello, amigo!"

