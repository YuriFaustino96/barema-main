# A linha abaixo deve ser a PRIMEIRA instrução do script
import streamlit as st
st.set_page_config(page_title="Barema - UESC", layout="wide")

import requests
import pandas as pd
from io import BytesIO
from pathlib import Path

st.title("📄 Barema - Produção Científica - UESC")

# === Lista de docentes
dados_docentes =[
    {
        "CPF": "48539015749",
        "Nome": "José Renato de Castro Pessôa",
        "DataNascimento": "09061960"
    },
    {
        "CPF": "53093534534",
        "Nome": "Rosenira Serpa da Cruz",
        "DataNascimento": "12081968"
    },
    {
        "CPF": "17998564881",
        "Nome": "César Alberto Bravo Pariente",
        "DataNascimento": "23031964"
    },
    {
        "CPF": "22368885897",
        "Nome": "Carla Martins Kaneto",
        "DataNascimento": "23011982"
    },
    {
        "CPF": "98491172572",
        "Nome": "Cleverson Alves de Lima",
        "DataNascimento": "03021981"
    },
    {
        "CPF": "00679790500",
        "Nome": "Marcos dos Santos Ferreira",
        "DataNascimento": "07081983"
    },
    {
        "CPF": "00923521542",
        "Nome": "Ruan Carlos de Araújo Moura",
        "DataNascimento": "19051986"
    },
    {
        "CPF": "89641248049",
        "Nome": "Fábio dos Santos Massena",
        "DataNascimento": "15051976"
    },
    {
        "CPF": "10818911816",
        "Nome": "Vera Rosa Capelossi",
        "DataNascimento": "06111965"
    },
    {
        "CPF": "76694240015",
        "Nome": "João Luis Almeida da Silva",
        "DataNascimento": "01061976"
    },
    {
        "CPF": "27520540847",
        "Nome": "Rodolfo Mariano Lopes da Silva",
        "DataNascimento": "17021979"
    },
    {
        "CPF": "94649197104",
        "Nome": "Fernando Cesário Rangel",
        "DataNascimento": "26071977"
    },
    {
        "CPF": "07520683850",
        "Nome": "Marcelo Pires de Oliveira",
        "DataNascimento": "02121965"
    },
    {
        "CPF": "31982577860",
        "Nome": "Larissa Rocha Santos",
        "DataNascimento": "13061984"
    },
    {
        "CPF": "47822961500",
        "Nome": "Cléa dos Santos Ferreira Mariano",
        "DataNascimento": "12121967"
    },
    {
        "CPF": "05125670693",
        "Nome": "Sonia Cristina Oliveira Melo",
        "DataNascimento": "03091980"
    },
    {
        "CPF": "71038876672",
        "Nome": "Maria Jaqueline Vasconcelos",
        "DataNascimento": "30011971"
    },
    {
        "CPF": "32453753878",
        "Nome": "Carla Fernanda Fávaro",
        "DataNascimento": "11051984"
    },
    {
        "CPF": "12352279879",
        "Nome": "Alexandre Schiavetti",
        "DataNascimento": "13021970"
    },
    {
        "CPF": "29487010823",
        "Nome": "Eduardo Koji Tamura",
        "DataNascimento": "13061981"
    },
    {
        "CPF": "12955797820",
        "Nome": "Carla Cristina Romano",
        "DataNascimento": "15101970"
    },
    {
        "CPF": "10971999830",
        "Nome": "Elilton Rodrigues Edwards",
        "DataNascimento": "04111968"
    },
    {
        "CPF": "87827913504",
        "Nome": "Viviane Borges Dias",
        "DataNascimento": "26031975"
    },
    {
        "CPF": "48250570553",
        "Nome": "Ronaldo Lima Gomes",
        "DataNascimento": "01121969"
    },
    {
        "CPF": "03226899619",
        "Nome": "Izaltina Silva Jardim Cavalli",
        "DataNascimento": "11041977"
    },
    {
        "CPF": "26478197859",
        "Nome": "Alexandre Justo de Oliveira Lima",
        "DataNascimento": "10111977"
    },
    {
        "CPF": "84250321568",
        "Nome": "Martín Roberto del Valle Alvarez",
        "DataNascimento": "17051968"
    },
    {
        "CPF": "93022310978",
        "Nome": "Marcelo Franco",
        "DataNascimento": "05021974"
    },
    {
        "CPF": "09590114717",
        "Nome": "Weslem Liberato Silva",
        "DataNascimento": "20021983"
    },
    {
        "CPF": "10202806707",
        "Nome": "Maíra Benchimol de Souza",
        "DataNascimento": "02031984"
    },
    {
        "CPF": "03343990680",
        "Nome": "Niel Nascimento Teixeira",
        "DataNascimento": "14021976"
    },
    {
        "CPF": "18802112894",
        "Nome": "CRISTIANO AUGUSTO DA SILVA",
        "DataNascimento": "08031976"
    },
    {
        "CPF": "61601667353",
        "Nome": "Sandra Rocha Gadelha Mello",
        "DataNascimento": "21021975"
    },
    {
        "CPF": "83091580504",
        "Nome": "Thiago Pereira das Chagas",
        "DataNascimento": "08061982"
    },
    {
        "CPF": "00171845765",
        "Nome": "Carlos Priminho Pirovani",
        "DataNascimento": "10081971"
    },
    {
        "CPF": "12663756865",
        "Nome": "Lauro juliano marin",
        "DataNascimento": "15041975"
    },
    {
        "CPF": "29804029820",
        "Nome": "Anaiá da Paixão Sevá",
        "DataNascimento": "26121980"
    },
    {
        "CPF": "81087160634",
        "Nome": "Carlos Roberto Guimarães",
        "DataNascimento": "07061968"
    },
    {
        "CPF": "80865860572",
        "Nome": "Lauricio Alves Carvalho Pedrosa",
        "DataNascimento": "01031981"
    },
    {
        "CPF": "88364259504",
        "Nome": "ANA PAULA MELO MARIANO",
        "DataNascimento": "27071972"
    },
    {
        "CPF": "81568185553",
        "Nome": "Geizane Lima da Silva",
        "DataNascimento": "28071981"
    },
    {
        "CPF": "03297961511",
        "Nome": "Daniele de Santana Rocha",
        "DataNascimento": "06021987"
    },
    {
        "CPF": "03512447783",
        "Nome": "Elisa Prestes Massena",
        "DataNascimento": "23031975"
    },
    {
        "CPF": "00062637550",
        "Nome": "Liliane Xavier Neves",
        "DataNascimento": "19081980"
    },
    {
        "CPF": "11921545844",
        "Nome": "WALTER FAGUNDES MORALES",
        "DataNascimento": "23021968"
    },
    {
        "CPF": "55620698068",
        "Nome": "Mauro de Paula Moreira",
        "DataNascimento": "29091966"
    },
    {
        "CPF": "17684134876",
        "Nome": "Rodrigo Luis Silva Ribeiro Santos",
        "DataNascimento": "27041977"
    },
    {
        "CPF": "33606765568",
        "Nome": "Carlos Alberto Menezes",
        "DataNascimento": "03071965"
    },
    {
        "CPF": "32724123875",
        "Nome": "Matheus Garcia Soares",
        "DataNascimento": "23121985"
    },
    {
        "CPF": "03424046795",
        "Nome": "George Rego Albuquerque",
        "DataNascimento": "16011974"
    },
    {
        "CPF": "37960717591",
        "Nome": "Roque Pinto da Silva Santos",
        "DataNascimento": "23101972"
    },
    {
        "CPF": "66336368653",
        "Nome": "Rosilene Aparecida de Oliveira",
        "DataNascimento": "30101966"
    },
    {
        "CPF": "07947729603",
        "Nome": "JUNEO FREITAS SILVA",
        "DataNascimento": "24041985"
    },
    {
        "CPF": "74089617049",
        "Nome": "Franco Dani Rico Amado",
        "DataNascimento": "17121973"
    },
    {
        "CPF": "05795881732",
        "Nome": "Dany Sanchez Dominguez",
        "DataNascimento": "30111975"
    },
    {
        "CPF": "96898640097",
        "Nome": "SIMONI TORMOHLEN GEHLEN",
        "DataNascimento": "03101977"
    },
    {
        "CPF": "78209587749",
        "Nome": "Andre Luis Batista Ribeiro",
        "DataNascimento": "09011968"
    },
    {
        "CPF": "52126978249",
        "Nome": "Yvonnick Victor Le Pendu",
        "DataNascimento": "09111967"
    },
    {
        "CPF": "29060748883",
        "Nome": "Marcos Rodrigo Trindade Pinheiro Menuchi",
        "DataNascimento": "27011980"
    },
    {
        "CPF": "01665612908",
        "Nome": "David Ohara",
        "DataNascimento": "17111975"
    },
    {
        "CPF": "92200435134",
        "Nome": "Danilo Simonini Teixeira",
        "DataNascimento": "15101979"
    },
    {
        "CPF": "30587309857",
        "Nome": "Wilson Barros Luiz",
        "DataNascimento": "03061982"
    },
    {
        "CPF": "96859911549",
        "Nome": "Ricardo Siqueira Bovendorp",
        "DataNascimento": "27121979"
    },
    {
        "CPF": "68512341068",
        "Nome": "Eduardo Gross",
        "DataNascimento": "04011973"
    },
    {
        "CPF": "65141989020",
        "Nome": "Gil Marcelo Reuss Strenzel",
        "DataNascimento": "06101966"
    },
    {
        "CPF": "84556510678",
        "Nome": "Gessilene Silveira Kanthack",
        "DataNascimento": "29041973"
    },
    {
        "CPF": "97591300504",
        "Nome": "Cristiane Batista da Silva Santos",
        "DataNascimento": "10031977"
    },
    {
        "CPF": "77609530549",
        "Nome": "MICHELLE ARAÚJO MOREIRA",
        "DataNascimento": "13081977"
    },
    {
        "CPF": "33405751268",
        "Nome": "Jorge Henrique Sales",
        "DataNascimento": "17111965"
    },
    {
        "CPF": "04278519710",
        "Nome": "Renata Santiago Alberto Carlos",
        "DataNascimento": "12031975"
    },
    {
        "CPF": "60656522534",
        "Nome": "José Augusto Gomes Azevêdo",
        "DataNascimento": "17041971"
    },
    {
        "CPF": "02330079893",
        "Nome": "Laura de Almeida",
        "DataNascimento": "03111963"
    },
    {
        "CPF": "00013654527",
        "Nome": "FÁBIO ALAN CARQUEIJA AMORIM",
        "DataNascimento": "22031981"
    },
    {
        "CPF": "65617436520",
        "Nome": "Dejeane de Oliveira Silva",
        "DataNascimento": "21121970"
    },
    {
        "CPF": "13115811896",
        "Nome": "Paulo Eduardo Ambrosio",
        "DataNascimento": "28101969"
    },
    {
        "CPF": "30241098890",
        "Nome": "Luciene Cristina Gastalho Campos Luiz",
        "DataNascimento": "15111982"
    },
    {
        "CPF": "36314048087",
        "Nome": "Celso Carlino  Maria Fornari Junior",
        "DataNascimento": "15121961"
    },
    {
        "CPF": "04685965698",
        "Nome": "Poliana de Castro Melo",
        "DataNascimento": "20041981"
    },
    {
        "CPF": "75018241500",
        "Nome": "Andréa dos Santos Souza",
        "DataNascimento": "25071975"
    },
    {
        "CPF": "17143674877",
        "Nome": "Luciana Sedano de Souza",
        "DataNascimento": "15031974"
    },
    {
        "CPF": "13746992842",
        "Nome": "Eduardo Ary Villela Marinho",
        "DataNascimento": "27091967"
    },
    {
        "CPF": "16330223823",
        "Nome": "marcelo henrique dias",
        "DataNascimento": "23121968"
    },
    {
        "CPF": "77746392504",
        "Nome": "Aline Conceição Souza",
        "DataNascimento": "24031980"
    },
    {
        "CPF": "97374962568",
        "Nome": "Erik Galvão Paranhos da Silva",
        "DataNascimento": "24101979"
    },
    {
        "CPF": "88687252749",
        "Nome": "Norma Eliane Pereira",
        "DataNascimento": "11091965"
    },
    {
        "CPF": "84786787604",
        "Nome": "Ana Paula Trovatti Uetanabaro",
        "DataNascimento": "19121972"
    },
    {
        "CPF": "06118645680",
        "Nome": "Cíntia Borges de Almeida",
        "DataNascimento": "25011983"
    },
    {
        "CPF": "02444400500",
        "Nome": "Milena Magalhães Aleluia",
        "DataNascimento": "08101986"
    },
    {
        "CPF": "62944266691",
        "Nome": "Virgínia Lúcia Fontes Soares",
        "DataNascimento": "29031971"
    },
    {
        "CPF": "05161408685",
        "Nome": "Eduardo Delcides Bernardes",
        "DataNascimento": "26011983"
    },
    {
        "CPF": "84390654691",
        "Nome": "Rachel Passos Rezende",
        "DataNascimento": "27081970"
    },
    {
        "CPF": "11648262805",
        "Nome": "Elena Malpezzi Marinho",
        "DataNascimento": "01081966"
    },
    {
        "CPF": "00834296543",
        "Nome": "Iuri Ribeiro Dias",
        "DataNascimento": "09111983"
    },
    {
        "CPF": "41971078549",
        "Nome": "Alberto Barretto Kruschewsky",
        "DataNascimento": "30051964"
    },
    {
        "CPF": "29445012836",
        "Nome": "ELIANA CAZETTA",
        "DataNascimento": "22111978"
    },
    {
        "CPF": "08946405694",
        "Nome": "Miriã Cristina Pereira Fagundes",
        "DataNascimento": "22041988"
    },
    {
        "CPF": "18441387800",
        "Nome": "Erica Cristina Almeida",
        "DataNascimento": "24061976"
    },
    {
        "CPF": "55929745587",
        "Nome": "Guilhardes de Jesus Júnior",
        "DataNascimento": "08011972"
    },
    {
        "CPF": "15600669895",
        "Nome": "Luiz Carlos Salay",
        "DataNascimento": "10111969"
    },
    {
        "CPF": "00989276635",
        "Nome": "regiane cristina duarte",
        "DataNascimento": "04041974"
    },
    {
        "CPF": "62519212349",
        "Nome": "Carla Regina Ferreira Freire Guimarães",
        "DataNascimento": "14061973"
    },
    {
        "CPF": "48035556304",
        "Nome": "MARIO SERGIO LIMA DE LAVOR",
        "DataNascimento": "04041975"
    },
    {
        "CPF": "41700031520",
        "Nome": "Ivon Pinheiro Lôbo",
        "DataNascimento": "02011967"
    },
    {
        "CPF": "94367663604",
        "Nome": "Adriana Bozzi",
        "DataNascimento": "04071975"
    },
    {
        "CPF": "93671717068",
        "Nome": "Cristina Luísa Conceição de Oliveira",
        "DataNascimento": "09111976"
    },
    {
        "CPF": "78938392520",
        "Nome": "Gildson Queiroz de Jesus",
        "DataNascimento": "03091979"
    },
    {
        "CPF": "09051646798",
        "Nome": "Victor Goyannes Dill Orrico",
        "DataNascimento": "16081980"
    },
    {
        "CPF": "79019684787",
        "Nome": "Erminda da Conceição Guerreiro Couto",
        "DataNascimento": "12031962"
    },
    {
        "CPF": "89823940525",
        "Nome": "Sílvia Maria Santos Carvalho",
        "DataNascimento": "21111975"
    },
    {
        "CPF": "64021564691",
        "Nome": "Jane Lima dos Santos",
        "DataNascimento": "17111967"
    },
    {
        "CPF": "86924940544",
        "Nome": "Marcio Luis Oliveira Ferreira",
        "DataNascimento": "06041977"
    },
    {
        "CPF": "23387050330",
        "Nome": "Antônia M M Barbosa",
        "DataNascimento": "21101963"
    },
    {
        "CPF": "34709234850",
        "Nome": "RAFAEL MARANI BARBOSA",
        "DataNascimento": "25021986"
    },
    {
        "CPF": "08671384675",
        "Nome": "Erickson Fabiano Moura Sousa Silva",
        "DataNascimento": "03111986"
    },
    {
        "CPF": "03303592900",
        "Nome": "Aline Patricia Mano",
        "DataNascimento": "07121981"
    },
    {
        "CPF": "44190590525",
        "Nome": "Fabio Pinto Gomes",
        "DataNascimento": "10071970"
    },
    {
        "CPF": "22957246864",
        "Nome": "Debora Duarte dos Santos",
        "DataNascimento": "10011987"
    },
    {
        "CPF": "92110932520",
        "Nome": "Raimundo Alves Lima Sobrinho",
        "DataNascimento": "09011977"
    },
    {
        "CPF": "01720211620",
        "Nome": "Orlando Jose Katime Santrich",
        "DataNascimento": "12051975"
    },
    {
        "CPF": "76832791704",
        "Nome": "Marcial Cotes Jorge",
        "DataNascimento": "12021964"
    },
    {
        "CPF": "04464336671",
        "Nome": "Roberto Ferreira Machado Michel",
        "DataNascimento": "06031980"
    },
    {
        "CPF": "73329916672",
        "Nome": "fatima Cerqueira Alvim",
        "DataNascimento": "08110972"
    },
    {
        "CPF": "13713533873",
        "Nome": "Adriana Ramos Mendes",
        "DataNascimento": "23111968"
    },
    {
        "CPF": "11341231836",
        "Nome": "Eduardo Lopes Piris",
        "DataNascimento": "10091972"
    },
    {
        "CPF": "52976777500",
        "Nome": "Eurivalda Ribeiro dos Santos Santana",
        "DataNascimento": "22031969"
    },
    {
        "CPF": "42569303534",
        "Nome": "Raildo Mota de Jesus",
        "DataNascimento": "14041967"
    },
    {
        "CPF": "13251393863",
        "Nome": "Anibal Ramadan Oliveira",
        "DataNascimento": "26011971"
    },
    {
        "CPF": "07152653771",
        "Nome": "Alexandre Dias Munhoz",
        "DataNascimento": "30031974"
    },
    {
        "CPF": "92437141553",
        "Nome": "Cícero Alfredo da Silva Filho",
        "DataNascimento": "01051977"
    },
    {
        "CPF": "87418401515",
        "Nome": "Rogério Soares de Oliveira",
        "DataNascimento": "29011976"
    },
    {
        "CPF": "04182954505",
        "Nome": "Vanessa Thamyris Carvalho dos Santos",
        "DataNascimento": "16021989"
    },
    {
        "CPF": "22945432897",
        "Nome": "Arturo Rodolfo Samana",
        "DataNascimento": "11081967"
    },
    {
        "CPF": "05197705604",
        "Nome": "Marcelo Gomes da Silva",
        "DataNascimento": "10031980"
    },
    {
        "CPF": "03939214507",
        "Nome": "Emanuella Gomes Maia",
        "DataNascimento": "26041989"
    },
    {
        "CPF": "25907171803",
        "Nome": "Emanuela Cardoso da Silva",
        "DataNascimento": "03011977"
    },
    {
        "CPF": "66509114100",
        "Nome": "Roueda Abou Said",
        "DataNascimento": "09031973"
    },
    {
        "CPF": "02837945692",
        "Nome": "Maxwell Roger da P Siqueira",
        "DataNascimento": "20121975"
    },
    {
        "CPF": "84378832534",
        "Nome": "Romari Martinez Montano",
        "DataNascimento": "05091971"
    },
    {
        "CPF": "75937611691",
        "Nome": "Vaneide Gomes",
        "DataNascimento": "21091969"
    },
    {
        "CPF": "59797797520",
        "Nome": "Miríades Augusto da Silva",
        "DataNascimento": "01081968"
    },
    {
        "CPF": "83421106053",
        "Nome": "Mirco Solé Kienle",
        "DataNascimento": "21111973"
    },
    {
        "CPF": "95517839568",
        "Nome": "Elizama Aguiar de Oliveira",
        "DataNascimento": "15071978"
    },
    {
        "CPF": "05387283700",
        "Nome": "Esbel Tomas Vlero Orellana",
        "DataNascimento": "28091972"
    },
    {
        "CPF": "93842465904",
        "Nome": "Andréa Miura da Costa",
        "DataNascimento": "21071975"
    },
    {
        "CPF": "03610573422",
        "Nome": "Marcio Barbalho Dantas Bezerra",
        "DataNascimento": "11011981"
    },
    {
        "CPF": "03336571529",
        "Nome": "Andréia Silva Araujo",
        "DataNascimento": "05011988"
    },
    {
        "CPF": "06464036807",
        "Nome": "Dirceu Martins Alves",
        "DataNascimento": "24091964"
    },
    {
        "CPF": "05303305716",
        "Nome": "Zina Angélica Cáceres Benavides",
        "DataNascimento": "18091962"
    },
    {
        "CPF": "56721013568",
        "Nome": "Ailton Pinheiro Lobo",
        "DataNascimento": "30111968"
    },
    {
        "CPF": "84824255449",
        "Nome": "Afonso Henriques",
        "DataNascimento": "04041966"
    },
    {
        "CPF": "17410000848",
        "Nome": "Daniela Mariano Lopes da Silva",
        "DataNascimento": "26101975"
    },
    {
        "CPF": "40053598172",
        "Nome": "Élida Paulina Ferreira",
        "DataNascimento": "21041964"
    },
    {
        "CPF": "29527754860",
        "Nome": "TIAGO NICOLA LAVOURA",
        "DataNascimento": "03051982"
    },
    {
        "CPF": "41374533068",
        "Nome": "André Luis Mitidieri Pereira",
        "DataNascimento": "18021967"
    },
    {
        "CPF": "01970099720",
        "Nome": "Andréa da Silva Gomes",
        "DataNascimento": "23071973"
    },
    {
        "CPF": "02616468778",
        "Nome": "BIANCA MENDES MACIEL",
        "DataNascimento": "22011976"
    },
    {
        "CPF": "27620600876",
        "Nome": "Camila Fabiana Rossi Squarcini",
        "DataNascimento": "05031979"
    },
    {
        "CPF": "31202201830",
        "Nome": "Camila Meneghetti",
        "DataNascimento": "09011983"
    },
    {
        "CPF": "27876592848",
        "Nome": "Camila Righetto Cassano",
        "DataNascimento": "22041978"
    },
    {
        "CPF": "77595165504",
        "Nome": "Cláudia Ribeiro Santana",
        "DataNascimento": "15071974"
    },
    {
        "CPF": "00139388788",
        "Nome": "Emilia Peixoto Vieira",
        "DataNascimento": "18011970"
    },
    {
        "CPF": "27691168861",
        "Nome": "Felipe Eduardo Ferreira Marta",
        "DataNascimento": "14081978"
    },
    {
        "CPF": "51764601653",
        "Nome": "Fernando Faustino de Oliveira",
        "DataNascimento": "27121966"
    },
    {
        "CPF": "21464106800",
        "Nome": "Flaviana dos Santos Silva",
        "DataNascimento": "18081979"
    },
    {
        "CPF": "84046546387",
        "Nome": "Julieta Rangel de Oliveira",
        "DataNascimento": "27011980"
    },
    {
        "CPF": "43336779553",
        "Nome": "Nair Floresta Andrade Neta",
        "DataNascimento": "20041970"
    },
    {
        "CPF": "07660646702",
        "Nome": "Raquel da Silva Ortega",
        "DataNascimento": "29051979"
    },
    {
        "CPF": "58605967587",
        "Nome": "Rozemere Cardoso de Souza",
        "DataNascimento": "25041971"
    },
    {
        "CPF": "78524687053",
        "Nome": "Sócrates Jacobo Moquete Guzmán",
        "DataNascimento": "22021964"
    },
    {
        "CPF": "07881138793",
        "Nome": "Tatiany Pertel Sabaini Dalben",
        "DataNascimento": "13071978"
    },
    {
        "CPF": "13220870597",
        "Nome": "Vitória Solange Coelho Ferreira",
        "DataNascimento": "12041958"
    },
    {
        "CPF": "96432594553",
        "Nome": "WOLNEY GOMES ALMEIDA",
        "DataNascimento": "29081980"
    },
    {
        "CPF": "54599792691",
        "Nome": "Marco Antonio Costa",
        "DataNascimento": "19061965"
    },
    {
        "CPF": "62554875634",
        "Nome": "Ronan Xavier Corrêa",
        "DataNascimento": "14081967"
    },
    {
        "CPF": "98584138587",
        "Nome": "JULIANNA NASCIMENTO TOREZANI",
        "DataNascimento": "27041980"
    },
    {
        "CPF": "03875882997",
        "Nome": "LACITA MENEZES SKALINSKI",
        "DataNascimento": "04071982"
    },
    {
        "CPF": "01553328566",
        "Nome": "Adi Neves Rocha",
        "DataNascimento": "05091984"
    },
    {
        "CPF": "01647613574",
        "Nome": "RAFAEL RODRIGUES DE QUEIOZ FREITAS",
        "DataNascimento": "16061986"
    },
    {
        "CPF": "04036936590",
        "Nome": "Samene Batista Pereira Santana",
        "DataNascimento": "30011987"
    },
    {
        "CPF": "01709625392",
        "Nome": "ROCHELE SHEILA VASCONCELOS",
        "DataNascimento": "25021986"
    },
    {
        "CPF": "05731005516",
        "Nome": "Lucas Xavier Trindade",
        "DataNascimento": "17081991"
    },
    {
        "CPF": "01537905554",
        "Nome": "Thiago Ferreira de Sousa",
        "DataNascimento": "19021986"
    },
    {
        "CPF": "10000793680",
        "Nome": "Natânia Silva Ferreira",
        "DataNascimento": "02071990"
    },
    {
        "CPF": "17396142830",
        "Nome": "Silvano da Conceição",
        "DataNascimento": "13081974"
    },
    {
        "CPF": "34056876835",
        "Nome": "Lucas José Luduverio Pizauro",
        "DataNascimento": "22021985"
    },
    {
        "CPF": "17332177897",
        "Nome": "Martha Ximena Torres Delgado",
        "DataNascimento": "18041968"
    },
    {
        "CPF": "01939594103",
        "Nome": "Stephanie Carvalho Borges",
        "DataNascimento": "27111986"
    },
    {
        "CPF": "02633880509",
        "Nome": "Indman Ruana Lima Queiroz",
        "DataNascimento": "24091989"
    },
    {
        "CPF": "02972971558",
        "Nome": "LUIZA RENATA FELIX DE CARVALHO LIMA",
        "DataNascimento": "23071991"
    },
    {
        "CPF": "99282968553",
        "Nome": "Lilian Moreira Cruz",
        "DataNascimento": "05051979"
    },
    {
        "CPF": "04604027579",
        "Nome": "Mariane Porto Lima",
        "DataNascimento": "19021992"
    },
    {
        "CPF": "27824185800",
        "Nome": "Carlos Gustavo Nóbrega de Jesus",
        "DataNascimento": "14081976"
    },
    {
        "CPF": "00444635530",
        "Nome": "Luana Novaes Santos",
        "DataNascimento": "22071983"
    },
    {
        "CPF": "75019485500",
        "Nome": "Pedro Alexandre Gomes Leite",
        "DataNascimento": "02031976"
    },
    {
        "CPF": "04839440506",
        "Nome": "Maria Dolores Sosin Rodriguez",
        "DataNascimento": "02091989"
    },
    {
        "CPF": "06176370752",
        "Nome": "Lina María Hurtado Gómez",
        "DataNascimento": "26061978"
    },
    {
        "CPF": "16786087850",
        "Nome": "Aparecida do Carmo Zerbo Tremacoldi",
        "DataNascimento": "16041961"
    },
    {
        "CPF": "02214012532",
        "Nome": "Isac Pimentel Guimaraes",
        "DataNascimento": "28011986"
    },
    {
        "CPF": "45699720472",
        "Nome": "Ivone Maia de Mello",
        "DataNascimento": "26111964"
    },
    {
        "CPF": "01215259530",
        "Nome": "LUCAS GABRIEL SANTOS COSTA",
        "DataNascimento": "18031983"
    },
    {
        "CPF": "63066378004",
        "Nome": "Antônio Carlos Luz Costa",
        "DataNascimento": "08041969"
    },
    {
        "CPF": "33310326896",
        "Nome": "Jose Carlos Morante Filho",
        "DataNascimento": "14091984"
    },
    {
        "CPF": "03202954512",
        "Nome": "Roger Magalhães da Silva",
        "DataNascimento": "25091989"
    },
    {
        "CPF": "03520659581",
        "Nome": "Rosilene Ventura de Souza",
        "DataNascimento": "01071989"
    },
    {
        "CPF": "06715006865",
        "Nome": "Jorge Onodera",
        "DataNascimento": "19041966"
    },
    {
        "CPF": "05864687731",
        "Nome": "Susana Marrero Iglesias",
        "DataNascimento": "25101975"
    },
    {
        "CPF": "87242320410",
        "Nome": "Trícia Souto Santos",
        "DataNascimento": "31071972"
    },
    {
        "CPF": "01704794552",
        "Nome": "Pedro Germano dos Anjos",
        "DataNascimento": "18051985"
    },
    {
        "CPF": "01897901720",
        "Nome": "Gesil Sampaio Amarante Segundo",
        "DataNascimento": "02031971"
    },
    {
        "CPF": "01349454508",
        "Nome": "Rodolpho Santos Telles de Menezes",
        "DataNascimento": "11031985"
    },
    {
        "CPF": "01927967554",
        "Nome": "SIMONE SANTOS SOUZA",
        "DataNascimento": "26041986"
    },
    {
        "CPF": "11952176760",
        "Nome": "Thiago Vinícius Mantuano da Fonseca",
        "DataNascimento": "07111990"
    },
    {
        "CPF": "10812223799",
        "Nome": "Vitor Lacerda Vasquez",
        "DataNascimento": "04041981"
    },
    {
        "CPF": "71203095015",
        "Nome": "Marcio Gilberto Cardoso Costa",
        "DataNascimento": "15071973"
    },
    {
        "CPF": "03654810500",
        "Nome": "Naiara Maria Santana dos Santos Neves",
        "DataNascimento": "11121988"
    },
    {
        "CPF": "41788109520",
        "Nome": "carlos vitorio de oliveira",
        "DataNascimento": "14081967"
    },
    {
        "CPF": "10980263735",
        "Nome": "Marcelo dos Santos da Silva",
        "DataNascimento": "20071985"
    },
    {
        "CPF": "96927402500",
        "Nome": "VANESSA BARREIROS GONÇALVES",
        "DataNascimento": "30101978"
    },
    {
        "CPF": "71524320587",
        "Nome": "ANA CAROLINA ALVARES LAVIGNE",
        "DataNascimento": "25091975"
    },
    {
        "CPF": "01326793535",
        "Nome": "PRISCILA PEREIRA SUZART DE CARVALHO",
        "DataNascimento": "30091985"
    },
    {
        "CPF": "89810627572",
        "Nome": "Paulo Melo",
        "DataNascimento": "08111977"
    },
    {
        "CPF": "62312669587",
        "Nome": "Álvaro Vinicius de Souza Coelho",
        "DataNascimento": "05061971"
    },
    {
        "CPF": "22106071833",
        "Nome": "Nila Cecília de Faria Lopes Medeiros",
        "DataNascimento": "21051981"
    },
    {
        "CPF": "06151735510",
        "Nome": "Renato Gonçalves Peruzzo",
        "DataNascimento": "02021993"
    },
    {
        "CPF": "32123954861",
        "Nome": "Vinicius Augusto Takahashi Arakawa",
        "DataNascimento": "08061984"
    },
    {
        "CPF": "06412223517",
        "Nome": "Luciano Cardoso Santos",
        "DataNascimento": "23091996"
    },
    {
        "CPF": "03124122151",
        "Nome": "Ítala Paris de Souza",
        "DataNascimento": "19071990"
    },
    {
        "CPF": "03823536680",
        "Nome": "Rodrigo Camargo Aragão",
        "DataNascimento": "01101977"
    },
    {
        "CPF": "01958983543",
        "Nome": "BOUGLEUX BOMJARDIM DA SILVA CARMO",
        "DataNascimento": "18081983"
    },
    {
        "CPF": "98962485591",
        "Nome": "REJANE SANTOS BARRETO",
        "DataNascimento": "02021981"
    },
    {
        "CPF": "36317817847",
        "Nome": "Edson Aparecido Vieira Filho",
        "DataNascimento": "10091987"
    },
    {
        "CPF": "80604013515",
        "Nome": "Maria Medrado Nascimento",
        "DataNascimento": "28071980"
    },
    {
        "CPF": "22138041840",
        "Nome": "Aline Prado Atassio",
        "DataNascimento": "19091981"
    },
    {
        "CPF": "85350206591",
        "Nome": "MARIA ISABEL CARVALHO GONÇALVES",
        "DataNascimento": "23081984"
    },
    {
        "CPF": "92226329900",
        "Nome": "Paula Regina Siega",
        "DataNascimento": "12021974"
    },
    {
        "CPF": "31159039879",
        "Nome": "Leonardo Iusuti de Medeiros",
        "DataNascimento": "29121982"
    },
    {
        "CPF": "05785565536",
        "Nome": "Natasha dos Santos Lopes",
        "DataNascimento": "25091992"
    },
    {
        "CPF": "05911207982",
        "Nome": "Karla Furtado Andriani",
        "DataNascimento": "08101986"
    },
    {
        "CPF": "27876592848",
        "Nome": "CAMILA RIGHETTO CASSANO",
        "DataNascimento": "20041978"
    },
    {
        "CPF": "08634309967",
        "Nome": "Geórgia Camargo Góss",
        "DataNascimento": "18051992"
    },
    {
        "CPF": "82315035520",
        "Nome": "Danilo de Santana Nunes",
        "DataNascimento": "30111982"
    },
    {
        "CPF": "92658784520",
        "Nome": "Milena Duarte Lima",
        "DataNascimento": "08071978"
    },
    {
        "CPF": "02845841507",
        "Nome": "ICARO JOSE SANTOS RIBEIRO",
        "DataNascimento": "29021988"
    },
    {
        "CPF": "19273029434",
        "Nome": "CELI NELZA ZULKE TAFFAREL",
        "DataNascimento": "08101951"
    },
    {
        "CPF": "58863060568",
        "Nome": "ALINE SILVA",
        "DataNascimento": "25011973"
    },
    {
        "CPF": "74418114572",
        "Nome": "Verônica Alves dos Santos Conceição",
        "DataNascimento": "31011973"
    },
    {
        "CPF": "36374946553",
        "Nome": "Maria Margarete do Rosário Farias",
        "DataNascimento": "25101963"
    },
    {
        "CPF": "38396320802",
        "Nome": "Larissa Araujo Coutinho de Paula",
        "DataNascimento": "04081989"
    },
    {
        "CPF": "10308028821",
        "Nome": "Hamilton José Brumatto",
        "DataNascimento": "22092024"
    },
    {
        "CPF": "05605880896",
        "Nome": "RENATO FONTANA",
        "DataNascimento": "05081966"
    },
    {
        "CPF": "22877607844",
        "Nome": "Felix Mas Milian",
        "DataNascimento": "23111977"
    },
    {
        "CPF": "01989244530",
        "Nome": "Homero Chiaraba",
        "DataNascimento": "10061986"
    },
    {
        "CPF": "51304260534",
        "Nome": "Marcelo araújo",
        "DataNascimento": "23071965"
    },
    {
        "CPF": "26540673191",
        "Nome": "Ilka Miglio de Mesquita",
        "DataNascimento": "20081961"
    },
    {
        "CPF": "04619997579",
        "Nome": "Tamiles da Silva Oliveira",
        "DataNascimento": "18081989"
    },
    {
        "CPF": "07478439616",
        "Nome": "Natalia Silveira de Carvalho",
        "DataNascimento": "02021986"
    },
    {
        "CPF": "04621116444",
        "Nome": "DANIEL NICOLAU LIMA ALVES",
        "DataNascimento": "14051985"
    },
    {
        "CPF": "03512728529",
        "Nome": "Camilla Maria Torres Pinto",
        "DataNascimento": "15051993"
    },
    {
        "CPF": "94241708587",
        "Nome": "Jorge Lima de Oliveira Filho",
        "DataNascimento": "13091979"
    },
    {
        "CPF": "09003081417",
        "Nome": "Jéssica Barbosa da Silva do Nascimento",
        "DataNascimento": "08071991"
    },
    {
        "CPF": "06765962662",
        "Nome": "Rodrigo Felipe Santos",
        "DataNascimento": "08061988"
    },
    {
        "CPF": "07549956154",
        "Nome": "Uriel José Castellanos Aguirre",
        "DataNascimento": "09111987"
    },
   
    {
        "CPF": "03547681588",
        "Nome": "Alice de Moura Lima",
        "DataNascimento": "15081988"
    },
    {
        "CPF": "02251864547",
        "Nome": "Bruno Aguiar Santana",
        "DataNascimento": "08031994"
    },
    {
        "CPF": "02513221060",
        "Nome": "Fabiano Stefanello",
        "DataNascimento": "18121990"
    },
    {
        "CPF": "11243575646",
        "Nome": "Maíra dos Santos Costa",
        "DataNascimento": "18111992"
    },
    {
        "CPF": "03707783162",
        "Nome": "Raner José Santana Silva",
        "DataNascimento": "08071991"
    },
    {
        "CPF": "05613672563",
        "Nome": "Laio Andrade Sacramento",
        "DataNascimento": "23041994"
    },
    {
        "CPF": "06889768400",
        "Nome": "Stephanny Conceição Farias do Egito Costa",
        "DataNascimento": "31081989"
    },
    {
        "CPF": "35443309897",
        "Nome": "Juliana Stracieri",
        "DataNascimento": "21021986"
    },
    {
        "CPF": "32505761825",
        "Nome": "Thais Garcia da Silva",
        "DataNascimento": "10071984"
    },
    {
        "CPF": "04846529584",
        "Nome": "Grégory Alves Dionor",
        "DataNascimento": "16081993"
    },
    {
        "CPF": "05814390581",
        "Nome": "Raquel Vieira Niella",
        "DataNascimento": "24031995"
    },
    {
        "CPF": "71535160500",
        "Nome": "Carlos Henrique Leite Borges",
        "DataNascimento": "17091973"
    },
    {
        "CPF": "05007563501",
        "Nome": "Geovana Pires Araujo Lima",
        "DataNascimento": "19071994"
    },
    {
        "CPF": "97855561587",
        "Nome": "Aretusa de Oliveira Martins Bitencourt",
        "DataNascimento": "04031976"
    },
    {
        "CPF": "09897691600",
        "Nome": "Brunela Pereira da Silva",
        "DataNascimento": "28051990"
    },
    {
        "CPF": "02976160562",
        "Nome": "Paula Elisa Brandão Guedes",
        "DataNascimento": "26031987"
    },
    {
        "CPF": "46498060549",
        "Nome": "TIANE CLÉA SANTOS OLIVEIRA DIAS",
        "DataNascimento": "13031970"
    },
    {
        "CPF": "23146036568",
        "Nome": "FERNANDO JOSÉ REIS DE OLIVEIRA",
        "DataNascimento": "09041962"
    },
    {
        "CPF": "03778968530",
        "Nome": "Amanda Freitas Cerqueira",
        "DataNascimento": "29091990"
    },
    {
        "CPF": "01754457533",
        "Nome": "Hllytchaikra Ferraz Fehlberg",
        "DataNascimento": "14011982"
    },
    {
        "CPF": "86549568528",
        "Nome": "Fernando Enrique Grenno",
        "DataNascimento": "25121980"
    },
    {
        "CPF": "55898351515",
        "Nome": "João Paulo Ocke de Freitas",
        "DataNascimento": "14091969"
    },
    {
        "CPF": "05335998571",
        "Nome": "Rodrigo da Luz Silva",
        "DataNascimento": "22041993"
    },
    {
        "CPF": "04144814530",
        "Nome": "Franciele Brito Barbosa",
        "DataNascimento": "18101991"
    },
    {
        "CPF": "07526648674",
        "Nome": "Luciana Carvalho Lacerda",
        "DataNascimento": "29121985"
    },
    {
        "CPF": "04719567592",
        "Nome": "Nayara de Almeida Santos",
        "DataNascimento": "06051989"
    },
    {
        "CPF": "06756613588",
        "Nome": "Randra Kevelyn Barbosa Barros",
        "DataNascimento": "14071996"
    },
    {
        "CPF": "05997901645",
        "Nome": "Carla Santana Cassini",
        "DataNascimento": "02031983"
    },
    {
        "CPF": "22242600591",
        "Nome": "SORAYA DANTAS SANTIAGO DOS ANJOS",
        "DataNascimento": "30061961"
    },
    {
        "CPF": "05231704679",
        "Nome": "Kátia Michelle Freitas",
        "DataNascimento": "22031981"
    },
    {
        "CPF": "31135664870",
        "Nome": "Raphael Ricon de Oliveira",
        "DataNascimento": "16041983"
    },
    {
        "CPF": "00469287586",
        "Nome": "Roberto Santos de Carvalho",
        "DataNascimento": "09031982"
    },
    {
        "CPF": "84324198500",
        "Nome": "Tauan Lucas Amaral Brandão",
        "DataNascimento": "28061988"
    },
    {
        "CPF": "06339731570",
        "Nome": "José Carlos Aragão Santos",
        "DataNascimento": "07071996"
    },
    {
        "CPF": "00839777833",
        "Nome": "Vera Lucia Merlini",
        "DataNascimento": "26091960"
    },
    {
        "CPF": "05679839512",
        "Nome": "Jefferson Lira Santos",
        "DataNascimento": "11031993"
    },
    {
        "CPF": "02606636546",
        "Nome": "Eduardo Neves Rocha de Brito",
        "DataNascimento": "02011987"
    },
    {
        "CPF": "91101395591",
        "Nome": "Eliuse Sousa Silva",
        "DataNascimento": "11051974"
    },
    {
        "CPF": "07901142677",
        "Nome": "Geanne Carla Novais Pereira",
        "DataNascimento": "29101987"
    },
    {
        "CPF": "86978126586",
        "Nome": "Jorge Mario Herrera Lopera",
        "DataNascimento": "30101994"
    },
    {
        "CPF": "04155345501",
        "Nome": "MAIRA SOUZA MACHADO",
        "DataNascimento": "12061989"
    },
    {
        "CPF": "64648370520",
        "Nome": "Alciene Pereira da Silva",
        "DataNascimento": "15121974"
    },
    {
        "CPF": "04890354506",
        "Nome": "Miléia Santos Almeida",
        "DataNascimento": "26121990"
    },
    {
        "CPF": "01865648132",
        "Nome": "Jéssica Carneiro de Souza",
        "DataNascimento": "15111987"
    },
    {
        "CPF": "06257028400",
        "Nome": "Nathália Mattos Novaes da Rocha",
        "DataNascimento": "12031986"
    },
    {
        "CPF": "96384212587",
        "Nome": "ELISANGELA SILVA FARIAS",
        "DataNascimento": "24121980"
    },
    {
        "CPF": "07621325585",
        "Nome": "Vinícius de Oliveira Menezes Sirqueira",
        "DataNascimento": "13081998"
    },
    {
        "CPF": "06019657523",
        "Nome": "Rodrigo Barbosa Moreira",
        "DataNascimento": "29071995"
    },
    {
        "CPF": "06857895511",
        "Nome": "Brenda Leal Mota Santos",
        "DataNascimento": "18051995"
    },
    {
        "CPF": "10415158630",
        "Nome": "Pilar Louisy Maia Braga",
        "DataNascimento": "12031990"
    },
    {
        "CPF": "03215406543",
        "Nome": "Thiago Francisco de Souza",
        "DataNascimento": "31101985"
    },
    {
        "CPF": "01604057505",
        "Nome": "Tacio Vitor Duarte Simoes",
        "DataNascimento": "30011987"
    },
    {
        "CPF": "01712035770",
        "Nome": "Marta Magda Dornelles",
        "DataNascimento": "18081971"
    },
    {
        "CPF": "09241360658",
        "Nome": "Paloma Silva Resende",
        "DataNascimento": "23091992"
    },
    {
        "CPF": "04611666581",
        "Nome": "Herick Macedo Santos",
        "DataNascimento": "02051990"
    },
    {
        "CPF": "07288665607",
        "Nome": "Sagid Salles Ferreira",
        "DataNascimento": "15021985"
    },
    {
        "CPF": "03935351500",
        "Nome": "Ana Clara Correia Melgaço",
        "DataNascimento": "30041988"
    },
    {
        "CPF": "80928773000",
        "Nome": "Claudete Rejane Weiss",
        "DataNascimento": "14021977"
    },
    {
        "CPF": "03191446583",
        "Nome": "Gláucia Carvalho Barbosa Silva",
        "DataNascimento": "29061990"
    },
    {
        "CPF": "82530122504",
        "Nome": "Wagner Carvalho de Argolo Nobre",
        "DataNascimento": "24091981"
    },
    {
        "CPF": "96830026504",
        "Nome": "HELGA DULCE BISPO PASSOS",
        "DataNascimento": "07091979"
    },
    {
        "CPF": "00768698570",
        "Nome": "MARIANE OLIVEIRA COSTA SILVA",
        "DataNascimento": "25051984"
    },
    {
        "CPF": "03485777536",
        "Nome": "Maysa Santos Barbosa",
        "DataNascimento": "05051989"
    },
    {
        "CPF": "15474548818",
        "Nome": "Larissa Pinca Sarro Gomes",
        "DataNascimento": "16111972"
    },
    {
        "CPF": "26156830553",
        "Nome": "Maria do Rosário Andrade Barreto Ferreira",
        "DataNascimento": "02091961"
    },
    {
        "CPF": "02988371539",
        "Nome": "FILIPE CESAR DA HORA CARVALHO",
        "DataNascimento": "12091987"
    },
    {
        "CPF": "65825942572",
        "Nome": "Cristiane Aparecida de Cerqueira",
        "DataNascimento": "04041972"
    },
    {
        "CPF": "02291318594",
        "Nome": "Thais Marcelo Souza",
        "DataNascimento": "27121990"
    },
    {
        "CPF": "05002943136",
        "Nome": "José Victor Alves Ferreira",
        "DataNascimento": "19081994"
    },
    {
        "CPF": "01762651980",
        "Nome": "Eduardo Kowalski neto",
        "DataNascimento": "25042026"
    },
    {
        "CPF": "05994157546",
        "Nome": "Anderson Carvalho Vieira",
        "DataNascimento": "22081995"
    },
    {
        "CPF": "03594429512",
        "Nome": "Alex Vinicius Souza Araujo",
        "DataNascimento": "30091989"
    },
    {
        "CPF": "05574674548",
        "Nome": "Kevin Sacramento Vivas Neres",
        "DataNascimento": "12041993"
    },
    {
        "CPF": "04975471558",
        "Nome": "Patrícia Honório Silva Santos",
        "DataNascimento": "04121992"
    },
    {
        "CPF": "30312714831",
        "Nome": "Franciani Cássia Sentanin",
        "DataNascimento": "27071982"
    },
    {
        "CPF": "54055261500",
        "Nome": "Jémison Mattos dos Santos",
        "DataNascimento": "17121969"
    },
    {
        "CPF": "77755758591",
        "Nome": "Rosane Leite Funato",
        "DataNascimento": "08101980"
    },
    {
        "CPF": "04567559509",
        "Nome": "Grazielle da Mota Alcântara",
        "DataNascimento": "01071991"
    },
    {
        "CPF": "06689570690",
        "Nome": "Marianne Costa Oliveira",
        "DataNascimento": "23011983"
    }
]

