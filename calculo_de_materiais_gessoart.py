#BASE DE DADOS DE PREÇOS
import math

preco_chapa_st = 41.9
preco_placa_ru = 60.0
preco_guia48 = 13.9
preco_guia70 = 16.9
preco_guia90 = 23.0
preco_montante48 = 14.7
preco_montante70 = 18.5
preco_montante90 = 27.0
preco_cantoneira = 7.3
preco_perfilf530 = 10.7
preco_tirante = 7.0
preco_suporte = 1.5
preco_fitatelada_p = 15.0
preco_fitatelada_g = 23.0
preco_prego = 10.0
preco_massa5kg = 30.0
preco_massa15kg = 55.0
preco_massa25kg = 80.0
preco_parafuso_mma = 10.0
preco_parafuso_gn25a = 10.0
preco_conectorf530 = 2.0

print("Base de dados OK!")

#BASE DE CÁLCULOS SIMPLES

#while_1 para medir o lado 1 ou o pé direito
while True:

  try:
    medida_1 = input("Digite a metragem do pé direito ou do lado 1: ").replace(',','.')
    medida_1 = float(medida_1)
    break

  except:
    print("Algum dígito foi inserido incorretamente. Tente novamente!")


#while_2 para medir o lado 2 ou o chão
while True:

  try:
    medida_2 = input("Digite a metragem do chão ou do lado 2: ").replace(',', '.')
    medida_2 = float(medida_2)
    break

  except:
    print("Algum dígito foi inserido incorretamente. Tente novamente!")


#Cálculo de área quadrilátera (Lado x Lado = L²)
area = (medida_1 * medida_2)
print(area)


print("Base de cálculo simples ok!")


#BASE DE CÁLCULO DE MATERIAL PARA TETO PLAQUINHA

#BASE DE CÁLCULO DE MATERIAL PARA TETO DRYWALL

