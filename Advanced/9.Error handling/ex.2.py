import exceptions

domain_names = ["com", "bg", "org", "net"]

command = input("enter command or email")

while command != "End":
    email = command

    if "@" not in email:
        raise exceptions.MustContainAtSymbolError("Email must contain @")

    name, domain = email.split("@")
    domain_address = domain.split(".")[1]
    if len(name) <= 4:
        raise exceptions.NameTooShortError("Name must be more than 4 characters")

    if domain_address not in domain_names:
        raise exceptions.InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    command = input()