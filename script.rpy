
# personagens
define p = Character("Pisquinha")
define h = Character("Husk")
define k = Character("Kai")


# o jogo começa aqui

label start:

    scene cena 1
    with fade
    play music "audio/musica.mp3"

    "Dois irmãos Pisquinha e Husk lutam pela liderança do clã dos lobos"

    show pisca at right
    with dissolve

    p "Não quero brigar com você, irmão"

    p "Essa luta não faz sentido para mim"

    hide pisca

    show husk at left
    with dissolve

    h "Deixa de conversa mole Pisquinha"

    h "Isto para mim tem outro nome"

    h "Covardia"

    hide husk

    "Pisquinha deve enfrentar o irmão Husk?"

menu:

    "Sim":
        jump game

    "Não":
        jump book

label game:

    show pisca at right
    with dissolve
    p "Se não há outra escolha, eu estou pronto, irmão"

    hide pisca

    show husk at left
    with dissolve

    h "Farei o que for necessário"

    hide husk

    jump marry

label book:

    show husk at left
    with dissolve

    h "Você não tem escolha, lembre-se a força vem do seu interior"

    hide husk

    show pisca at right
    with dissolve

    p "Eu não queria, mas se é o unico jeito..."

    hide pisca

    jump marry

label marry:

    "Então os irmãos batalham"
    stop music

    return
