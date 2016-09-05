
import subjects
import settings

def entities_display(entities, title, tmpl="{pk:>03}) {nome}"):
    print(title.upper() + ":")
    for e in entities.values():
        print(tmpl.format(**e))


def main():

    while True:

        attrs_template = "{pk:>03}) " + ", ".join([attr.upper() +"={" + attr + "}" for attr in settings.ATTRIBUTES])
        entities_display(subjects.CLIENTI, "CLIENTI", attrs_template)
        print("")
        entities_display(subjects.FORNITORI, "FORNITORI", attrs_template)

        c = raw_input("\nInserisci [cliente/1 / fornitore/2 /BASTA] ? ")
        if c.lower() in ["cliente","fornitore","1","2"]:
            entity = {}
            for attr in settings.ATTRIBUTES:
                while not entity.get(attr):
                    entity[attr] = raw_input("Inserisci {}: ".format(attr))
            
            if c in ['cliente', "1"]:
                entities = subjects.CLIENTI
            else:
                entities = subjects.FORNITORI

            entity['pk'] = pk = len(entities) + 1
            entities[pk] = entity

            print("\n------------\n")

        else:
            break

            
            
if __name__ == '__main__':
    main()
