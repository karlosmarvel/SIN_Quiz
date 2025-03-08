import pandas as pd
import random
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class SinChat_Quiz:
    def __init__(self, request, excel_file='Prompts.xlsx', Rotina_Operacional="Programação de Intervenções"):
        try:
            self.excel_file = excel_file
            self.Prompts = pd.read_excel(excel_file)
            self.perguntas = self.Prompts.to_dict(orient='records')
        except FileNotFoundError:
            print(f"Arquivo '{self.excel_file}' não encontrado.")
            self.perguntas = []
        except Exception as e:
            print(f"Erro ao carregar o arquivo Excel: {e}")
            self.perguntas = []

        self.Rotina_Operacional = Rotina_Operacional

        api_key = os.getenv('GOOGLE_API_KEY')
        
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('models/gemini-2.0-flash-001')
        else:
            print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")
            self.model = None

        if self.model:
            self.Desc_Question = self.Extrator_Questao()
            request.session['Pergunta'] = self.Desc_Question[0]
            request.session['Alternativa_A'] = self.Desc_Question[1]
            request.session['Alternativa_B'] = self.Desc_Question[2]
            request.session['Alternativa_C'] = self.Desc_Question[3]
            request.session['Alternativa_D'] = self.Desc_Question[4]
            request.session['Resposta'] = self.Desc_Question[5]
        else:
            print ("Erro: Modelo Gemini não inicializado.")

    def Sortear_Item(self):
        try:
            qntd_Itens_da_Secao = (self.Prompts['Rotina_Operacional'] == 'Programação de Intervenções').sum()
            Id_Prompt_Sorteado = random.randint(0, qntd_Itens_da_Secao - 1)
            Prompt_Sorteado = self.Prompts['Prompts'][Id_Prompt_Sorteado]
            return Prompt_Sorteado
        except KeyError as e:
            print(f"Erro: Coluna '{e}' não encontrada no DataFrame.")
            return None
        except IndexError:
            print("Erro: Id_Prompt_Sorteado fora do intervalo.")
            return None

    def Gerador_Questao(self):
        if self.model is None:
            return "Erro: Modelo Gemini não inicializado. Verifique a configuração da chave de API."

        Conhecimento = self.Sortear_Item()
        Comando = "Elabore uma pergunta objetiva com 4 alternativas: A, B, C e D. Responda com a resposta correta em seguida sobre o assunto em questão. Na questão, contextualize os assuntos citados. Todas as perguntas precisam ter relação com o ONS e sua atuação. Configuração da resposta: Na primeira linha imprima a pergunta, na segunda linha a alternativa A, na segunda linha a alternativa B, na terceira linha a alternativa C, na quarta linha a alternativa D e na quinta linha apenas a alternativa correta. Na quinta linha somente a alternativa, sem a descrição da alternativa. Insira apenas essas quebras de linha"
        Resposta = self.model.generate_content([Comando, Conhecimento])
        return Resposta.text

    def Extrator_Questao(self):
        if self.model is None:
            return ["Erro: Modelo Gemini não inicializado. Verifique a configuração da chave de API."]
        Pergunta = self.Gerador_Questao()
        linhas = Pergunta.split('\n')
        Pergunta = [linha for linha in linhas if linha.strip()]
        return Pergunta