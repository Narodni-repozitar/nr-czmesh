import csv
from csv import DictWriter
from pathlib import Path

from pymarc import MARCReader, Record


def run(file: str = '/tmp/MeSH2020_Marc21-DW.mrc', output: str = "/tmp/czmesh.csv"):
    path, file_name = output.rsplit('/', 1)
    if not Path(path).exists():
        Path(path).mkdir(parents=True)
    with open(file, 'rb') as fh, open(output, 'w') as csvfile:
        fieldnames = ['slug', 'title_cs', 'title_en', 'relatedURI_0', 'relatedURI_1',
                      *[f"TreeNumberList_{i}" for i in range(get_max_tree_number_list(file)[0])]]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        reader = MARCReader(fh)
        for i, record in enumerate(reader):
            result = get_dict_from_record(record)
            save_csv_from_dict(result, writer)
            print(f"Record number: {i}")


def get_dict_from_record(record: Record) -> dict:
    result = {}
    for field in record:
        if hasattr(field, "subfields"):
            subfields = {}
            for i, subfield in enumerate(field.subfields):
                if i % 2 == 0:
                    key = subfield
                else:
                    value = subfield
                    if key:
                        subfields[key] = value
            if res := result.get(field.tag):
                if isinstance(res, dict):
                    result[field.tag] = [res, subfields]
                else:
                    res.append(subfields)
                    result[field.tag] = res
            else:
                result[field.tag] = subfields
        else:
            result[field.tag] = field.data
    return result


def get_tree_list_header(result):
    l = len(result)
    res = []
    for i in range(l):
        res.append(f"TreeNumberList_{i}")
    return res


def get_tree_number(record):
    el = record.get("686")
    result = []
    if not el:
        return
    if isinstance(el, dict):
        result.extend(get_tree_path(el))
    if isinstance(el, (tuple, list)):
        for _ in el:
            result.extend(get_tree_path(_))
    header = get_tree_list_header(result)
    return header, result


def get_tree_path(el):
    res = []
    value = el.get("a")
    array = value.split(".")
    for _ in array:
        if res:
            res.append(".".join([res[-1], _]))
        else:
            res.append(_)
    return res


def save_csv_from_dict(record: dict, writer: DictWriter):
    tree_number_header, tree_number_list = get_tree_number(record)
    slug = record["001"]
    try:
        row = {
            "slug": slug,
            "title_cs": record.get("150", {}).get("a") or record.get("155", {}).get("a"),
            "title_en": record.get("750", {}).get("a") or record.get("755", {}).get("a"),
            "relatedURI_0": f"http://www.medvik.cz/link/{slug}",
            "relatedURI_1": f"http://id.nlm.nih.gov/mesh/{slug}",
        }
    except:
        print(record)
        raise
    for i, _ in enumerate(tree_number_list):
        row[f"TreeNumberList_{i}"] = _
    writer.writerow(row)


def get_max_tree_number_list(path: str):
    with open(path, 'rb') as fh:
        reader = MARCReader(fh)
        length = 0
        final_header = None
        for i, record in enumerate(reader):
            print(i)
            result = get_dict_from_record(record)
            header, tree_number_list = get_tree_number(result)
            l = len(header)
            if l > length:
                length = l
                final_header = header
        return length, final_header


if __name__ == '__main__':
    run()
