def contato(request):
    """Página de contato (formulário)"""
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Salva a solicitação no banco
            solicitacao = form.save()

            # Envia email (opcional)
            try:
                send_mail(
                    subject=f'Nova solicitação: {solicitacao.assunto}',
                    message=f'''
Nova solicitação de contato recebida:

Nome: {solicitacao.nome}
Email: {solicitacao.email}
Telefone: {solicitacao.telefone}
Assunto: {solicitacao.assunto}

Mensagem:
{solicitacao.mensagem}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@reformas.com',
                    recipient_list=['contato@reformas.com'],  # Substitua pelo seu email
                )
            except Exception as e:
                print(f'Erro ao enviar email: {e}')

            messages.success(request, 'Sua mensagem foi enviada com sucesso! Entraremos em contato em breve.')
            return redirect('reformasapp:contato')
    else:
        form = ContatoForm()

    context = {
        'form': form
    }

    return render(request, 'reformasapp/contato.html', context)
  