def medida_teto():
  #CHAPA
  chapa_teto_st_calc = math.ceil(area / 2) #Cálculo de chapa para teto. Área/2 arredondando para cima.
  preco_total_chapa_teto = chapa_teto_st_calc * preco_chapa_st
  print(f"{chapa_teto_st_calc} CHAPA ACARTONADO ST = R${round(preco_total_chapa_teto, 2)}")
  #___________________________________________________________________________________________

  #PERFIL F-530
  perfil_f530_calc = math.ceil(area / 1.8) #Cálculo de perfil para teto. Área/1.8 arredondando para cima.
  preco_total_perfilf530 = perfil_f530_calc * preco_perfilf530
  print(f"{perfil_f530_calc} PERFIL F-530 = R${round(preco_total_perfilf530, 2)}")
  #___________________________________________________________________________________________

  #CANTONEIRA EM L 25X30
  cantoneira_padrao_calc = math.ceil((medida_1 + medida_2) * 2 / 3) #Cálculo de cantoneira para teto. Perímetro da medida ([m1 + m2] * 2 / 3) arredondando para cima.
  preco_total_cantoneira_padrao = cantoneira_padrao_calc * preco_cantoneira
  print(f"{cantoneira_padrao_calc} CANTONEIRA 25 x 30 = R${round(preco_total_cantoneira_padrao, 2)}")
  #___________________________________________________________________________________________

  #SUPORTE REGULADOR
  suporte_regulador_calc = chapa_teto_st_calc * 4 #Cálculo de suporte para teto
  preco_total_suporte_regulador = suporte_regulador_calc * preco_suporte
  print(f"{suporte_regulador_calc} SUPORTE REGULADOR = R${round(preco_total_suporte_regulador)}")
  #___________________________________________________________________________________________

  #CONECTOR DE PERFIL
  conector_perfilf530_calc = math.ceil(area) # 1 conector por m².
  preco_total_conector_perfilf530 = preco_conectorf530 * conector_perfilf530_calc
  print(f"{conector_perfilf530_calc} CONECTOR/UNIÃO DE PERFIL F-530 = R${round(preco_total_conector_perfilf530, 2)}")
  #___________________________________________________________________________________________

  #ARAME TIRANTE
  tirante_calc = math.ceil(area * 1.25 / 3)
  preco_total_tirante = tirante_calc * preco_tirante
  print(f"{tirante_calc} TIRANTE DE 3 METROS= R$ {round(preco_total_tirante, 2)}")
  #___________________________________________________________________________________________

  #PARAFUSO GN 25 AGULHA
  parafuso_gn25a_calc = chapa_teto_st_calc * 30 #Cálculo de parafuso gn25 para teto. 30 parafusos por placa.
  parafuso_gn25a_calc_condicao = (  # Condição de preço dos parafusos
      10.0 if parafuso_gn25a_calc < 100
      else 20.0 if parafuso_gn25a_calc < 200
      else 30.0 if parafuso_gn25a_calc < 300
      else 40.0 if parafuso_gn25a_calc < 400
      else 50.0 if parafuso_gn25a_calc < 500
      else 60.0 if parafuso_gn25a_calc < 1000
      else 70.0 if parafuso_gn25a_calc < 1100
      else 80.0 if parafuso_gn25a_calc < 1200
      else 90.0 if parafuso_gn25a_calc < 1300
      else 100.0 if parafuso_gn25a_calc < 1400
      else 110.0 if parafuso_gn25a_calc < 1500
      else 120.0 if parafuso_gn25a_calc < 2000
      else 130.0 if parafuso_gn25a_calc < 2100
      else 140.0 if parafuso_gn25a_calc < 2200
      else 150.0 if parafuso_gn25a_calc < 2300
      else 160.0 if parafuso_gn25a_calc < 2400
      else 170.0 if parafuso_gn25a_calc < 2500
      else 180.0 if parafuso_gn25a_calc < 3000
      else 190.0 if parafuso_gn25a_calc < 3100
      else 200.0 if parafuso_gn25a_calc < 3200
      else 210.0 if parafuso_gn25a_calc < 3300
      else 220.0 if parafuso_gn25a_calc < 3400
      else 230.0 if parafuso_gn25a_calc < 3500
      else 240.0 if parafuso_gn25a_calc < 4000
      else 250.0 if parafuso_gn25a_calc < 4100
      else 260.0 if parafuso_gn25a_calc < 4200
      else 270.0 if parafuso_gn25a_calc < 4300
      else 280.0 if parafuso_gn25a_calc < 4400
      else 290.0 if parafuso_gn25a_calc < 4500
      else 300.0 if parafuso_gn25a_calc < 5000
      else 310.0 if parafuso_gn25a_calc < 5100
      else 320.0 if parafuso_gn25a_calc < 5200
      else 330.0 if parafuso_gn25a_calc < 5300
      else 340.0 if parafuso_gn25a_calc < 5400
      else 350.0 if parafuso_gn25a_calc < 5500
      else 360.0 if parafuso_gn25a_calc < 6000
      else 370.0 if parafuso_gn25a_calc < 6100
      else 380.0 if parafuso_gn25a_calc < 6200
      else 390.0 if parafuso_gn25a_calc < 6300
      else 400.0 if parafuso_gn25a_calc < 6400
      else 410.0 if parafuso_gn25a_calc < 6500
      else 420.0 if parafuso_gn25a_calc < 7000
      else 430.0 if parafuso_gn25a_calc < 7100
      else 440.0 if parafuso_gn25a_calc < 7200
      else 450.0 if parafuso_gn25a_calc < 7300
      else 460.0 if parafuso_gn25a_calc < 7400
      else 470.0 if parafuso_gn25a_calc < 7500
      else 480.0 if parafuso_gn25a_calc < 8000
      else 490.0 if parafuso_gn25a_calc < 8100
      else 500.0 if parafuso_gn25a_calc < 8200
      else 510.0 if parafuso_gn25a_calc < 8300
      else 520.0 if parafuso_gn25a_calc < 8400
      else 530.0 if parafuso_gn25a_calc < 8500
      else 540.0 if parafuso_gn25a_calc < 9000
      else 550.0 if parafuso_gn25a_calc < 9100
      else 560.0 if parafuso_gn25a_calc < 9200
      else 570.0 if parafuso_gn25a_calc < 9300
      else 580.0 if parafuso_gn25a_calc < 9400
      else 590.0 if parafuso_gn25a_calc < 9500
      else 600.0 if parafuso_gn25a_calc < 10000
      else parafuso_gn25a_calc  # Valor padrão se for >= 10000
  )

  print(f"{parafuso_gn25a_calc} PARAFUSO GN 25 AGULHA = R${round(parafuso_gn25a_calc_condicao, 2)}")
  #___________________________________________________________________________________________

  #PARAFUSO METAL-METAL AGULHA PADRÃO (PEQUENO)
  parafuso_mma_calc = perfil_f530_calc * 2 #2 metal-metal por F-530
  parafuso_mma_calc_condicao = (
    10.0 if parafuso_mma_calc <= 100
    else 20.0 if parafuso_mma_calc <= 200
    else 30.0 if parafuso_mma_calc <= 300
    else 40.0 if parafuso_mma_calc <= 400
    else 50.0 if parafuso_mma_calc <= 500
    else 60.0 if parafuso_mma_calc <= 1000
    else 70.0 if parafuso_mma_calc <= 1100
    else 80.0 if parafuso_mma_calc <= 1200
    else 90.0 if parafuso_mma_calc <= 1300
    else 100.0 if parafuso_mma_calc <= 1400
    else 110.0 if parafuso_mma_calc <= 1500
    else 120.0 if parafuso_mma_calc <= 2000
    else 130.0 if parafuso_mma_calc <= 2100
    else 140.0 if parafuso_mma_calc <= 2200
    else 150.0 if parafuso_mma_calc <= 2300
    else 160.0 if parafuso_mma_calc <= 2400
    else 170.0 if parafuso_mma_calc <= 2500
    else 180.0 if parafuso_mma_calc <= 3000
    else parafuso_mma_calc  # Valor padrão se for >= 3000
)
  print(f"{math.ceil(parafuso_mma_calc)} PARAFUSO METAL METAL AGULHA PEQUENO = R${round(parafuso_mma_calc_condicao)}")
  #___________________________________________________________________________________________

  #PREGO
  prego_calc = cantoneira_padrao_calc * 5 #1 prego a cada 60cm.
  prego_calc_condicao = (
      10.0 if prego_calc <= 100
      else 20.0 if prego_calc <= 200
      else 30.0 if prego_calc <= 300
      else 40.0 if prego_calc <= 400
      else 50.0 if prego_calc <= 500
      else 60.0 if prego_calc <= 1000
      else 70.0 if prego_calc <= 1100
      else 80.0 if prego_calc <= 1200
      else 90.0 if prego_calc <= 1300
      else 100.0 if prego_calc <= 1400
      else 110.0 if prego_calc <= 1500
      else 120.0 if prego_calc <= 2000
      else 130.0 if prego_calc <= 2100
      else 140.0 if prego_calc <= 2200
      else 150.0 if prego_calc <= 2300
      else 160.0 if prego_calc <= 2400
      else 170.0 if prego_calc <= 2500
      else 180.0 if prego_calc <= 3000
      else prego_calc  # Valor padrão se for >= 3000
  )
  print(f"{prego_calc} PREGOS DE AÇO = R${round(prego_calc_condicao)}")
  #___________________________________________________________________________________________

  #FITA TELADA
  fita_telada_teto_calc = area * 1.5 # 1,5m por m²
  fita_telada_calc_condicao = (
    preco_fitatelada_p if fita_telada_teto_calc <= 45
    else preco_fitatelada_g if fita_telada_teto_calc <= 90
    else preco_fitatelada_p + preco_fitatelada_g if fita_telada_teto_calc <= 45 + 90
    else preco_fitatelada_g * 2 if fita_telada_teto_calc <= 90 * 2
    else preco_fitatelada_p + preco_fitatelada_g * 2 if fita_telada_teto_calc <= 45 + 90 * 2
    else preco_fitatelada_g * 3 if fita_telada_teto_calc <= 90 * 3
    else preco_fitatelada_p + preco_fitatelada_g * 3 if fita_telada_teto_calc <= 45 + 90 * 3
    else preco_fitatelada_g * 4 if fita_telada_teto_calc <= 90 * 4
    else preco_fitatelada_p + preco_fitatelada_g * 4 if fita_telada_teto_calc <= 45 + 90 * 4
    else preco_fitatelada_g * 5
  )
  print(f"{math.ceil(fita_telada_teto_calc)} METROS DE FITA TELADA = R${round(fita_telada_calc_condicao, 2)}")
  #___________________________________________________________________________________________

  #MASSA DE REJUNTE
  massa_de_rejunte_calc = 0.35 * area # 0,350 gramas por metro quadrado
  massa_de_rejunte_calc_condicao = (
    preco_massa5kg if massa_de_rejunte_calc <= 5 # 1 massa de 5kg se menor ou igual a 5
    else preco_massa15kg if massa_de_rejunte_calc <= 15 # 1 massa de 15 kg se > 5 ou <= 15
    else preco_massa25kg if massa_de_rejunte_calc <= 25 # 1 massa de 25 kg se >15 ou <= 25
    else preco_massa25kg + preco_massa5kg if massa_de_rejunte_calc <= 30 # 1 massa de 25 kg e 1 massa de 5 kg se > 25 ou <= 30
    else preco_massa25kg + preco_massa15kg if massa_de_rejunte_calc <= 40 # 1 massa de 25 kg e 1 massa de 15 kg se > 30 ou <= 40
    else preco_massa25kg * 2 if massa_de_rejunte_calc <= 50 # 2 massas de 25 kg se > 40 ou <= 50
    else preco_massa25kg * 2 + preco_massa5kg if massa_de_rejunte_calc <= 55 # 2 massas de 25 kg e 1 de 5 kg se > 50 ou <= 55
    else preco_massa25kg * 2 + preco_massa15kg if massa_de_rejunte_calc <= 65 #2 massas de 25 kg e 1 de 15kg se > 55 ou <= 65
    else preco_massa25kg * 3 if massa_de_rejunte_calc <= 75 # 3 massas de 25 kg se > 65 ou <= 75
    else preco_massa25kg * 4 #demais opções a ajudat se necessário.
  )
  print(f"{round(massa_de_rejunte_calc, 2)}KG DE MASSA DE REJUNTE = R${round(massa_de_rejunte_calc_condicao, 2)}")
  #___________________________________________________________________________________________

  print() #pulando uma linha
  #___________________________________________________________________________________________

  #TOTAL DO ORÇAMENTO:
  total_orcamento_teto = preco_total_chapa_teto + preco_total_cantoneira_padrao + preco_total_perfilf530 + preco_total_tirante + preco_total_suporte_regulador + prego_calc_condicao + massa_de_rejunte_calc_condicao + fita_telada_calc_condicao + parafuso_gn25a_calc_condicao + parafuso_mma_calc_condicao
  print(f"TOTAL ORÇAMENTO PARA TETO DRYWALL {round(area, 2)} m² = R${round(total_orcamento_teto, 2)}")

  
  


