from fpdf import FPDF

# Coleta de dados do usuário
projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o prazo estimado: ")
valor_hora = input("Digite o valor da hora: ")
prazo = input("Digite o prazo: ")

# Cálculo do valor total
try:
    valor_total = int(horas_estimadas) * int(valor_hora)
except ValueError:
    print("Por favor, insira valores numéricos válidos para horas estimadas e valor da hora.")
    exit()

# Formatação do valor total
valor_total_formatado = "{:,.2f}".format(valor_total).replace(',', 'X').replace('.', ',').replace('X', '.')

# Criação do PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

# Adiciona imagem ao PDF
pdf.image("template.png", x=0, y=0)

# Adiciona texto ao PDF
pdf.text(115, 145, projeto)
pdf.text(115, 160, str(horas_estimadas))
pdf.text(115, 175, str(valor_hora))
pdf.text(115, 190, prazo)
pdf.text(115, 205, valor_total_formatado)

# Salva o PDF
pdf.output("orcamento.pdf")

print("Orçamento gerado com sucesso")
