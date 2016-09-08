import json
import sys
import os

if __name__ == "__main__":

    path = sys.argv[1]
    outfname = "people_fixture.json"
    PEOPLE = []
    all_json = 0

    for root, dirs, files in os.walk(path):

        json_fnames = [ f for f in files if f.endswith(".json")]
        all_json += len(json_fnames)
        for fname in json_fnames:

            full_path = os.path.join(root, fname)
            print(full_path)
            with open(full_path, "rb") as fobj:
                PEOPLE += json.load(fobj)

    print("{} persone trovate in {} files".format(len(PEOPLE), all_json))
    with open(outfname, "wb") as outf:
        json.dump(PEOPLE, outf, indent=2)