# === Função para buscar dados da API
def consultar_dados(docente):
    url = 'https://www.stelaexperta.com.br/ws/totaiscv'
    headers = {'Content-Type': 'application/json'}
    payload = {
        "chave": "84030e4c-adf4-11ed-afa1-0242ac120002",
        "cpf": docente["CPF"],
        "nome": docente["Nome"],
        "dataNascimento": docente["DataNascimento"],
        "paisNascimento": "Brasil",
        "nacionalidade": "brasileira",
        "filtro": {"anoInicio": 2021, "anoFim": 2025},
        "downloadXml": 0
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json() if response.status_code == 200 else {}

# === Função para achatar JSON
def flatten_json(y):
    out = {}
    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], f'{name}{a}_')
        elif isinstance(x, list):
            if all(isinstance(i, (str, int, float)) for i in x):
                out[name[:-1]] = ', '.join(map(str, x))
        else:
            out[name[:-1]] = x
    flatten(y)
    return out

# === Upload do CSV com pesos/tipos
st.subheader("📄 Envie ou selecione a origem do arquivo de Pesos e Tipos")
origem_pesos = st.radio("📁 Origem dos Pesos e Tipos:", ["Arquivo enviado", "Cache local", "Github (online)"])

uploaded_file = None
if origem_pesos == "Arquivo enviado":
    uploaded_file = st.file_uploader("CSV com as colunas: Indicador, Peso, Tipo", type="csv")

