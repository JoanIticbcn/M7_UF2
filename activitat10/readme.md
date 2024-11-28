<h1>Activitat 10 Postgres</h1>
<h4>Creació i insercio dels registres a la taula</h4>
<p>Per començar he creat una taula buida a postgres de nom act10 en la que hi ha 2 columnes de name una de NOM i una de THEME.</p>
<img src="captures/taulabuida.png">
<p>Despres d'executar el script csvToPostgres.py la taula ja s'ha emplenat completament i correctament amb totes les dades de forma correcta. Captura a continuació.</p>
<img src="captures/taulaplena.png">

<h4>Documentacio dels metodes fastAPI<h4>
<p>El primer metode de la API es el opcions tematica que el que fa es retornarte totes les opcions de tematica uniques dispoibles. La sortida de dades esta serialitzada amb el readOptions schema i amb el readOptions fem la consulta SQL a la taula postgres i la retornem</p>
<img src="captures/opcions.png">
<p>El segon metode de la API es el getWord que et retorna una paraula aleatoria de una tematica que be donada com a path parametre de la API. Al igual que l'altre metode les dades es serialitzen amb el WordSchema i la consulta SQL es fa amb el readWord</p>
<img src="captures/word.png">