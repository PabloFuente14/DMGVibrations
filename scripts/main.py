import extract_data
import cross_data


if __name__== '__main__': 
    automator = extract_data.Automator()
    automator.run()
 
#----------------------------------------------------------
    df_valor_hora_hta = cross_data.cruce_valor_y_hta(automator.data_valor_hora, automator.data_htas)

    print("Hola...")