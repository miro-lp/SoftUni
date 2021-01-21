class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


line = input()
domains = ["com", "bg", "org", "net"]

while line:
    if "@" not in line:
        raise MustContainAtSymbolError("Email must contain @")
    name, domain = line.split("@")
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    valid_domain = domain.split(".")[-1]
    if valid_domain not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is Valid")
    line = input()