#BASE DE CÁLCULO DE MATERIAL PARA PAREDE DRYWALL

def medida_parede():
  #CHAPA
  chapa_parede_st_calc = math.ceil(area) #Cálculo de chapa para parede. Chapa é igual à área arredondada pra cima.
  preco_total_chapa_parede = chapa_parede_st_calc * preco_chapa_st
  print(f"{chapa_parede_st_calc} CHAPA ACARTONADO ST = R${round(preco_total_chapa_parede, 2)} ")
  #___________________________________________________________________________________________
  
  #GUIA
  guia_48_calc = math.ceil((medida_1 + medida_2) * 2 / 3) #Cálculo de guia para parede. (m1 + m2) * 2 / 3 arredondando pra cima
  preco_total_guia48 = guia_48_calc * preco_guia48
  print(f"{guia_48_calc} GUIAS = R${round(preco_total_guia48, 2)} ")
  #___________________________________________________________________________________________

  #MONTANTE
  montante_48_calc = math.ceil(area / 1.8) #Cálculo de montante para parede
  preco_total_montante48 = montante_48_calc * preco_montante48
  print(f"{montante_48_calc} MONTANTES = R${round(preco_total_montante48, 2)} ")
  #___________________________________________________________________________________________
  #PARAFUSO GN 25 AGULHA
  parafuso_gn25a_calc = chapa_parede_st_calc * 30 #Cálculo de parafuso gn25 para parede
  parafuso_gn25a_calc_condicao = (  # Condição de preço dos parafusos
      10.0 if parafuso_gn25a_calc <= 100
      else 20.0 if parafuso_gn25a_calc <= 200
      else 30.0 if parafuso_gn25a_calc <= 300
      else 40.0 if parafuso_gn25a_calc <= 400
      else 50.0 if parafuso_gn25a_calc <= 500
      else 60.0 if parafuso_gn25a_calc <= 1000
      else 70.0 if parafuso_gn25a_calc <= 1100
      else 80.0 if parafuso_gn25a_calc <= 1200
      else 90.0 if parafuso_gn25a_calc <= 1300
      else 100.0 if parafuso_gn25a_calc <= 1400
      else 110.0 if parafuso_gn25a_calc <= 1500
      else 120.0 if parafuso_gn25a_calc <= 2000
      else 130.0 if parafuso_gn25a_calc <= 2100
      else 140.0 if parafuso_gn25a_calc <= 2200
      else 150.0 if parafuso_gn25a_calc <= 2300
      else 160.0 if parafuso_gn25a_calc <= 2400
      else 170.0 if parafuso_gn25a_calc <= 2500
      else 180.0 if parafuso_gn25a_calc <= 3000
      else 190.0 if parafuso_gn25a_calc <= 3100
      else 200.0 if parafuso_gn25a_calc <= 3200
      else 210.0 if parafuso_gn25a_calc <= 3300
      else 220.0 if parafuso_gn25a_calc <= 3400
      else 230.0 if parafuso_gn25a_calc <= 3500
      else 240.0 if parafuso_gn25a_calc <= 4000
      else 250.0 if parafuso_gn25a_calc <= 4100
      else 260.0 if parafuso_gn25a_calc <= 4200
      else 270.0 if parafuso_gn25a_calc <= 4300
      else 280.0 if parafuso_gn25a_calc <= 4400
      else 290.0 if parafuso_gn25a_calc <= 4500
      else 300.0 if parafuso_gn25a_calc <= 5000
      else 310.0 if parafuso_gn25a_calc <= 5100
      else 320.0 if parafuso_gn25a_calc <= 5200
      else 330.0 if parafuso_gn25a_calc <= 5300
      else 340.0 if parafuso_gn25a_calc <= 5400
      else 350.0 if parafuso_gn25a_calc <= 5500
      else 360.0 if parafuso_gn25a_calc <= 6000
      else 370.0 if parafuso_gn25a_calc <= 6100
      else 380.0 if parafuso_gn25a_calc <= 6200
      else 390.0 if parafuso_gn25a_calc <= 6300
      else 400.0 if parafuso_gn25a_calc <= 6400
      else 410.0 if parafuso_gn25a_calc <= 6500
      else 420.0 if parafuso_gn25a_calc <= 7000
      else 430.0 if parafuso_gn25a_calc <= 7100
      else 440.0 if parafuso_gn25a_calc <= 7200
      else 450.0 if parafuso_gn25a_calc <= 7300
      else 460.0 if parafuso_gn25a_calc <= 7400
      else 470.0 if parafuso_gn25a_calc <= 7500
      else 480.0 if parafuso_gn25a_calc <= 8000
      else 490.0 if parafuso_gn25a_calc <= 8100
      else 500.0 if parafuso_gn25a_calc <= 8200
      else 510.0 if parafuso_gn25a_calc <= 8300
      else 520.0 if parafuso_gn25a_calc <= 8400
      else 530.0 if parafuso_gn25a_calc <= 8500
      else 540.0 if parafuso_gn25a_calc <= 9000
      else 550.0 if parafuso_gn25a_calc <= 9100
      else 560.0 if parafuso_gn25a_calc <= 9200
      else 570.0 if parafuso_gn25a_calc <= 9300
      else 580.0 if parafuso_gn25a_calc <= 9400
      else 590.0 if parafuso_gn25a_calc <= 9500
      else 600.0 if parafuso_gn25a_calc <= 10000
      else parafuso_gn25a_calc  # Valor padrão se for >= 10000
  )
  print(f"{parafuso_gn25a_calc} PARAFUSOS GN 25 AGULHA = R${round(parafuso_gn25a_calc_condicao, 2)}")
  #___________________________________________________________________________________________

  #PARAFUSO METAL-METAL AGULHA PEQUENO (PADRÃO)
  parafuso_mma_calc = montante_48_calc * 4
  parafuso_mma_calc_condicao = (
      10.0 if parafuso_mma_calc <= 100
      else 20.0 if parafuso_mma_calc <= 200
      else 30.0 if parafuso_mma_calc <= 300
      else 40.0 if parafuso_mma_calc <= 400
      else 50.0 if parafuso_mma_calc <= 500
      else 60.0 if parafuso_mma_calc <= 1000
      else 70.0 if parafuso_mma_calc <= 1100
      else 80.0 if parafuso_mma_calc <= 1200
      else 90.0 if parafuso_mma_calc <= 1300
      else 100.0 if parafuso_mma_calc <= 1400
      else 110.0 if parafuso_mma_calc <= 1500
      else 120.0 if parafuso_mma_calc <= 2000
      else 130.0 if parafuso_mma_calc <= 2100
      else 140.0 if parafuso_mma_calc <= 2200
      else 150.0 if parafuso_mma_calc <= 2300
      else 160.0 if parafuso_mma_calc <= 2400
      else 170.0 if parafuso_mma_calc <= 2500
      else 180.0 if parafuso_mma_calc <= 3000
      else parafuso_mma_calc  # Valor padrão se for >= 3000
  )
  print(f"{parafuso_mma_calc} PARAFUSO METAL METAL AGULHA PEQUENO = R${round(parafuso_mma_calc_condicao, 2)}")
  #___________________________________________________________________________________________

  #FITA TELADA
  fita_telada_calc = math.ceil(area) * 3 # 3 metros por m²
  fita_telada_calc_condicao = (
      preco_fitatelada_p if fita_telada_calc <= 45
      else preco_fitatelada_g if fita_telada_calc <= 90
      else preco_fitatelada_p + preco_fitatelada_g if fita_telada_calc <= 45 + 90
      else preco_fitatelada_g * 2 if fita_telada_calc <= 90 * 2
      else preco_fitatelada_p + preco_fitatelada_g * 2 if fita_telada_calc <= 45 + 90 * 2
      else preco_fitatelada_g * 3 if fita_telada_calc <= 90 * 3
      else preco_fitatelada_p + preco_fitatelada_g * 3 if fita_telada_calc <= 45 + 90 * 3
      else preco_fitatelada_g * 4 if fita_telada_calc <= 90 * 4
      else preco_fitatelada_p + preco_fitatelada_g * 4 if fita_telada_calc <= 45 + 90 * 4
      else preco_fitatelada_g * 5
  )
  print(f"{fita_telada_calc} METROS DE FITA TELADA = R${round(fita_telada_calc_condicao, 2)}")
  #___________________________________________________________________________________________

  #MASSA DE REJUNTE
  massa_de_rejunte_calc = 0.7 * math.ceil(area) # 0,700 gramas por metro quadrado
  massa_de_rejunte_calc_condicao = (
      preco_massa5kg if massa_de_rejunte_calc <= 5 # 1 massa de 5kg se menor ou igual a 5
      else preco_massa15kg if massa_de_rejunte_calc <= 15 # 1 massa de 15 kg se > 5 ou <= 15
      else preco_massa25kg if massa_de_rejunte_calc <= 25 # 1 massa de 25 kg se >15 ou <= 25
      else preco_massa25kg + preco_massa5kg if massa_de_rejunte_calc <= 30 # 1 massa de 25 kg e 1 massa de 5 kg se > 25 ou <= 30
      else preco_massa25kg + preco_massa15kg if massa_de_rejunte_calc <= 40 # 1 massa de 25 kg e 1 massa de 15 kg se > 30 ou <= 40
      else preco_massa25kg * 2 if massa_de_rejunte_calc <= 50 # 2 massas de 25 kg se > 40 ou <= 50
      else preco_massa25kg * 2 + preco_massa5kg if massa_de_rejunte_calc <= 55 # 2 massas de 25 kg e 1 de 5 kg se > 50 ou <= 55
      else preco_massa25kg * 2 + preco_massa15kg if massa_de_rejunte_calc <= 65 #2 massas de 25 kg e 1 de 15kg se > 55 ou <= 65
      else preco_massa25kg * 3 if massa_de_rejunte_calc <= 75 # 3 massas de 25 kg se > 65 ou <= 75
      else preco_massa25kg * 4 #demais opções a ajudat se necessário.
  )
  print(f"{round(massa_de_rejunte_calc, 2)} KG DE MASSA DE REJUNTE = R${round(massa_de_rejunte_calc_condicao, 2)}")
  #___________________________________________________________________________________________

  #PULANDO UMA LINHA
  print()
  #___________________________________________________________________________________________

  #TOTAL DO ORÇAMENTO:
  total_orcamento_parede = preco_total_chapa_parede + preco_total_guia48 + preco_total_montante48 + parafuso_gn25a_calc_condicao + parafuso_mma_calc_condicao + fita_telada_calc_condicao + massa_de_rejunte_calc_condicao
  print(f"TOTAL ORÇAMENTO PAREDE DRYWALL {round(area, 2)} m² = R${round(total_orcamento_parede, 2)}")



#ESCOLHA DE ORÇAMENTO PARA TETO OU PAREDE

while True:

  alternativa = input("Digite 1 para TETO ou 2 para PAREDE: ")

  if alternativa == '1':
    print(f"ORÇAMENTO PARA TETO DRYWALL: {medida_1} x {medida_2} = {round(area, 2)} m²")
    medida_teto()
    break

  elif alternativa == '2':
    print(f"ORÇAMENTO PARA PAREDE DRYWALL: {medida_1} x {medida_2} = {round(area, 2)} m²")
    medida_parede()
    break

  else:
    print("TENTE NOVAMENTE")



