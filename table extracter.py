from docx import Document
import pandas as pd
import os

def print_dictionary(the_big_dictionary):
    for key in the_big_dictionary.keys():
        print(key,end=", ")
    print()
    for i in range(len(the_big_dictionary["Register Number"])):
        print(the_big_dictionary["Register Number"][i],the_big_dictionary["Student Name"][i],
              the_big_dictionary["Subject Code"][i],the_big_dictionary["Grade"][i],the_big_dictionary["Exam Date"][i])
def find_exam_date():
    n=0
    catch = -1
    exam_date = list()
    remove_data = ["Examination","Provisional Results of",".",","]
    for paragraph in doc.paragraphs:
        if (paragraph.text == "ANNA UNIVERSITY :: CHENNAI - 600025."):
            catch =  3
            n+=1
        catch = catch - 1
        if catch == 0:
            text = paragraph.text
            for x in remove_data:
                text = text.replace(x,"")
            exam_date.append(text[1:].replace(" / ","/"))
    if not len(exam_date) is len(doc.tables):
        raise Exception("Table and Title Matching Error")
    return exam_date 
def convert_to_dictionary(model):
    current_dir = os.getcwd()
    the_big_dictionary = {"Register Number":[],"Student Name":[],"Subject Code":[],"Grade":[],"Exam Date":[]}
    for file in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, file)) and file.endswith(".docx"):
            exam_date = file.replace(".docx","")
            doc = Document(os.path.join(current_dir, file))
            if model == "full":
                for table_index, table in enumerate(doc.tables):
                    if table.rows[0].cells[0].text == "": 
                        sub_codes = [cell.text for cell in table.rows[0].cells[3:]]
                        grades = [row.cells[3:] for row in table.rows[2:]]
                        for i,sub_code in enumerate(sub_codes):
                            grade_list = []
                            for j,grade in enumerate(grades):
                                grade_list.append(grade[i].text)
                            the_big_dictionary["Subject Code"].extend([sub_code for row in table.rows[2:]])
                            the_big_dictionary["Register Number"].extend([row.cells[0].text for row in table.rows[2:]])
                            the_big_dictionary["Student Name"].extend([row.cells[1].text.replace("\n"," ") for row in table.rows[2:]])
                            the_big_dictionary["Grade"].extend(grade_list)
                            the_big_dictionary["Exam Date"].extend([exam_date for row in table.rows[2:]])
            if model=="result release":
                for table_index, table in enumerate(doc.tables):
                    if table.rows[0].cells[0].text == "": 
                        sub_codes = [cell.text for cell in table.rows[0].cells[2:]]
                        grades = [row.cells[2:] for row in table.rows[2:]]
                        for i,sub_code in enumerate(sub_codes):
                            grade_list = []
                            for j,grade in enumerate(grades):
                                grade_list.append(grade[i].text)
                            the_big_dictionary["Subject Code"].extend([sub_code for row in table.rows[2:]])
                            the_big_dictionary["Register Number"].extend([row.cells[0].text for row in table.rows[2:]])
                            the_big_dictionary["Student Name"].extend([row.cells[1].text.replace("\n"," ") for row in table.rows[2:]])
                            the_big_dictionary["Grade"].extend(grade_list)
                            the_big_dictionary["Exam Date"].extend([exam_date for row in table.rows[2:]])
                    else:   
                        grades = [row.cells[2:] for row in table.rows]
                        for i,sub_code in enumerate(sub_codes):
                            grade_list = []
                            for j,grade in enumerate(grades):
                                grade_list.append(grade[i].text)
                            the_big_dictionary["Subject Code"].extend([sub_code for row in table.rows])
                            the_big_dictionary["Register Number"].extend([row.cells[0].text for row in table.rows])
                            the_big_dictionary["Student Name"].extend([row.cells[1].text.replace("\n"," ") for row in table.rows])
                            the_big_dictionary["Grade"].extend(grade_list)
                            the_big_dictionary["Exam Date"].extend([exam_date for row in table.rows])
    return the_big_dictionary
#print_dictionary(convert_to_dictionary(r"result.docx","result release","Apr"))
pd.DataFrame(convert_to_dictionary("result release")).to_excel("result.xlsx")
