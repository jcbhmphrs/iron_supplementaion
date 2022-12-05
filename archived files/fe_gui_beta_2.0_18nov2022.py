from tkinter import *
from tkinter.ttk import Labelframe
from datetime import datetime
'''
Jacob Humphreys 
15OCT2022
FE_supplementation_function
'''

root = Tk()
root.title('Iron supplementation @ Cytiva; CopyWrite - Jacob Humphreys')
#main function
def main():
    #set expected ranges for test results
    control_uibc_expected_range = range(109,184)
    control_total_serum_iron_expected_range = range(47,72)
    control_tibc_expected_range = range(156,255)

    #UIBC Initial Fields
    uibc_initial_labelframe = LabelFrame(root, bg='#ffffe6',text='UIBC INITIAL READINGS')
    uibc_initial_labelframe.grid(row=0, column=0,padx=10,pady=10)

    uibc_initial_standard_label=Label(uibc_initial_labelframe,bg='#ffffe6', text='Initial UIBC standard')
    uibc_initial_standard_label.pack(padx=5, pady=3)
    uibc_initial_standard=Entry(uibc_initial_labelframe, width=10)
    #take out later
    uibc_initial_standard.insert(END,'0.001')
    uibc_initial_standard.pack(padx=5, pady=3)

    uibc_initial_test_label=Label(uibc_initial_labelframe, bg='#ffffe6',text='Initial UIBC test')
    uibc_initial_test_label.pack(padx=5, pady=3)
    uibc_initial_test=Entry(uibc_initial_labelframe, width=10)
    #take out later
    uibc_initial_test.insert(END,'0.019')
    uibc_initial_test.pack(padx=5, pady=3)

    uibc_initial_control_label=Label(uibc_initial_labelframe,bg='#ffffe6', text='Initial UIBC control')
    uibc_initial_control_label.pack(padx=5, pady=3)
    uibc_initial_control=Entry(uibc_initial_labelframe, width=10)
    #take out later
    uibc_initial_control.insert(END,'0.023')
    uibc_initial_control.pack(padx=5, pady=3)

    #Iron Initial Fields
    iron_initial_labelframe = LabelFrame(root, bg= '#ff9999' , text="IRON INITIAL READINGS")
    iron_initial_labelframe.grid(row=1, column=0,padx=10,pady=10)
 
    iron_initial_standard_label=Label(iron_initial_labelframe,bg='#ff9999',text='Initial iron standard')
    iron_initial_standard_label.pack(padx=5, pady=3)
    iron_initial_standard=Entry(iron_initial_labelframe,width=10)
    #take out later
    iron_initial_standard.insert(END,'0.002')
    iron_initial_standard.pack(padx=5, pady=3)

    iron_initial_test_label=Label(iron_initial_labelframe,bg='#ff9999',text='Initial iron test')
    iron_initial_test_label.pack(padx=5, pady=3)
    iron_initial_test=Entry(iron_initial_labelframe,width=10)
    #take out later
    iron_initial_test.insert(END,'0.011')
    iron_initial_test.pack(padx=5, pady=3)

    iron_initial_control_label=Label(iron_initial_labelframe,bg='#ff9999',text='Initial iron control')
    iron_initial_control_label.pack(padx=5, pady=3)
    iron_initial_control=Entry(iron_initial_labelframe,width=10)
    #take out later
    iron_initial_control.insert(END,'0.021')
    iron_initial_control.pack(padx=5, pady=3)

    #UIBC Final Fields
    uibc_final_labelframe = LabelFrame(root,bg='#ffffe6', text="UIBC FINAL READINGS")
    uibc_final_labelframe.grid(row=0, column=1,padx=10,pady=10)
 
    uibc_final_standard_label=Label(uibc_final_labelframe,bg='#ffffe6', text='Final UIBC standard')
    uibc_final_standard_label.pack(padx=5, pady=3)
    uibc_final_standard=Entry(uibc_final_labelframe, width=10)
    #take out later
    uibc_final_standard.insert(END,'0.437')
    uibc_final_standard.pack(padx=5, pady=3)

    uibc_final_test_label=Label(uibc_final_labelframe,bg='#ffffe6', text='Final UIBC test')
    uibc_final_test_label.pack(padx=5, pady=3)
    uibc_final_test=Entry(uibc_final_labelframe, width=10)
    #take out later
    uibc_final_test.insert(END,'0.315')
    uibc_final_test.pack(padx=5, pady=3)

    uibc_final_control_label=Label(uibc_final_labelframe,bg='#ffffe6', text='Final UIBC control')
    uibc_final_control_label.pack(padx=5, pady=3)
    uibc_final_control=Entry(uibc_final_labelframe, width=10)
    #take out later
    uibc_final_control.insert(END,'0.383')
    uibc_final_control.pack(padx=5, pady=3)

    #Iron Final Fields
    iron_final_labelframe = LabelFrame(root, bg='#ff9999',text="IRON FINAL READINGS")
    iron_final_labelframe.grid(row=1, column=1,padx=10,pady=10)
 
    iron_final_standard_label=Label(iron_final_labelframe,bg='#ff9999',text='Final iron standard')
    iron_final_standard_label.pack(padx=5, pady=3)
    iron_final_standard=Entry(iron_final_labelframe,width=10)
    #take out later
    iron_final_standard.insert(END,'0.401')
    iron_final_standard.pack(padx=5, pady=3)

    iron_final_test_label=Label(iron_final_labelframe,bg='#ff9999',text='Final iron test')
    iron_final_test_label.pack(padx=5, pady=3)
    iron_final_test=Entry(iron_final_labelframe,width=10)
    #take out later
    iron_final_test.insert(END,'0.256')
    iron_final_test.pack(padx=5, pady=3)

    iron_final_control_label=Label(iron_final_labelframe,bg='#ff9999',text='Final iron control')
    iron_final_control_label.pack(padx=5, pady=3)
    iron_final_control=Entry(iron_final_labelframe,width=10)
    #take out later
    iron_final_control.insert(END,'0.045')
    iron_final_control.pack(padx=5, pady=3)
    
    def get_calculations():
        #calculate
        #calculate UIBC a, b, and c
        uibc_a=(float(uibc_final_test.get()))-(float(uibc_initial_test.get()))
        uibc_b=(float(uibc_final_control.get()))-(float(uibc_initial_control.get()))
        uibc_c=(float(uibc_final_standard.get()))-(float(uibc_initial_standard.get()))

        #calculate iron a, b, and c
        iron_a=(float(iron_final_test.get()))-(float(iron_initial_test.get()))
        iron_b=(float(iron_final_control.get()))-(float(iron_initial_control.get()))
        iron_c=(float(iron_final_standard.get()))-(float(iron_initial_standard.get()))

        #calculate UIBC and UIBC control
        uibc=round((500-((uibc_a/uibc_c)*500))*2)
        control_uibc=round((500-((uibc_b/uibc_c)*500))*2)

        #calculate Total Iron and Total Iron Control
        total_serum_iron=round((iron_a/iron_c)*1000)
        control_total_serum_iron=round((iron_b/iron_c)*1000)
        
        #calculate TIBC and Control TIBC and iron saturation
        tibc=total_serum_iron+uibc
        control_tibc=control_total_serum_iron+control_uibc
        iron_saturation=round((total_serum_iron/tibc)*100)

        #output results
        uibc_variables_labelframe = LabelFrame(root, text='UIBC Variables')
        uibc_variables_labelframe.grid(row=3, columnspan=2)
        label_1=Label(uibc_variables_labelframe, text=f'A: {uibc_a:.3f} ; B: {uibc_b:.3f} ; C: {uibc_c:.3f}')
        label_1.pack()
        uibc_results_labelframe = Labelframe(root,text='UIBC')
        uibc_results_labelframe.grid(row=4, columnspan=2)
        label_2=Label(uibc_results_labelframe, text=f'{uibc} ; Control:{control_uibc} ; In Range: {control_uibc in control_uibc_expected_range}')
        label_2.pack()
        iron_variables_labelframe=Labelframe(root, text='Iron Variables')
        iron_variables_labelframe.grid(row=5,columnspan=2)
        label_3=Label(iron_variables_labelframe,text=f'A: {iron_a:.3f} ; B: {iron_b:.3f} ; C: {iron_c:.3f}')
        label_3.pack()
        total_serum_iron_labelframe=Labelframe(root,text='Total Serum Iron')
        total_serum_iron_labelframe.grid(row=6,columnspan=2)
        label_4=Label(total_serum_iron_labelframe,text=f'{total_serum_iron} ; Control: {control_total_serum_iron} ; In Range: {control_total_serum_iron in control_total_serum_iron_expected_range}')
        label_4.pack()
        tibc_labelframe=LabelFrame(root,text='TIBC')
        tibc_labelframe.grid(row=7,columnspan=2)
        label_5=Label(tibc_labelframe,text=f'{tibc} ; Control: {control_tibc} ; In Range: {control_tibc in control_tibc_expected_range}')
        label_5.pack()
        iron_saturation_labelframe=LabelFrame(root,text='Iron Saturation')
        iron_saturation_labelframe.grid(row=8, columnspan=2)
        label_6=Label(iron_saturation_labelframe,text=f'{iron_saturation}%')
        label_6.pack()
        
        #send results to a text file for record keeping. bothe in range and out of range results.
        with open('supplementation_results.txt','at') as results:
            #print information to the file
            print(f'{datetime.now():%d-%b-%Y},{uibc_a},{uibc_b},{uibc_c},{uibc},{control_uibc},{iron_a},{iron_b},{iron_c},{total_serum_iron},{control_total_serum_iron},{tibc},{control_tibc},{iron_saturation}', file=results)

    button_results=Button(root,bg='#b3ff99',text='Get Results',pady=10, command=get_calculations)
    button_results.grid(row=2,columnspan=2,pady=20)

main()

root.mainloop()