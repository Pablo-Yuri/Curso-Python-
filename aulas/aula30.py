"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

# range_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) # se >= 99 e <= 101
# vel_permitida_radar_1 = velocidade > RADAR_1

# print(range_radar_1, vel_permitida_radar_1)

# if range_radar_1 and vel_permitida_radar_1: 
#         print(f"Multado, {velocidade=}")


range_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) # se >= 99 e <= 101

if range_radar_1: # se >= 99 e <= 101
    if velocidade > RADAR_1:
        print(f"Multado, {velocidade=}")
    else:
        print("Abaixo da velociadade permitida")
else:
    print('O carro está fora do alcance do radar')