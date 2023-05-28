# Linguagens de Programação
## Pset 1
Aluno: Henrique Oliveira Waisman </br>
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
Output:  </br>
![image_bluegill](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/bluegill.png) </br>
### Questão 3
#### Considere uma etapa de correlacionar uma imagem com o seguinte kernel: </br> 0.00 -0.07 0.00 </br> -0.45 1.20 -0.25 </br> 0.00 -0.12 0.00 </br></br> Aqui está uma parte de uma imagem de amostra, com as luminosidades específicas de alguns pixels:
![image_questao3](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/questao3.png)</br>
#### Qual será o valor do pixel na imagem de saída no local indicado pelo destaque vermelho? </br> Observe que neste ponto ainda não arredondamos ou recortamos o valor, informe exatamente como você calculou. </br> Observação: demonstre passo a passo os cálculos realizados.
Resposta: </br>
Ox,y = 32,76 </br>
Cálculo: </br>
80x0 &nbsp;         +	&nbsp; (-0,07x53) &nbsp;   + &nbsp; 99x0 + </br>
(-0,45x129) &nbsp;	+	&nbsp; 127x1,20 &nbsp;     + &nbsp; (-0,25x148) + </br>
175x0 &nbsp;        +	&nbsp; (-0,12x174) &nbsp;  + &nbsp; 193x0 </br>
+0		  &nbsp;    -3,71		&nbsp;  +0 </br>
-58,05	&nbsp;	  +152,4	&nbsp;	-37 </br>
+0		  &nbsp;    -20,88  &nbsp;  +0 </br>
= 32,76 </br>
### Questão 4
####  Quando você tiver implementado seu código, tente executá-lo em test_images/pigbird.png com o seguinte kernel 9 × 9: </br> 0 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> 1 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> 0 0 0 0 0 0 0 0 0 </br> Ao rodar esse kernel, salve a imagem resultante em seu repositório GitHub. </br>
Chamado:</br> 
![call5](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/call5.png)</br> 
Output:</br> 
![pigbird](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/pigbird1.png)</br> 
### Questão da Seção 5.1
#### Quando você terminar e seu código passar em todos os testes relacionados ao desfoque, execute seu filtro na imagem test_images/cat.png com um kernel de desfoque de caixa de tamanho 5, salve o resultado como uma imagem PNG e faça o upload para seu repositório GitHub.
Chamado: </br>
![call5.1]([https://github.com/henriquewaisman/ubvv](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/call51.png))
Output: </br>
![cat1](https://github.com/henriquewaisman/uvv_lp_1_cc3m/blob/main/img_readme/cat1.png)
