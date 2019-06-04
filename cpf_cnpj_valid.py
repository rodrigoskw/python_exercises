import validate_docbr

cpf = validate_docbr.CPF()

# Gerar CPF
print(cpf.generate())

# Gerar uma lista de documentos
list_documents = cpf.generate_list(5,True, False)
for document in list_documents:
    print(document)




