from tkinter import *
from tkinter.ttk import Labelframe
from datetime import datetime
from number_entry import *
'''
Jacob Humphreys 
15OCT2022
FE_supplementation_function
'''

root = Tk()
root.title('Iron supplementation Cytiva; CopyWrite - Jacob Humphreys')
root.configure(bg='#e6e6e6')
root.iconbitmap('beaker.ico')
root.geometry('900x600')
bg = PhotoImage(file='background_image.png')
background_label = Label(root, image=bg)
background_label.place(x=0,y=0,relheight=1,relwidth=1)
#set expected ranges for test results
control_uibc_expected_range = range(109,184)
control_total_serum_iron_expected_range = range(47,72)
control_tibc_expected_range = range(156,255)



#main function
def main():
    

 #GUI

    #UIBC Initial Fields
    uibc_initial_labelframe = LabelFrame(root, bg='#fcab88',text='UIBC INITIAL READINGS',pady=15)
    uibc_initial_labelframe.grid(row=0, column=0,padx=40,pady=30)

    uibc_initial_standard_label=Label(uibc_initial_labelframe,bg='#fcab88', text='Standard')
    uibc_initial_standard_label.pack(padx=5, pady=3)
    uibc_initial_standard=FloatEntry(uibc_initial_labelframe,0,10,width=10)
    #take out later
    uibc_initial_standard.insert(END,'0.001')
    uibc_initial_standard.pack(padx=5, pady=3)

    uibc_initial_test_label=Label(uibc_initial_labelframe, bg='#fcab88',text= 'Test')
    uibc_initial_test_label.pack(padx=5, pady=3)
    uibc_initial_test=FloatEntry(uibc_initial_labelframe,0,10,width=10)
    #take out later
    uibc_initial_test.insert(END,'0.019')
    uibc_initial_test.pack(padx=5, pady=3)

    uibc_initial_control_label=Label(uibc_initial_labelframe,bg='#fcab88', text='Control')
    uibc_initial_control_label.pack(padx=5, pady=3)
    uibc_initial_control=FloatEntry(uibc_initial_labelframe,0,10,width=10)
    #take out later
    uibc_initial_control.insert(END,'0.023')
    uibc_initial_control.pack(padx=5, pady=3)

    #Iron Initial Fields
    iron_initial_labelframe = LabelFrame(root, bg= '#cc3923' , text='IRON INITIAL READINGS', pady=15)
    iron_initial_labelframe.grid(row=1, column=0,padx=40,pady=10)
 
    iron_initial_standard_label=Label(iron_initial_labelframe,bg='#cc3923',text='Standard')
    iron_initial_standard_label.pack(padx=5, pady=3)
    iron_initial_standard=FloatEntry(iron_initial_labelframe,0,10, width=10)
    #take out later
    iron_initial_standard.insert(END,'0.002')
    iron_initial_standard.pack(padx=5, pady=3)

    iron_initial_test_label=Label(iron_initial_labelframe,bg='#cc3923',text='Test')
    iron_initial_test_label.pack(padx=5, pady=3)
    iron_initial_test=FloatEntry(iron_initial_labelframe,0,10, width=10)
    #take out later
    iron_initial_test.insert(END,'0.011')
    iron_initial_test.pack(padx=5, pady=3)

    iron_initial_control_label=Label(iron_initial_labelframe,bg='#cc3923',text='Control')
    iron_initial_control_label.pack(padx=5, pady=3)
    iron_initial_control=FloatEntry(iron_initial_labelframe,0,10, width=10)
    #take out later
    iron_initial_control.insert(END,'0.021')
    iron_initial_control.pack(padx=5, pady=3)

    #UIBC Final Fields
    uibc_final_labelframe = LabelFrame(root,bg='#fcab88', text='UIBC FINAL READINGS', pady=15)
    uibc_final_labelframe.grid(row=0, column=1,padx=40,pady=30)
 
    uibc_final_standard_label=Label(uibc_final_labelframe,bg='#fcab88', text='Standard')
    uibc_final_standard_label.pack(padx=5, pady=3)
    uibc_final_standard=FloatEntry(uibc_final_labelframe,0,10,  width=10)
    #take out later
    uibc_final_standard.insert(END,'0.437')
    uibc_final_standard.pack(padx=5, pady=3)

    uibc_final_test_label=Label(uibc_final_labelframe,bg='#fcab88', text='Test')
    uibc_final_test_label.pack(padx=5, pady=3)
    uibc_final_test=FloatEntry(uibc_final_labelframe,0,10,  width=10)
    #take out later
    uibc_final_test.insert(END,'0.315')
    uibc_final_test.pack(padx=5, pady=3)

    uibc_final_control_label=Label(uibc_final_labelframe,bg='#fcab88', text='Control')
    uibc_final_control_label.pack(padx=5, pady=3)
    uibc_final_control=FloatEntry(uibc_final_labelframe, 0,10, width=10)
    #take out later
    uibc_final_control.insert(END,'0.383')
    uibc_final_control.pack(padx=5, pady=3)

    #Iron Final Fields
    iron_final_labelframe = LabelFrame(root, bg='#cc3923',text='IRON FINAL READINGS', pady=15)
    iron_final_labelframe.grid(row=1, column=1,padx=40,pady=10)
 
    iron_final_standard_label=Label(iron_final_labelframe,bg='#cc3923',text='Standard')
    iron_final_standard_label.pack(padx=5, pady=3)
    iron_final_standard=FloatEntry(iron_final_labelframe,0,10, width=10)
    #take out later
    iron_final_standard.insert(END,'0.401')
    iron_final_standard.pack(padx=5, pady=3)

    iron_final_test_label=Label(iron_final_labelframe,bg='#cc3923',text='Test')
    iron_final_test_label.pack(padx=5, pady=3)
    iron_final_test=FloatEntry(iron_final_labelframe,0,10, width=10)
    #take out later
    iron_final_test.insert(END,'0.256')
    iron_final_test.pack(padx=5, pady=3)

    iron_final_control_label=Label(iron_final_labelframe,bg='#cc3923',text='Control')
    iron_final_control_label.pack(padx=5, pady=3)
    iron_final_control=FloatEntry(iron_final_labelframe,0,10, width=10)
    #take out later
    iron_final_control.insert(END,'0.045')
    iron_final_control.pack(padx=5, pady=3)
    
    #output fields
    result_frame = Frame(root,pady=5,bg='#c7f2f1')
    result_frame.grid(row=0,rowspan = 3 ,column = 3, padx=20,pady=20)

    uibc_variables_labelframe = LabelFrame(result_frame, text='UIBC Var')
    uibc_variables_labelframe.grid(row=3, column=0,padx=20, pady=10)
    label_1=Label(uibc_variables_labelframe,text=f'A:    \nB:    \nC:    ')
    label_1.pack()

    uibc_results_labelframe = Labelframe(result_frame,text='UIBC')
    uibc_results_labelframe.grid(row=3, column=1,padx=20, pady=10)
    label_2=Label(uibc_results_labelframe,text=f'\nControl:\nIn Range:')
    label_2.pack()

    iron_variables_labelframe=Labelframe(result_frame, text='Iron Var')
    iron_variables_labelframe.grid(row=4,column=0,padx=20, pady=10)
    label_3=Label(iron_variables_labelframe,text=f'A:    \nB:    \nC:    ')
    label_3.pack()

    total_serum_iron_labelframe=Labelframe(result_frame,text='TSI')
    total_serum_iron_labelframe.grid(row=4,column=1,padx=20, pady=10)
    label_4=Label(total_serum_iron_labelframe,text=f'\nControl:\nIn Range:')
    label_4.pack()

    tibc_labelframe=LabelFrame(result_frame,text='TIBC')
    tibc_labelframe.grid(row=5,column=0,padx=20, pady=10)
    label_5=Label(tibc_labelframe,text=f'\nControl:\nIn Range:')
    label_5.pack()

    iron_saturation_labelframe=LabelFrame(result_frame,text='Iron %')
    iron_saturation_labelframe.grid(row=5, column=1,pady=10)
    label_6=Label(iron_saturation_labelframe)
    label_6.pack()

    #button clear command
    def clear_all_fields():
        uibc_initial_test.delete(0, END)
        uibc_initial_control.delete(0, END)
        uibc_initial_standard.delete(0, END)
        iron_initial_test.delete(0, END)
        iron_initial_control.delete(0, END)
        iron_initial_standard.delete(0, END)
        uibc_final_test.delete(0, END)
        uibc_final_control.delete(0, END)
        uibc_final_standard.delete(0, END)
        iron_final_test.delete(0, END)
        iron_final_control.delete(0, END)
        iron_final_standard.delete(0, END)
        label_1.config(text='')
        label_2.config(text='')
        label_3.config(text='')
        label_4.config(text='')
        label_5.config(text='')
        label_6.config(text='')

    #button Get Results command
    def compute_and_print_results():
            
        def get_a_b_c_from_gui():
            #calculate UIBC a, b, and c
            global uibc_a
            uibc_a=(uibc_final_test.get())-(uibc_initial_test.get())
            global uibc_b
            uibc_b=(uibc_final_control.get())-(uibc_initial_control.get())
            global uibc_c
            uibc_c=(uibc_final_standard.get())-(uibc_initial_standard.get())

            #calculate iron a, b, and c
            global iron_a
            iron_a=((iron_final_test.get()))-((iron_initial_test.get()))
            global iron_b
            iron_b=((iron_final_control.get()))-((iron_initial_control.get()))
            global iron_c    
            iron_c=((iron_final_standard.get()))-((iron_initial_standard.get()))
        
        def reconfigure_output_labels():
            #reconfigure the output results
            label_1.config(text=f'A: {uibc_a:.3f}\nB: {uibc_b:.3f}\nC: {uibc_c:.3f}')
            label_2.config(text=f'{uibc}\nControl:{control_uibc}\nIn Range: {control_uibc in control_uibc_expected_range}')
            label_3.config(text=f'A: {iron_a:.3f}\nB: {iron_b:.3f}\nC: {iron_c:.3f}')
            label_4.config(text=f'{total_serum_iron}\nControl: {control_total_serum_iron}\nIn Range: {control_total_serum_iron in control_total_serum_iron_expected_range}')
            label_5.config(text=f'{tibc}\nControl: {control_tibc}\nIn Range: {control_tibc in control_tibc_expected_range}')
            label_6.config(text=f'{iron_saturation}%')
        
        get_a_b_c_from_gui()

        #calculate UIBC and UIBC control
        global uibc
        uibc=round((500-((uibc_a/uibc_c)*500))*2)
        global control_uibc
        control_uibc=round(((500-(uibc_b/uibc_c)*500))*2)

        #calculate Total Iron and Total Iron Control
        global total_serum_iron
        total_serum_iron=round((iron_a/iron_c)*1000)
        global control_total_serum_iron
        control_total_serum_iron=round((iron_b/iron_c)*1000)
        
        #calculate TIBC and Control TIBC and iron saturation
        global tibc
        tibc=total_serum_iron+uibc
        global control_tibc
        control_tibc=control_total_serum_iron+control_uibc
        
        iron_saturation=round((total_serum_iron/tibc)*100)


        
        write_to_textfile('supplementation_results.txt',iron_saturation)
        reconfigure_output_labels()


    def write_to_textfile(file_name, iron_saturation):
        #send results to a text file for record keeping. bothe in range and out of range results.
        with open('supplementation_results.txt','at') as results:
            #print information to the file
            print(f'{datetime.now():%d-%b-%Y},{uibc_a},{uibc_b},{uibc_c},{uibc},{control_uibc},{iron_a},{iron_b},{iron_c},{total_serum_iron},{control_total_serum_iron},{tibc},{control_tibc},{iron_saturation}', file=results)

    

    #buttons
    clear_all_b = Button(root, bg='#c7f2f1',width=15,text='Clear All', pady=10, command= clear_all_fields)
    clear_all_b.grid(row=2, column=0,pady=20)

    results_b=Button(root,bg='#b3ff99',text='Get Results',width=15,pady=10, command= compute_and_print_results)
    results_b.grid(row=2,column = 1,pady=20)


    root.mainloop()

if __name__ == '__main__':
    main()