import csv
import argparse


def extend_csv(csv_path_input, csv_path_output):
    with open(csv_path_input, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader, None)
        new_rows = []
        for row in csv_reader:
            disciplines = row[13].split(',')
            disciplines_var = [] if row[14] is None else row[14].split(',')
            max_len = max(len(disciplines), len(disciplines_var))
            rows = []
            for disc_i in range(max_len):
                current_row = row.copy()
                new_disc = disciplines[disc_i].strip() if disc_i < len(disciplines) else None
                new_disc_var = disciplines_var[disc_i].strip() if disc_i < len(disciplines_var) else None
                current_row[13] = new_disc
                current_row[14] = new_disc_var
                rows.append(current_row)
            new_rows.extend(rows)

    with open(csv_path_output, 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)
        for row in new_rows:
            csv_writer.writerow(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="source_csv", help="source table")
    parser.add_argument(dest="target_csv", help="extended table")
    args = parser.parse_args()

    extend_csv(args.source_csv, args.target_csv)
    # extend_csv('merged.csv', 'merged_extended.csv')
