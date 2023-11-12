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

my $archivo = 'C:\xampp\htdocs\ProgramasdeUniversidades.csv';
open my $fh, '<', $archivo;

my $csv = Text::CSV->new({ binary => 1, sep_char => '|' });

my $tableKey = "";
if (my $fila = $csv->getline($fh)) {
    for my $valor (@$fila) {
        $tableKey .= "<th>$valor</th>\n";
    }
}

my $tableValues = "";
my $v = "";
while (my $fila = $csv->getline($fh)) {
    $v .= $fila->[16];
    if (($fila->[1] eq $nombreUni ) && ($fila->[4] eq $periodoLic ) &&($fila->[10] eq $depLocal ) &&($fila->[16] eq $denoProg )) {
        $tableValues .= "<tr>";
        for my $valor (@$fila) {
            $tableValues .= "<td>$valor</td>\n";
        }
        $tableValues .= "</tr>";
    }
}


close $fh;

print $cgi->header('text/html');

print <<HTML;
<!DOCTYPE html>
<html lang = "es">
<head>
    <meta charset="UTF-8">
    <title>Resultados Busqueda</title>
</head>
<body>
    <h1>Parametros seleccionados</h1>
    <h2>Nombre de universidad: $nombreUni<h2>
    <h2>Periodo de Licenciamiento: $periodoLic<h2>
    <h2>Departamento Local: $depLocal<h2>
    <h2>Denominacion Programa: $denoProg<h2>
    <h1>Resultados de la Busqueda</h1>
    <table border="1">
        <tr>$tableKey</tr>
        $tableValues
    </table>
</body>
</html>
HTML