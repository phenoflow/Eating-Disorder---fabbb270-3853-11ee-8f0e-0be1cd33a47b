# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Jonathan Green, Carolyn A Chew-Graham, Nav Kapur, Darren M Aschcroft, 2023.

import sys, csv, re

codes = [{"code":"E275400","system":"readv2"},{"code":"Eu50511","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('eating-disorder-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["eating-disorder-vomiting---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["eating-disorder-vomiting---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["eating-disorder-vomiting---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)