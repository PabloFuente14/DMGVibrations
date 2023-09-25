import extract_data
import cross_data


if __name__== '__main__': 
    automator = extract_data.Automator()
    automator.run()
    #data_valor_hora = automator.data_valor_hora
    #data_htas = automator.data_htas
    #data_ofs = automator.data_ofs

    #------------------Nuevo
    df_valor_hora_hta = cross_data.cruce_valor_y_hta(automator.data_valor_hora, automator.data_htas)

    print("Hola...")