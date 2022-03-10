import collections

input = {
    "bl_items_lists": [
        {
            "ERPSite": "NOIT",
            "OANumber": "P00016",
            "LineOANumber": 1,
            "ReleaseOANumber": 0,
            "CodeArt": "46961100F1000",
            "SerialNumber": "AW05920-019A",
            "PalletNumber": "AW19059-5",
            "Quantity": 1,
            "ProductTemplate": "4696",
            "PrintCode": "gthf",
            "Width": 1100,
            "Length": 1090,
            "UsableWidth": 1100,
            "Quality": "ghf",
            "Weld": 0,
            "Printed": "gfh",
            "Perforated": "gh",
            "Edge": "0ed",
            "Core": "ghf",
            "Packaging": "gfh"
        },
        {
            "ERPSite": "NOIT",
            "OANumber": "P00016",
            "LineOANumber": 2,
            "ReleaseOANumber": 0,
            "CodeArt": "46961100F1000",
            "SerialNumber": "ACOUSTIC-019B",
            "PalletNumber": "AW19059-5",
            "Quantity": 1,
            "ProductTemplate": "4696",
            "PrintCode": "il",
            "Width": 1100,
            "Length": 1090,
            "UsableWidth": 1100,
            "Quality": "iul",
            "Weld": 0,
            "Printed": "yjt",
            "Perforated": "yj",
            "Edge": "0ed",
            "Core": "tdj",
            "Packaging": "yjt"
        }
    ]
}


class SubObjectMassReception:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


delivery_lines = input["bl_items_lists"]

receptions = collections.defaultdict(list)

for line in delivery_lines:
    reception = SubObjectMassReception(**line)
    po_number_line = line['OANumber'] + "_" + line['ERPSite']
    receptions[po_number_line].append(reception)

for po, po_lines in receptions.items():
    test = po_lines[0]
    erp_site = po_lines[0].ERPSite
    po_number = po_lines[0].OANumber

for po_line in po_lines:
    i = 1
    print(po_line)
