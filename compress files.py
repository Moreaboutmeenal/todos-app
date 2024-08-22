import FreeSimpleGUI as sg

label1 = sg.Text("Enter the Feet ")
input1 = sg.Input()

label2 = sg.Text("Enter the Inches")
input2 = sg.Input()

Convert_button = sg.Button("Compress")

window = sg.Window('Compress Files',layout=[[label1,input1],
                                            [label2,input2],
                                            [Convert_button]])

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")

window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1,
                            option2,
                            option3,
                            option4],
                           ])

window.read()
window.close()

