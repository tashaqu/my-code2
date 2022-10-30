per_cent={
    "ТКБ":5.6,
    "СКБ":5.9,
    "ВТБ":4.28,
    "СБЕР":4.0
}
money=10000
deposit=[x*money for x in per_cent.values() ]
print(deposit)
deposit_max=max(deposit)
print("Максимальная сумма которую вы можете заработать-",deposit_max )