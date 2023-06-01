# Linguagens de Programação
## Pset 1
Aluno: Henrique Oliveira Waisman </br>
Turma: CC3M </br>
Professor: Abrantes Araújo Silva Filho
### Descrição
Este PSET é uma tradução da primeira tarefa de programação que os alunos da </br>
disciplina “MIT 6.009: Fundamentals of Programming” recebem logo no primeiro </br>
dia de aula, feita para os alunos da disciplina “Linguagens de Programação” na </br>
Universidade Vila Velha (UVV). </br>
## Questões
### Questão 1
#### Se você passar essa imagem (altura: 1 • largura: 4 • pixels: [29, 89, 136, 200]) pelo filtro de inversão, qual seria o output esperado? Justifique sua resposta. </br>
Ao aplicar o filtro de inversão, cada pixel da imagem passará pela função:  </br>
![image_invertida](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/invertida.png) </br>
Após toda imagem passar pelo tratamento, será esperado um output de altura: 1, largura: 4 e pixels: [226, 166, 119, 55]  </br>
### Questão 2
#### Faça a depuração e, quando terminar, seu código deve conseguir passar em todos os testes do grupo de teste TestInvertida (incluindo especificamente o que você acabou de criar). Execute seu filtro de inversão na imagem test_images/bluegill.png, salve o resultado como uma imagem PNG e salve a imagem em seu repositório GitHub.
Chamado: </br>
![call3](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/call3.png) </br>
Input: </br>
![input1](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/test_images/bluegill.png) </br>
Output:  </br>
![image_bluegill](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_resultado/bluegill1.png) </br>
### Questão 3
#### Considere uma etapa de correlacionar uma imagem com o seguinte kernel: </br> 0.00 -0.07 0.00 </br> -0.45 1.20 -0.25 </br> 0.00 -0.12 0.00 </br></br> Aqui está uma parte de uma imagem de amostra, com as luminosidades específicas de alguns pixels:
![image_questao3](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/questao3.png)</br>
#### Qual será o valor do pixel na imagem de saída no local indicado pelo destaque vermelho? </br> Observe que neste ponto ainda não arredondamos ou recortamos o valor, informe exatamente como você calculou. </br> Observação: demonstre passo a passo os cálculos realizados.
Resposta: </br>
Ox,y = 32,76 </br></br>
Cálculo: </br>
80x0 &nbsp;         +	&nbsp; (-0,07x53) &nbsp;   + &nbsp; 99x0 + </br>
(-0,45x129) &nbsp;	+	&nbsp; 127x1,20 &nbsp;     + &nbsp; (-0,25x148) + </br>
175x0 &nbsp;        +	&nbsp; (-0,12x174) &nbsp;  + &nbsp; 193x0 </br></br>
+0		  &nbsp;    -3,71		&nbsp;  +0 </br>
-58,05	&nbsp;	  +152,4	&nbsp;	-37 </br>
+0		  &nbsp;    -20,88  &nbsp;  +0 </br>
= 32,76 </br>
### Questão 4
####  Quando você tiver implementado seu código, tente executá-lo em test_images/pigbird.png com o seguinte kernel 9 × 9: </br> 0 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> 1 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> Ao rodar esse kernel, salve a imagem resultante em seu repositório GitHub. </br>
Chamado:</br> 
![call5](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/call5.png)</br> 
Input:</br>
![input2](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/test_images/pigbird.png)</br>
Output:</br> 
![pigbird](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_resultado/pigbird1.png)</br> 
### Questão da Seção 5.1
#### Quando você terminar e seu código passar em todos os testes relacionados ao desfoque, execute seu filtro na imagem test_images/cat.png com um kernel de desfoque de caixa de tamanho 5, salve o resultado como uma imagem PNG e faça o upload para seu repositório GitHub.
Chamado:</br>
![call5.1](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/call51.png)</br>
Input:</br>
![input3](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/test_images/cat.png)</br>
Output:</br>
![cat1](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_resultado/cat1.png)</br>
### Questão 5
#### Se quisermos usar uma versão desfocada B que foi feita com um kernel de desfoque de caixa de 3 × 3, que kernel k poderíamos usar para calcular toda a imagem nítida com uma única correlação? Justifique sua resposta mostrando os cálculos.
O kernel pode ser calculado pela equação descrita na seção 5.2 do pdf:
  - Sx,y = round(2Ix,y − Bx,y) </br> 
Como queremos achar o kernel de entrada, precisamos usar o kernel identidade descrito na seção 4.3.1
  - 0 0 0 </br> 0 1 0 </br> 0 0 0 </br>
Multiplicando por 2 como mostrado na equação 2Ix,y − Bx,y, temos:
  - 0 0 0 </br> 0 2 0 </br> 0 0 0 </br>
Bastaria então fazer a subtração de 2Ix,y de 2bx, y que obteríamos o resultado esperado com uma única correlação. </br>
#### Aplicação:
Chamado:</br>
![call55](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/call55.png)</br>
Input:</br>
![python](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/test_images/python.png)</br>
Output:</br>
![python1](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_resultado/python1.png)</br>
### Questão 6
#### Explique o que cada um dos kernels acima, por si só, está fazendo. Tente executar mostrar nos resultados dessas correlações intermediárias para ter uma noção do que está acontecendo aqui.
#### Kernel Kx:</br>-1 0 1</br>-2 0 2</br>-1 0 1</br></br>Kernel Ky:</br>-1 -2 -1</br>0 0 0</br>1 2 1
Kernel Kx destaca bordas no eixo X e Ky faz o mesmo no eixo Y</br>
#### Chamado: </br>
![call6](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/call6.png)</br>
#### Original:</br>
![construct](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/test_images/construct.png)
#### Kernel Kx:</br>
![kx](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_resultado/construct1.png)</br>
#### Kernel Ky:</br>
![ky](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_resultado/construct2.png)</br>
#### Ambos Aplicados:</br>
![kxky](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_resultado/construct3.png)</br>
# Arquivo Teste:</br>
![test](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/teste.png)
