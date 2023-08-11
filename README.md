YouTube_to_mp3
Este é um projeto que permite converter vídeos do YouTube em arquivos de áudio no formato MP3. Ele utiliza a biblioteca pytube para fazer o download dos vídeos e a biblioteca moviepy para converter os vídeos baixados em arquivos de áudio MP3.

Observação: Certifique-se de que está utilizando este projeto de acordo com as leis de direitos autorais e os termos de uso do YouTube. Baixar e distribuir conteúdo protegido por direitos autorais sem permissão é ilegal.

Como usar
Certifique-se de que você tem o Python instalado em seu sistema.
Clone este repositório para o seu computador ou faça o download do código-fonte.
Instale as dependências necessárias executando o seguinte comando:
bash
Copy code
pip install -r requirements.txt
Execute o script youtube_to_mp3.py:
bash
Copy code
python youtube_to_mp3.py
O script irá pedir para você inserir o URL do vídeo do YouTube que deseja converter. Copie o URL do vídeo e cole no terminal.

O script irá baixar o vídeo e convertê-lo em um arquivo MP3. O arquivo resultante será salvo na pasta output.

Configurações
Você pode personalizar algumas configurações do projeto editando o arquivo config.json:

output_folder: O diretório onde os arquivos MP3 convertidos serão salvos.
bitrate: A taxa de bits do áudio do arquivo MP3 resultante.
Contribuições
Contribuições são bem-vindas! Se você deseja contribuir para este projeto, sinta-se à vontade para criar um fork, fazer as alterações e enviar um pull request.

Antes de enviar um pull request, certifique-se de testar suas alterações e seguir as diretrizes de estilo de código.

Aviso Legal
Este projeto é apenas para fins educacionais e de aprendizado. O uso inadequado deste projeto para violar os direitos autorais e os termos de uso do YouTube é estritamente proibido. Os criadores e colaboradores deste projeto não se responsabilizam pelo uso indevido do mesmo.

Licença
Este projeto está sob a licença MIT.
