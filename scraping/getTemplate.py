from string import Template

def getTemplate(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        template_file_content = f.read()
    return Template(template_file_content) #Object Template