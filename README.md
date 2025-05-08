# Você Político

**Você Político** é um aplicativo Android que visa conscientizar os eleitores sobre seus valores políticos e promover o engajamento na política. O projeto adapta o teste internacional **8Values** para o cenário político brasileiro, ajudando os usuários a entenderem seu posicionamento político por meio de questões divididas em quatro eixos principais.

## Objetivo

O objetivo do aplicativo é fornecer uma ferramenta para o público brasileiro refletir sobre seus valores políticos e entender seu papel no cenário político, promovendo maior engajamento e esclarecimento sobre o processo eleitoral.

## Funcionalidades

- **Teste de Valores Políticos**: Os usuários respondem a questões baseadas no **8Values**, medindo seu posicionamento em 4 eixos: Econômico, Diplomático, Civil e Social.
- **Perfil Político**: Ao final, o aplicativo gera um perfil ideológico do usuário com base nas respostas.
- **Escala de Respostas**: As respostas seguem uma escala do tipo Likert: Discordo Totalmente, Discordo, Imparcial, Concordo e Concordo Totalmente.
- **Feedback Visual**: O resultado é apresentado de forma gráfica para ajudar o usuário a compreender seu posicionamento ideológico.

## Tecnologias Utilizadas

- **Android Studio**: Ambiente de desenvolvimento para a criação do protótipo Android.
- **Java/Kotlin**: Linguagens utilizadas no desenvolvimento.
- **Firebase**: Para armazenamento de dados de usuários e resultados.



## Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/leonardo-spy/voce-politico.git
   ```

2. **Abra no Android Studio**:
   Abra o Android Studio e carregue o projeto.

3. **Execute no seu dispositivo Android**:
   Conecte seu dispositivo ou use um emulador para rodar o app.

## Screenshots

![0](https://github.com/user-attachments/assets/f0c598b2-9c61-4621-8128-d0f485b1107e)
![1](https://github.com/user-attachments/assets/8977fc20-f90f-4b70-8849-5b3f9809bc21)
![2](https://github.com/user-attachments/assets/5ed074d7-2999-4d23-9e02-056182510353)
![3](https://github.com/user-attachments/assets/1bda14ed-6968-4ee3-9797-c77b18c67b0c)
![4](https://github.com/user-attachments/assets/46b6059e-2426-4db4-834d-2989ff94e3c8)
![5](https://github.com/user-attachments/assets/077ad05e-859c-479d-bb67-4f1f2fed8517)

## Demonstração

- [Demonstração do Projeto no YouTube](https://www.youtube.com/watch?v=LIO82mgYVqI)

## Links

- [Link para o Teste de 8Values](https://8values.github.io/)

## Conversão de Dados JSON para Seeder

O projeto inclui um script Python para converter dados de arquivos JSON, contendo as questões políticas e seus respectivos efeitos, para um formato de **Seeder** no Laravel. Isso facilita a inserção de dados no banco de dados do Laravel.

### Como Usar

1. **Execute o script** `main.py` para gerar o código do Seeder.
2. **Copie o código gerado** para o Seeder do Laravel e execute a migração para popular a tabela com as questões.

## Contribuições

Contribuições são bem-vindas! Se você deseja ajudar, pode abrir uma issue ou enviar um pull request.

## Autores
Leonardo Marques dos Santos<br/>
Danilo Faria Dutra

## Integração com o Seeder do Laravel (Opcional)

O projeto **Você Político** também conta com uma [API](https://github.com/leonardo-spy/voce-politico-api) que facilita a conversão de dados JSON para o banco de dados do Laravel. Esse processo é realizado através de um Seeder, utilizando o script **main.py** localizado no diretório `converter json to database Seeder`. O script lê arquivos JSON contendo dados de questões e efeitos, e insere esses dados diretamente no modelo do Laravel `App\Models\Questoes`.

### Fluxo de Dados

1. **Leitura dos arquivos JSON**: Os arquivos `questions.json` e `effect.json` são lidos e processados para garantir a formatação adequada.
2. **Inserção no banco de dados**: O script gera instruções SQL para inserir os dados no banco de dados, utilizando o modelo Laravel para a tabela `Questoes`.

Essa funcionalidade facilita a integração dos dados no banco e é um componente chave para a alimentação do banco de dados com as questões e efeitos usados pelo teste de valores políticos.