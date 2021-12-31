from random import choice
import discord
import pandas as pd

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        # Gera tabelas individuais ou do grupo como todo

        names = ['DARIUS', 'ELANA', 'JO', 'THE MEN', 'WALKER']
        health = [78, 70, 70, 78, 90]
        stress = [2, 2, 4, 2, 3]
        strenght = [39, 35, 35, 39, 45]
        speed = [32, 39, 36, 43, 36]
        intellect = [33, 42, 24, 37, 20]
        combat = [40, 21, 28, 37, 40]
        sanity = [25, 40, 30, 20, 25]
        fear = [30, 25, 35, 85, 30]
        body = [35, 25, 30, 40, 35]
        armor = [40, 25, 35, 25, 40]

        mothership = {'Nome': names, 'Saúde': health, 'Estresse': stress,
                      'Força': strenght, 'Velocidade': speed, 'Intelecto': intellect, 'Combate': combat,
                      'Sanidade': sanity, 'Medo': fear, 'Corpo': body, 'Armadura': armor}

        resume = pd.DataFrame(mothership)

        resume.index = ['Marine', 'Scientist', 'Teamster', 'Android', 'Marine']

        # char = discord.Embed(title=f'{message.author.nick}', color = discord.Color.random())
        # char.add_field(name='Você selecionou:', value=f'```{resume.iloc[[0]]}```')
        # char.set_footer(text='Mais informações, acessar: surubaorpgistico.ml')


        if message.content == '?darius':
            await message.channel.send(f'```{resume.iloc[[0]]}```')

        if message.content == '?elana':
            await message.channel.send(f'```{resume.iloc[[1]]}```')

        if message.content == '?jo':
            await message.channel.send(f'```{resume.iloc[[2]]}```')

        if message.content == '?themen':
            await message.channel.send(f'```{resume.iloc[[3]]}```')

        if message.content == '?walker':
            await message.channel.send(f'```{resume.iloc[[4]]}```')

        if message.content == '?m':
            await message.channel.send(f'```{resume}```')

        
        # Randomiza um trabalho em conceito espacial

        job = ('**1)** Mineração de asteróides (minério, combustível não refinado, metal precioso).', 
        '**2)** Transporte de carga (mercadorias comerciais, minério, suprimentos).', 
        '**3)** Entrega de mensagens importantes.', 
        '**4)** Escolta de passageiros.', 
        '**5)** Sucatear naves espaciais abandonadas.',
        '**6)** Contrabandear mercadorias (importação ou exportação ilegal, drogas).', 
        '**7)** Invadir naves corporativas.', 
        '**8)** Mapear setores do espaço não cartografado.',
        '**9)** Caçar criminosos perigosos em busca de recompensa.', 
        '**10)** Coletar dados sobre espécies desconhecidas.')

        job_answer = discord.Embed(title=f'{message.author.nick}', color = discord.Color.random())
        job_answer.add_field(name='Você sorteou:', value=f'{choice(job)}')
        job_answer.set_footer(text="Mothership - Player's Survival Guide Pág. 08")

        if message.content == '?j':
            await message.channel.send(embed=job_answer)


        # Define as condições ao recuperar a consciência

        death = ('**1)** Você está em coma e com morte cerebral. Somente medidas extraordinárias o levarão de volta ao mundo desperto.',
        '**2)** Em 1d10 dias, com 1 Saúde. -5 Força, -5 Velocidade, -5 Intelecto (perda permanente). Desvantagem em todos os testes por 1d10 dias.+ 1d10 Estresse.', 
        '**3)** Em 1d10 dias, com 1 Saúde. -5 Força, -5 Velocidade, -5 Intelecto (perda permanente). Desvantagem em todos os testes por 1d10 dias.+ 1d10 Estresse.', 
        '**4)** Em 1d10 horas. 1 Saúde. -5 Força, e -5 Velocidade (perda permanente). Desvantagem em todas as rolagens por 1d10 horas. +3 Estresse.', 
        '**5)** Em 1d10 horas. 1 Saúde. -5 Força, e -5 Velocidade (perda permanente). Desvantagem em todas as rolagens por 1d10 horas. +3 Estresse.', 
        '**6)** Em 1d10 horas. 1 Saúde. -5 Força, e -5 Velocidade (perda permanente). Desvantagem em todas as rolagens por 1d10 horas. +3 Estresse.', 
        '**7)** Em 1d10 minutos. 1 Saúde. -5 Força (perda permanente). Desvantagem em todos os testes por 3d10 minutos. +2 Estresse.', 
        '**8)** Em 1d10 minutos. 1 Saúde. -5 Força (perda permanente). Desvantagem em todos os testes por 3d10 minutos. +2 Estresse.', 
        '**9)** Em 1d10 minutos. 1 Saúde. -5 Força (perda permanente). Desvantagem em todos os testes por 3d10 minutos. +2 Estresse.', 
        '**10)** Imediatamente. 1 Saúde. Desvantagem para todas rolagens por 1d10 minutos. +1 Estresse.')

        death_answer = discord.Embed(title=f'{message.author.name}, você recupera a consciência...', description=f'{choice(death)}', color = discord.Color.random())

        if message.content == '?d':
            await message.channel.send(embed=death_answer)
        

        # Randomiza uma Bugiganga durante a criação do personagem

        trinket = ('**00) Aberração Insetóide Preservada.**', '**01) Ficha de Pôquer Verde Desbotada.**', 
        '**02) Roteiro de Empresa Antiga (Mineração de Asteróide).**', '**03) Boneca de Pele Dessecada.**', '**04) Flor Alienígena Prensada (Comum).**', 
        '**05) Colar de Invólucros de Conchas.**', '**06) Núcleo Lógico Andróide, Corroído.**', '**07) Panfleto: *Sinais de Infecção Parasitária*.**', 
        '**08) Manual: *Trate Seu Rifle Como Uma Dama*.**', '**09) Faca de Osso.**', '**10) Calendário: *Arte Alienígena Pin-Up*.**', 
        '**11) Plaqueta de Identificação Militar (Herança).**', '**12) Dançarina Serpentiforme Holográfica.**', '**13) Uísque de Serpente.**', 
        '**14) Recipiente Médico, Pó Roxo.**', '**15) Comprimidos: Realce Masculino, Qualidade Inferior.**', '**16) Baralho de Cassino.**', '**17) Pé de Coelho.**', 
        '**18) Anel de Pedra da Lua.**', '**19) Manual: *Segurança em Mineração e Você*.**', '**20) Panfleto: *Contra Simulacro Humanos*.**',
        '**21) Crânio de Animal, 3 Olhos, Chifres Enrolados.**', '**22) Certificação de Bartender (Expirada).**', '**23) Chave Inglesa.**', 
        '**24) Caneca de Prospecção, Amassada.**', '**25) Máscara Estranha.**', '**26) Marmóreo Vantablack.**', '**27) Dados de Marfim.**', 
        '**28) Cartas de Tarô, Usadas, com Bordas de Pirita Dourada.**', '**29) Saco de Dentes Sortidos.**', '**30) Cinzas (de um Parente).**', 
        '**31) Colar ONR (Ordens de Não Reanimação).**', '**32) Cigarros (Crânio Sorridente).**', '**33) Comprimidos: Noz de Areca.**', 
        '**34) Solicitação Rejeitada (Nave de Colonização).**', '**35) Panfleto: *Andróides Soberanos*.**', '**36) Catecismos (Sedicioso): *O Capitão, Ordenado*.**', 
        '**37) Chave (Lar da Infância).**', '**38) Manual: *Pânico: Precursor da Catástrofe*.**', '**39) Bóton: *“Seu Moral Está Melhorando?”***', 
        '**40) Bastões Fluorescentes, Néon.**', '**41) Panfleto: *As Estrelas Indiferentes*.**', '**42) Calendário: *Batalhas Militares*.**', 
        '**43) Manual: *Capitão Rico, Capitão Pobre*.**', '**44) Cartaz da Campanha (Planeta Natal).**', '**45) Pingente: Fragmentos de Casca Suspensos em Plástico.**', 
        '**46) Palito de Dentes de Titânio.**', '**47) Luvas, Couro (Couro de Xenomorfo).**', '**48) Panfleto: *O Zen e a Arte da Organização de Carga*.**', 
        '**49) Pornografia Ilustrada, Amassada, Bem Manuseada.**', '**50) Soco Inglês.**', '**51) Algemas Felpudas.**', '**52) Diário do Ódio.**', 
        '**53) Cigarreira Estilizada.**', '**54) Esfera de Fios de Bitolas Variadas.**', '**55) Chave de Parafusos.**', '**56) Canivete Suíço.**', 
        '**57) Chifre de Xenomorfo em Pó.**', '**58) Árvore Bonsai.**', '**59) Taco de Golfe.**', '**60) Trilobita Fossilizado.**', 
        '**61) Panfleto: *Uma Garota Em Cada Porto*.**', '**62) Macacões Remendados, Personalizados.**', '**63) Coisa Carnuda Selada em um Jarro Lúgubre.**', 
        '**64) Bracelete de Cravos.**', '**65) Gaita de Boca.**', '**66) Manual: *Almanaque do Viajante Espacial* (Desatualizado).**', 
        '**67) Fotografia Desbotada, Uma Charneca Varrida Pelo Vento.**', '**68) Bola Anti-Estresse, lê-se: *"Estresse Zero em Gravidade Zero"*.**', 
        '**69) Manual: *Luar Cintilante com óleo lubrificante e combustível*.**', '**70) Giroscópio, Curvado, em Flandre.**', 
        '**71) Xícara de Café, Lascada, *FELICIDADE É OBRIGATÓRIA*.**', '**72) Dardos Magnéticos.**', '**73) Tinta Aerosol.**', 
        '**74) Cartaz de Procurado, Envelhecido.**', '**75) Medalhão, Trança de Cabelo.**', '**76) Picareta, Miniatura.**', '**77) Cobertor, Retardante de Fogo.**', 
        '**78) Parka com Capuz, Forrada de Lã.**', '**79) Arma de Chumbinho.**', '**80) Machadinha de Pedra.**', 
        '**81) Pingente: Dois Astronautas formando uma Caveira.**', '**82) Cubo Mágico.**', '**83 Manual: *Sobrevivência: Tome Sopa Com Uma Faca*.**', 
        '**84) Broche do Sputnik.**', '**85) Ushanka (Gorro Russo).**', '**86) Boné de Caminhoneiro, Malha, Logotipo com Alienígena Grey.**', 
        '**87) Bálsamo Mentolado.**', '**88) Capacete de Medula.**', '**89) Lona 3m².**', '**90) *I Ching*, Faltam Palitos.**', '**91) Kukri (Faca do Nepal).**',
        '**92) Pá de Trincheira.**', '**93) Canivete, Faca de Manteiga Afiada.**', '**94) Gato Taxidermizado.**', '**95) Panfleto: *Interpretando Sonhos com Ovelhas*.**', 
        '**96) Óculos de Tiro, Cartuchos Gastos de Espingarda.**', '**97) Óculos de Ópera.**', '**98) Panfleto: *A Relíquia da Carne*.**', 
        '**99) Kit de Xadrez Miniatura, Feito em Ossos, Peças Faltando.**')

        if message.content == '?t':
            await message.channel.send(f'{message.author.name}, você sorteou: {choice(trinket)}')


        # Randomiza um Retalho durante a criação do personagem

        patch = ('**00) *“Funcionário do Mês”***', '**01) *"Segurança"***', '**02) Tipo Sanguíneo**', '**03) Logotipo de Camisa Vermelha (Star Trek)**', 
        '**04) *“Não Corra, Você Só Morrerá Cansado”*, Remendo para Costas**', '**05) Cartas de Pôquer: Mão do Homem Morto**', '**06) Símbolo de Perigo Biológico**', 
        '**07) Sr. Yuck (Símbolo)**', '**08) Símbolo Nuclear**', '**09) *“Coma os Ricos”***', '**10) *“Tenha Certeza: Toque Duas Vezes”***', '**11) Emoji de Fogo**', 
        '**12) Smiley (Brilha no Escuro)**', '**13) *“Sorria, Você Está Sendo Filmado!”***', '**14) Bandeira Pirata**', '**15) Crânio Viking**', 
        '**16) *“PREDADOR ALFA”* (Crânio de Esmilodonte)**', '**17) Pin-Up (Ás de Espadas)**', '**18) Rainha de Copas**', '**19) Pin-Up (Mecânico)**', 
        '**20) *"A Cobra Vai Fumar!"***', '**21) *Frente Para O Inimigo* (Mina Terrestre)**', '**22) Pin-Up (Montando Míssil)**', '**23) *"Senta A Púa!"***',
        '**24) *“Eu Sou Uma Máquina (do Amor)”***', '**25) Médico (Caveira e Ossos Cruzados no Logotipo)**', '**26) *"OLÁ, MEU NOME É:"***', 
        '**27) *“Abastecido por Café”***', '**28) *“Leve-me Ao Seu Líder”* (OVNI)**', '**29) *“FAÇA SEU TRABALHO”***', '**30) *“Tome Minha Vida (Por Favor)”***', 
        '**31) *“Tô Cheio Dessa Merda!”* (Astronauta com Bolsos Vazios)**', '**32) *"Alérgico a Besteiras"* (Remendo em Estilo Médico)**', 
        '**33) *“Me Salva Primeiro”* (Caduceu)**', '**34) *“Cidadão de Bem”***', '**35) Logotipo da NASA**', '**36) *“Cowboyzão”* (Revólveres Cruzados)**',
        '**37) Pombo no Alvo**', '**38) Cthulhu Chibi**', '**39) *“Bem-vindo à ZONA DE PERIGO”***', '**40) Crânio e Ferramentas Cruzadas**', '**41) Pin-Up (Súcubo)**', 
        '**42) *“TPMF?”* (Tô Pouco Me Fodendo)**', '**43) *“BEBA / LUTE / TREPE”***', '**44) *“Trabalhe Duro / Festeje Mais Ainda”***', '**45) Silhueta Feminina**', 
        '**46) Medidor de Diversão (Leitura: Péssima Hora)**', '**47) *“GAME OVER”* (Noiva e Noivo)**', '**48) Coração**', '**49) *“MELHORAR / ADAPTAR / SUPERAR”***',
        '**50) *“CHUPA!”***', '**51) *“Dono da Porra Toda!”***', '**52) *“Solucionador de Problemas”***', '**53) *“SIGAM-ME OS BONS!”*, Remendo para Costas**', 
        '**54) Martelos Cruzados com Asas**', '**55) *“Mantenha-se Bem Lubrificado”***', '**56) Martelo e Foice Soviética**', '**57) *“Funciona Bem Com Os Outros”***',
        '**58) *“Viva Loucamente e Morra Jovem”***', '**59) Pin-Up (Enfermeira): *“Cê Precisar de Mim... É Só Tocar na Campainha”***', '**60) *“Saco de Pancada”***',
        '**61) *“Eu Não Sou Um Robô”***', '**62) Engrenagem Vermelha**', '**63) *“Não Consigo Consertar Burrice”***', 
        '**64) *“O Espaço é Minha Casa”* (Astronauta Triste)**', '**65) Olho da Providência**', '**66) *“Por Acaso Eu PAREÇO Um Especialista?”***',
        '**67) *“NÔMADE”***', '**68) *“Não Sou Um Cientista de Foguetes / Você Que É Um Idiota”***', '**69) *“LOBO SOLITÁRIO”***', 
        '**70) *“Eu Sou o Guardião do Meu Irmão”***', '**71) *“Mamãe Bem Que Tentou”***', '**72) Aranha Viúva Negra**', 
        '**73) *"Asa de Urubu, Pena de Galinha, Se Você Já Deu..."***', '**74) *“Tamanho Único”* (Granada)**', '**75) Morte, Remendo para Costas**', 
        '**76) *"отъебись"* ("Foda-se", em Russo)**', '**77) *“Só No Sapatinho”***', '**78) Símbolo Atômico', '**79) *"Pela Ciência!***', 
        '**80) *“Na Verdade, EU SOU Um Cientista de Foguetes”***', '**81) *“Procura-se ajuda”***', '**82) Princesa**', 
        '**83) *“Eu Gosto de Minhas Ferramentas Limpas / e Minhas Mulheres Sujas”***', '**84) *“BOM MENINO”***', '**85) Dados (Dois nº 1)**', 
        '**86) *“Viaje para Lugares Exóticos Distantes / Conheça Coisas Incomuns / Seja comido”***', '**87) *“Bom”* (Cérebro)**', '**88) *“Fodona”***',
        '**89) *“Muito Bonito para Morrer”***', '**90) *“Foda-se para Sempre”* (Rosas)**', '**91) Ícaro**', '**92) *"Melhor Amigo das Garotas”* (Diamante)**',
        '**93) Símbolo de Risco de Eletrocussão**', '**94) Cruz Invertida**', '**95) *“Tu Paga Meus Boletos?”*, Remendo para Costas**', '**96) *“Eu ♥ a Mim Mesmo”***',
        '**97) Cereja Dupla**', '**98) *“Voluntário”***', '**99) *“Solve Et Coagula”* (Bafomé)**')

        if message.content == '?p':
            await message.channel.send(f'{message.author.name}, você sorteou: {choice(patch)}')
        

        # Efeito do Pânico. Onde X é o resultado do seu Teste de Efeito de Pânico somado ao seu Estresse atual

        panic2_3 = ('***Super Focado*. Vantagem em todos os testes para nas próximas 1d10 horas.**')

        if message.content == '?s2':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic2_3}')
        
        if message.content == '?s3':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic2_3}')
            
        panic4_5 = ('***Surto de Adrenalina Maior*. Vantagem para todas rolagens pelos próximos 3d10 minutos.**')

        if message.content == '?s4':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic4_5}')

        if message.content == '?s5':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic4_5}')

        panic6_7 = ('***Surto de Adrenalina Menor*. Vantagem para todas rolagens pelos próximos 1d10 minutos.**')
            
        if message.content == '?s6':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic6_7}')

        if message.content == '?s7':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic6_7}')

        panic8_9 = ('***Ansioso*. Ganhe 1 de Estresse.**')
            
        if message.content == '?s8':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic8_9}')

        if message.content == '?s9':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic8_9}')
        
        panic10_11 = ('***Convulsão Nervosa*. Ganhe 2 de Estresse. O membro da tripulação mais próximo também ganha 1 de Estresse.**')

        if message.content == '?s10':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic10_11}')
        
        if message.content == '?s11':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic10_11}')

        panic12_13 = ('***Covardia*. Ganhe 1 de Estresse. Pelas próximas 1d10 horas você deve fazer uma Salvaguarda de Medo para se envolver em combate ou então fugir.**')
        
        if message.content == '?s12':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic12_13}')

        if message.content == '?s13':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic12_13}')

        panic14_15 = ('***Alucinações*. Pelas próximas 2d10 horas (determinado secretamente) você tem problemas em distinguir entre realidade e fantasia.**')

        if message.content == '?s14':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic14_15}')

        if message.content == '?s15':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic14_15}')

        panic16_17 = ('***Medo Paralisante*. Ganhe uma nova fobia permanente. Sempre que você encontrar essa fobia faça uma Salvaguarda de Medo com Desvantagem ou ganhe 1d10 de Estresse.**')
            
        if message.content == '?s16':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic16_17}')

        if message.content == '?s17':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic16_17}')

        panic18_19 = ('***Sobrecarregado*. Ganhe 1d10 de Estresse.**')

        if message.content == '?s18':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic18_19}')

        if message.content == '?s19':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic18_19}')

        panic20_21 = ('***Irritado*. Solta um grito de gelar o sangue. Desvantagem em todos os testes por 2d10 minutos.**')

        if message.content == '?s20':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic20_21}')

        if message.content == '?s21':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic20_21}')

        panic22 = ('***Paranóico*. Pelos próximos 1d10 dias, sempre que um personagem se juntar ao seu grupo (mesmo que apenas por um curto período de tempo), faça uma Salvaguarda de Medo ou ganhe 1 de Estresse.**')

        if message.content == '?s22':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic22}')

        panic23 = ('***Autodestruição*. Pelos próximos Xd10 dias (onde X = Stress) sempre que encontrar um estranho ou inimigo conhecido você deve fazer uma Salvaguarda de Sanidade ou ataque-os imediatamente.**')

        if message.content == '?s23':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic23}')

        panic24 = ('***Catatônico*. Torne-se indiferente e imóvel por Xd10 minutos (onde X = estresse).**')

        if message.content == '?s24':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic24}')

        panic25 = ('***Acabado*. Pelos próximos Xd10 dias (onde X = estresse) faça uma Salvaguarda de Pânico sempre que um membro da tripulação próximo falhar em uma Salvaguarda.**')

        if message.content == '?s25':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic25}')
        
        panic26 = ('***Psicótico*. Ataque imediatamente o membro da tripulação mais próximo até que você cause pelo menos 2d10 de Dano. Se não houver nenhum membro da tripulação por perto, você ataca o ambiente.**')

        if message.content == '?s26':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic26}')

        panic27 = ('***Problemas Compostos*. Role duas vezes nessa tabela.**')

        if message.content == '?s27':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic27}')
        
        panic28 = ('***À Beira da Loucura*. Ganhe 2 novas fobias. Seu Estresse não pode ser reduzido abaixo de 5.**')

        if message.content == '?s28':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic28}')

        panic29 = ('***Colapso Psicológico*. Torna-se permanentemente, irreparavelmente insano. Sua personagem agora é interpretado pelo Warden.**')

        if message.content == '?s29':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic29}')

        panic30 = ('***Infarto*. Morte instantânea.**')

        if message.content == '?s30':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {panic30}')


        # Efeito do Pânico em Andróides. Onde X é o resultado do seu Teste de Efeito de Pânico somado ao seu Estresse atual

        android2_3 = ('***Probabilidades Estabelecidas*. Oferece Vantagem em todos os testes do grupo durante 1 hora.**')

        if message.content == '?a2':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android2_3}')
        
        if message.content == '?a3':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android2_3}')

        android4_5 = ('***Etimologia das Palavras Apresentadas*. Vantagem em rolagens de Conhecimento por 1 hora.**')

        if message.content == '?a4':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android4_5}')

        if message.content == '?a5':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android4_5}')

        android6_7 = ('***Objetos Organizados por Padrões Geométricos*. Todos os outros recebem 1 de Estresse.**')
            
        if message.content == '?a6':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android6_7}')

        if message.content == '?a7':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android6_7}')

        android8_9 = ('***Inventário de Partículas de Pó por Tamanho*. Não pode se envolver em outras tarefas, todos os outros ganham 2 Estresse.**')
            
        if message.content == '?a8':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android8_9}')

        if message.content == '?a9':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android8_9}')
        
        android10_11 = ('***Emite Sons Agudos como uma Máquina de Fax*. Lapsos em código morse, não pode se comunicar ou esgueirar. Todos os outros ganham 2 de Estresse.**')

        if message.content == '?a10':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android10_11}')
        
        if message.content == '?a11':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android10_11}')

        android12_13 = ('***Declara Incorretamente as Probabilidades*. Insiste que tarefas impossíveis são triviais, tarefas triviais são impossíveis... pelas próximas 2d10 horas. Distraindo. Qualquer um que tentar uma tarefa complexa deve fazer uma Salvaguarda de Medo ou ganhar 1d10 de Estresse.**')
        
        if message.content == '?a12':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android12_13}')

        if message.content == '?a13':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android12_13}')

        android14_15 = ('***Movimentos Ansiosos Repetitivos*. Suas tarefas manuais têm Desvantagem, todos os outros ganham 2 de Estresse.**')

        if message.content == '?a14':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android14_15}')

        if message.content == '?a15':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android14_15}')

        android16_17 = ('***Perda de Expressividade*. Discute a irracionalidade de outras fobias, procura desencadeá-las.**')
            
        if message.content == '?a16':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android16_17}')

        if message.content == '?a17':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android16_17}')

        android18_19 = ('***Adesão Não Razoável ao Presente Curso de Ação*. Sofra 1d10 de dano por ferimentos em movimentos repetitivos. Todos os outros rolam Salvaguarda de Medo ou ganham 1d10/2 de Estresse.**')

        if message.content == '?a18':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android18_19}')

        if message.content == '?a19':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android18_19}')

        android20_21 = ('***Niilistacamente Adorador da Fonte de Perigo*. Todos os outros têm Desvantagem nos testes contra isso. Todos os outros fazem uma Salvaguarda de Medo ao deixar de agir contra o perigo ou ganham uma fobia.**')

        if message.content == '?a20':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android20_21}')

        if message.content == '?a21':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android20_21}')

        android22 = ('***Modo Autodestrutivo*. Enlouquecer de raiva, não se retirará do combate independentemente da situação, não aderirá às táticas.**')

        if message.content == '?a22':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android22}')

        android23 = ('***Falha no Teste de Turing*. Tem dificuldade em expressar humanidade. Os membros do grupo fazem uma Salvaguarda de Medo ou ganham 1 de Estresse sempre que você aparece.**')

        if message.content == '?a23':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android23}')

        android24 = ('***Sobrecarga do Sistema*. Crise catatônica num erro cíclico de reinicialização por 1d10 horas.**')

        if message.content == '?a24':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android24}')

        android25 = ('***Núcleo Lógico em Curto*. Comportamento frenético e sem sentido, todo mundo faz um Teste de Pânico.**')

        if message.content == '?a25':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android25}')
        
        android26 = ('***Dano ao Avaliador de Ameaças*. Traia um membro do grupo na primeira oportunidade, acreditando que você está ajudando a tripulação. Todo Estresse ganho é aumentado em 1d10 pelas próximas 1d10 horas.**')

        if message.content == '?a26':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android26}')

        android27 = ('***Corrupção dos Dados Compostos*. Role duas vezes nessa tabela.**')

        if message.content == '?a27':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android27}')
        
        android28 = ('***Faha de Firmware*. Role 1d10 nesta tabela, o comportamento é permanente.**')

        if message.content == '?a28':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android28}')

        android29 = ('***Corrupção de Dados*. O Warden assume o personagem permanentemente, mau funcionamento e comportamento macabro.**')

        if message.content == '?a29':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android29}')

        android30 = ('***Destroçado*. Explosão de cabeça, todos os presentes ganham fobia e 1d10/2 de Estresse (Salvaguarda de Medo).**')

        if message.content == '?a30':
            await message.channel.send(f'{message.author.name}, seu efeito de Pânico é: {android30}')

client = MyClient()
client.run('YOUR BOT TOKEN')

