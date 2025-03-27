data_nasce = input("digite sua data de nascimento: (dd/mm/yy)" )
nascimento = datetime.strptime(data_nasce, "%d/%m/%y")
hoje = datetime.today()
idade = hoje.year - nascimento.year

