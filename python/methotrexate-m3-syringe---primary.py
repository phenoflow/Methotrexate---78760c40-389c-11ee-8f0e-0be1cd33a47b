# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"14347","system":"gprdproduct"},{"code":"16540","system":"gprdproduct"},{"code":"26064","system":"gprdproduct"},{"code":"30703","system":"gprdproduct"},{"code":"32865","system":"gprdproduct"},{"code":"40273","system":"gprdproduct"},{"code":"40281","system":"gprdproduct"},{"code":"40371","system":"gprdproduct"},{"code":"44908","system":"gprdproduct"},{"code":"45165","system":"gprdproduct"},{"code":"7337","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('methotrexate-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["methotrexate-m3-syringe---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["methotrexate-m3-syringe---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["methotrexate-m3-syringe---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
