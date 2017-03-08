import DBGeneration
import Prediction

security, botnet, size = 10, 25, 100
attacks = Prediction.predict_attack(security, botnet, size, Prediction.get_model())
print attacks, int(Prediction.get_payment(size, attacks, 0.1))

security, botnet, size = 10, 25, 500
attacks = Prediction.predict_attack(security, botnet, size, Prediction.get_model())
print attacks, int(Prediction.get_payment(size, attacks, 0.1))

security, botnet, size = 25, 25, 10000
attacks = Prediction.predict_attack(security, botnet, size, Prediction.get_model())
print attacks, int(Prediction.get_payment(size, attacks, 0.1))