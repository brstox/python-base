 email_tmpl = """
    ...: Olá, %(nome)s
    ...:
    ...: Tem interesse em comprar %(produto)s
    ...:
    ...: Este produto é ótimo para resolver %(texto)s
    ...:
    ...: Clique agora %(link)s
    ...:
    ...: Apenas %(quantidade)d disponíveis:
    ...:
    ...: Preço promocional %(preço).2f
    ...: """
    ...:
    ...: clientes = ["Janaína", "Laura", "Helena"]
    ...:
    ...: texto_descritivo = """Problemas de segurança? Na PentaSeg, nossa missão é transformar sua casa em um ambiente seguro e intel
       ⋮ igente. Com soluções personalizadas em sistemas de segurança residencial, oferecemos tecnologia avançada para garantir tranq
       ⋮ uilidade para você e sua família.
    ...:
    ...: Desenvolvemos desde câmeras de monitoramento 24/7 até sistemas de alarme integrados, tudo controlado pelo seu smartphone. Co
       ⋮ mbinando inovação e confiabilidade, a PentaSeg está sempre um passo à frente, protegendo o que mais importa.
    ...:
    ...: Sua segurança em primeiro lugar. Sempre."""
    ...:
    ...: for cliente in clientes:
    ...:     print(email_tmpl % {
    ...:         "nome": cliente,
    ...:         "produto": "Sistema de segurança residencial",
    ...:         "texto": texto_descritivo,
    ...:         "link": "https://pentaseg.com",
    ...:         "quantidade": 1,
    ...:         "preço": 15000.00
    ...:     })

