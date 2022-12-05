'''
Jacob Humphreys 
15OCT2022
FE_supplementation_function
'''
import os
#main function
def main():

    #set expected ranges for test results
    control_uibc_expected_range = range(1,101)
    control_total_serum_iron_expected_range = range(1,101)
    control_tibc_expected_range = range(1-101)

    os.system('cls')

    #after uibc and iron is mixed - collect initial results
    uibc_initial_standard=float(input('initial UIBC standard: '))
    uibc_initial_test=float(input('initial UIBC test: '))
    uibc_initial_control=float(input('initial UIBC control: '))
    print()
    iron_initial_standard=float(input('initial iron standard: '))
    iron_initial_test=float(input('initial iron test: '))
    iron_initial_control=float(input('initial iron control: '))
    print()

    #after color agent has been added and placed in water bath for 10 min - collect final results
    uibc_final_standard=float(input('final UIBC standard: '))
    uibc_final_test=float(input('final UIBC test: '))
    uibc_final_control=float(input('final UIBC control: '))
    print()
    iron_final_standard=float(input('final iron standard: '))
    iron_final_test=float(input('final iron test: '))
    iron_final_control=float(input('final iron control: '))
    
    #calculate UIBC a, b, and c
    uibc_a=uibc_final_test-uibc_initial_test
    uibc_b=uibc_final_control-uibc_initial_control
    uibc_c=uibc_final_standard-uibc_initial_standard

    #calculate iron a, b, and c
    iron_a=iron_final_test-iron_initial_test
    iron_b=iron_final_control-iron_initial_control
    iron_c=iron_final_standard-iron_initial_standard

    #space + result title
    print()
    print('RESULTS')
    print()
    
    #call UIBC function and print results
    uibc,control_uibc=get_uibc_results(uibc_a,uibc_b,uibc_c)
    
    print()
    print(f'UIBC: {uibc}')
    print(f'Control UIBC: {control_uibc}')
    print(f'Control UIBC in range: {control_uibc == control_uibc_expected_range}')
    
    #space
    print()

    #call iron function and print results
    total_serum_iron,control_total_serum_iron=get_iron_results(iron_a,iron_b,iron_c)

    #space
    print()
    print(f'Total iron: {total_serum_iron}')
    print(f'Control total serum iron: {control_total_serum_iron}')
    print(f'Control total serum iron in range: {control_total_serum_iron == control_total_serum_iron_expected_range}')
    print()

    #calculate TIBC and Control TIBC and iron saturation
    tibc=total_serum_iron+uibc
    control_tibc=control_total_serum_iron+control_uibc
    iron_saturation=round(total_serum_iron/control_uibc)*100
    
    print(f'TIBC: {tibc}')
    print(f'Control TIBC: {control_tibc}')
    print(f'Control TIBC in range: {control_tibc == control_tibc_expected_range}')
    print()
    print(f'Iron saturation: {iron_saturation}%')
    print()
    

#use UIBC a, b, and c to calculate UIBC results
def get_uibc_results(a,b,c):
    print(f'UIBC a = {a:.3f}, b = {b:.3f}, c = {c:.3f}')
    uibc=round((500-((a/c)*500))*2)
    control_uibc=round((500-((b/c)*500))*2)
    # print(f'UIBC: {uibc}')
    # print(f'Control UIBC: {control_uibc}')
    return uibc, control_uibc

#use iron a, b, and c to calculate iron results
def get_iron_results(a,b,c):
    print(f'Iron a = {a:.3f}, b = {b:.3f}, c = {c:.3f}')
    total_serum_iron=round((a/c)*1000)
    control_total_serum_iron=round((b/c)*1000)
    # print(f'Total iron: {total_serum_iron}')
    # print(f'Expected iron: {control_total_serum_iron}')
    return total_serum_iron, control_total_serum_iron

main()