if origem_pesos == "Arquivo enviado" and uploaded_file:
    pesos_df = pd.read_csv(uploaded_file)
elif origem_pesos == "Cache local" and Path("pesos_tipos_padrao.csv").exists():
    pesos_df = pd.read_csv("pesos_tipos_padrao.csv")
elif origem_pesos == "Github (online)":
    url_remoto = "https://raw.githubusercontent.com/fbrunoso/barema/refs/heads/main/pesos_tipos.csv"
    pesos_df = pd.read_csv(url_remoto)
else:
    st.error("❌ Nenhuma fonte válida de pesos disponível. Envie um arquivo ou selecione outra opção.")
    st.stop()

# Limpeza e tratamento
pesos_df.columns = pesos_df.columns.str.strip().str.lower()
pesos_df["tipo"] = pd.to_numeric(pesos_df["tipo"], errors="coerce").fillna(0).astype(int).astype(str)
pesos_df["peso"] = pd.to_numeric(pesos_df["peso"], errors="coerce").fillna(0)

# Inicializa os dicionários
pesos = dict(zip(pesos_df["indicador"], pesos_df["peso"]))
tipos = dict(zip(pesos_df["indicador"], pesos_df["tipo"]))

# Interface retraída para edição manual
with st.expander("🔧 Ajustar manualmente pesos e tipos (opcional)"):
    opcoes_tipo = ["0", "1", "2", "3"]
    for _, row in pesos_df.iterrows():
        indicador = row["indicador"]
        col1, col2 = st.columns([0.6, 0.4])
        with col1:
            pesos[indicador] = st.number_input(f"Peso - {indicador}", value=float(pesos[indicador]), step=0.1, key=f"peso_{indicador}")
        with col2:
            tipo_padrao = tipos[indicador] if tipos[indicador] in opcoes_tipo else "0"
            tipos[indicador] = st.radio(
                f"Tipo - {indicador}", options=opcoes_tipo,
                index=opcoes_tipo.index(tipo_padrao), horizontal=True, key=f"tipo_{indicador}"
            )

