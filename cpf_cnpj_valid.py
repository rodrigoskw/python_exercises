import validate_docbr

cpf = validate_docbr.CPF()

print(cpf.generate())

list_documents = cpf.generate_list(5,True, False)
for document in list_documents:
    print(document)




