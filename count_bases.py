import os
from Bio import SeqIO

def calcular_total_bases(diretorio):
    total_bases = 0
    
    # Iterar sobre todos os arquivos no diretório
    for filename in os.listdir(diretorio):
        if filename.endswith(".fasta") or filename.endswith(".fa"):
            filepath = os.path.join(diretorio, filename)
            # Ler o arquivo FASTA
            for record in SeqIO.parse(filepath, "fasta"):
                total_bases += len(record.seq)
    
    return total_bases

def converter_bases(total_bases):
    megabases = total_bases / 1e6
    gigabases = total_bases / 1e9
    return megabases, gigabases

# Caminho para o diretório contendo os arquivos FASTA
diretorio = r"C:\Users\Galileu\Desktop\mtDNA-novoplasty"

# Calcular o total de bases
total_bases = calcular_total_bases(diretorio)

# Converter o total de bases em megabases e gigabases
megabases, gigabases = converter_bases(total_bases)

# Exibir os resultados
print(f"Total de bases: {total_bases}")
print(f"Total de megabases (Mb): {megabases:.2f}")
print(f"Total de gigabases (Gb): {gigabases:.2f}")