# === Busca dados da API
st.subheader("🔍 Coleta de Dados da API")
campos_presentes = set()
linhas = []
for docente in dados_docentes:
    with st.spinner(f"Buscando dados para {docente['Nome'].capitalize()}..."):
        dados = consultar_dados(docente)
        flat = flatten_json(dados)
        campos_presentes.update(flat.keys())
        flat["Nome"] = docente["Nome"].capitalize()
        linhas.append(flat)

df = pd.DataFrame(linhas)
for campo in campos_presentes:
    if campo not in df.columns:
        df[campo] = 0
df = df.fillna(0)
colunas_ordenadas = ["Nome"] + [c for c in df.columns if c != "Nome"]
df = df[colunas_ordenadas]

st.success("✅ Planilha gerada com sucesso!")

# === Cálculo robusto
df_resultado = df.copy()
if st.button("🧲 Calcular Pontuação"):
    indicadores_validos = list(set(df.columns) & set(pesos.keys()))

    st.subheader("🧪 Diagnóstico de Indicadores")
    st.markdown(f"- 🔢 **Indicadores no DataFrame**: `{len(df.columns)}`")
    st.markdown(f"- 🎯 **Indicadores no CSV**: `{len(pesos)}`")
    st.markdown(f"- ✅ **Indicadores utilizados no cálculo**: `{len(indicadores_validos)}`")

    def calcular_pontuacao(row):
        total = 0
        for col in indicadores_validos:
            valor = pd.to_numeric(row[col], errors="coerce")
            valor = 0 if pd.isna(valor) else float(valor)
            peso = float(pesos.get(col, 0))
            total += valor * peso
        return total

    df_resultado["Pontuação Total"] = df_resultado.apply(calcular_pontuacao, axis=1)

    st.subheader("📈 Pontuação Final por Docente")
    st.dataframe(df_resultado[["Nome", "Pontuação Total"]].sort_values(by="Pontuação Total", ascending=False), use_container_width=True)

    tipo_totais = []
    for tipo in ["1", "2", "3"]:
        tipo_cols = [k for k, v in tipos.items() if v == tipo and k in df_resultado.columns]
        if tipo_cols:
            tipo_label = f"Tipo {tipo} Total"
            df_resultado[tipo_label] = df_resultado[tipo_cols].apply(
                lambda row: sum(
                    pd.to_numeric(row[col], errors="coerce") * float(pesos.get(col, 0))
                    if pd.notna(pd.to_numeric(row[col], errors="coerce")) else 0
                    for col in tipo_cols
                ), axis=1
            )
            tipo_totais.append(tipo_label)

    if tipo_totais:
        st.subheader("📁 Totais por Tipo")
        cols_to_show = ["Nome"] + tipo_totais + ["Pontuação Total"]
        st.dataframe(df_resultado[cols_to_show].sort_values(by="Pontuação Total", ascending=False), use_container_width=True)
    else:
        st.info("ℹ️ Nenhum tipo relevante foi definido.")

    st.subheader("📄 Exportar Resultados")
    pesos_export = pd.DataFrame({
        "Indicador": list(pesos.keys()),
        "Peso": [pesos[k] for k in pesos.keys()],
        "Tipo": [tipos[k] for k in tipos.keys()]
    })

    st.download_button("📁 Baixar pesos e tipos (CSV)", data=pesos_export.to_csv(index=False).encode('utf-8'),
                       file_name="pesos_tipos_atualizado.csv", mime="text/csv")

    towrite = BytesIO()
    with pd.ExcelWriter(towrite, engine='xlsxwriter') as writer:
        df_resultado.to_excel(writer, index=False, sheet_name="Produção Completa")
        pesos_export.to_excel(writer, index=False, sheet_name="Pesos e Tipos")
    towrite.seek(0)

    st.download_button(
        "📅 Baixar Excel com toda a produção",
        towrite,
        file_name="producao_uesc_completa.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
