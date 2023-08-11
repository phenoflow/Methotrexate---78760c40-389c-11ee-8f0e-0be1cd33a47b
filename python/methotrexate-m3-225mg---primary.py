# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"13428","system":"gprdproduct"},{"code":"14748","system":"gprdproduct"},{"code":"16519","system":"gprdproduct"},{"code":"17672","system":"gprdproduct"},{"code":"18424","system":"gprdproduct"},{"code":"20951","system":"gprdproduct"},{"code":"21889","system":"gprdproduct"},{"code":"27342","system":"gprdproduct"},{"code":"30780","system":"gprdproduct"},{"code":"32111","system":"gprdproduct"},{"code":"40293","system":"gprdproduct"},{"code":"40328","system":"gprdproduct"},{"code":"41104","system":"gprdproduct"},{"code":"41585","system":"gprdproduct"},{"code":"45558","system":"gprdproduct"},{"code":"49951","system":"gprdproduct"},{"code":"51120","system":"gprdproduct"},{"code":"52606","system":"gprdproduct"},{"code":"53385","system":"gprdproduct"},{"code":"56037","system":"gprdproduct"},{"code":"58303","system":"gprdproduct"},{"code":"59685","system":"gprdproduct"},{"code":"823","system":"gprdproduct"},{"code":"8583","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('methotrexate-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["methotrexate-m3-225mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["methotrexate-m3-225mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["methotrexate-m3-225mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
