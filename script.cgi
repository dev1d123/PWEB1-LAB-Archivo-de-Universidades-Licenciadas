#!"C:/xampp/perl/bin/perl.exe"
use strict;
use warnings;
use CGI;
use Text::CSV;
use utf8;
my $cgi = CGI->new;

my $nombreUni    = $cgi->param('nombreUniversidad');
my $periodoLic   = $cgi->param('periodoLicenciamiento');
my $depLocal     = $cgi->param('departamentoLocal');
my $denoProg     = $cgi->param('denominacionPrograma');
utf8::decode($nombreUni );
utf8::decode($periodoLic );
utf8::decode($depLocal );
utf8::decode($denoProg );

my $archivo = 'ProgramasdeUniversidades.csv';
open my $fh, '<', $archivo;

my $csv = Text::CSV->new({ binary => 1, sep_char => '|' });

my $tableKey = "";
if (my $fila = $csv->getline($fh)) {
    for my $valor (@$fila) {
        $tableKey .= "<th>$valor</th>\n";
    }
}

my $tableValues = "";
my $coincidencias1 = 0;
my $coincidencias2 = 0;
my $coincidencias3 = 0;
my $coincidencias4 = 0;
my $coincidenciasTotales = 0;

while (my $fila = $csv->getline($fh)) {
    if (($fila->[1] eq $nombreUni ) && ($fila->[4] eq $periodoLic ) &&($fila->[10] eq $depLocal ) &&($fila->[16] eq $denoProg )) {
        $tableValues .= "<tr>";
        for my $valor (@$fila) {
            $tableValues .= "<td>$valor</td>\n";
        }
        $tableValues .= "</tr>";
        $coincidenciasTotales++;
    }
    if ($fila->[1] eq $nombreUni ) {
        $coincidencias1++;
    }
    if ($fila->[4] eq $periodoLic) {
        $coincidencias2++;
    }
    if ($fila->[10] eq $depLocal ) {
        $coincidencias3++;
    }
    if ($fila->[16] eq $denoProg) {
        $coincidencias4++;
    }
}
if($coincidenciasTotales == 0){
    $coincidenciasTotales = "No existen valores que cumplan con los campos"
}else{
    $coincidenciasTotales = "Existen $coincidenciasTotales coincidencias de todos los campos"
}

close $fh;

print $cgi->header('text/html');

print <<HTML;
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Resultados Búsqueda</title>
    <style>
        body {
            background-color: red;
            color: yellow;
        }

        h1, h2 {
            color: black;
            font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;

        }

        table {
            border-collapse: collapse;
            width: 100%;

        }

        table, th, td {
            border: 0.4rem solid yellow;
            box-shadow: 10px 10px 10px rgba(0, 0, 0, 0.3);
        }
        tr:nth-child(1) {
            color: black;
            background-color: orange;
        }
        tr:not(:first-child) {
            color: yellow;
            font-weight: bold;
        } 
        th, td {
            padding: 0.7rem;
            text-align: center;
        }

        form {
            margin-top: 20px;
        }
        table tr{
            font-size: 0.7rem;
        }
        input[type="submit"] {
            background-color: orange;
            color: black;
            font-size: 2rem;
            font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
            padding: 10px 20px;
            border: 1rem black collapse;
            cursor: pointer;
            display: block;
            margin-left: 40%;
            transition: background-color 0.3s;
        }

        input[type="submit"]:hover {
            background-color: yellow;
        }
    </style>
</head>
<body>
    <h1>Parámetros seleccionados</h1>
    <h2>Nombre de universidad: $nombreUni >>>>> Existen $coincidencias1 coincidencias</h2>
    <h2>Periodo de Licenciamiento: $periodoLic >>>>> Existen $coincidencias2 coincidencias</h2>
    <h2>Departamento Local: $depLocal >>>>> Existen $coincidencias3 coincidencias</h2>
    <h2>Denominación Programa: $denoProg >>>>> Existen $coincidencias4 coincidencias</h2>
    <h2>$coincidenciasTotales</h2>
    <h1>Resultados de la Búsqueda</h1>
    <table>
        <tr>$tableKey</tr>
        $tableValues
    </table>

    <form action="index.html">
        <input type="submit" value="Regresar al buscador">
    </form>
</body>
</html>
HTML
