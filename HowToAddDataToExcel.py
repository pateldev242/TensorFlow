import xlsxwriter

data = [
    {'name': 'A',
     'phone': '1',
     'email': 'asdasdxasc',
     },
    {'name': 'B',
     'phone': '2',
     'email': 'sdasadea',
     },
    {'name': 'C',
     'phone': '3',
     'email': 'accacxaxee'
     }
]


def generateData(data):
    workbook = xlsxwriter.Workbook("TataShare.xlsx")
    worksheet = workbook.add_worksheet("firstSheet")

    worksheet.write(0, 0, "#")
    worksheet.write(0, 1, "Share Price")
    worksheet.write(0, 2, "Date and Time")
    worksheet.write(0, 3, "Up or Down")

    for index, entry in enumerate(data):
        worksheet.write(index + 1, 0, str(index))
        worksheet.write(index + 1, 1, entry["name"])
        worksheet.write(index + 1, 2, entry["phone"])
        worksheet.write(index + 1, 3, entry["email"])

    workbook.close()