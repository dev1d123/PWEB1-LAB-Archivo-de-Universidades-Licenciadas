#!"C:/xampp/perl/bin/perl.exe"
use strict;
use warnings;
use CGI;
use Text::CSV;

my $cgi = CGI->new;

# Parámetros del formulario
my $nombreUni    = $cgi->param('nombreUniversidad');
my $periodoLic   = $cgi->param('periodoLicenciamiento');
my $depLocal     = $cgi->param('departamentoLocal');
my $denoProg     = $cgi->param('denominacionPrograma');

# Abrir el archivo CSV en modo lectura (<)
my $archivo = 'C:\xampp\htdocs\ProgramasdeUniversidades.csv';
open my $fh, '<', $archivo;

# Crear un objeto de la clase Text::CSV con el constructor
my $csv = Text::CSV->new({ binary => 1, sep_char => '|' });

# Crear los encabezados de la tabla
my $tableKey = "";
if (my $fila = $csv->getline($fh)) {
    for my $valor (@$fila) {
        $tableKey .= "<th>$valor</th>\n";
    }
}

# Iniciar la construcción de la tabla HTML
my $tableValues = "";
my $v = "";
# Procesar las filas del archivo CSV
while (my $fila = $csv->getline($fh)) {
    $v .= $fila->[16];
    if (($fila->[16] eq $denoProg)) {
        $tableValues .= "<tr>";
        for my $valor (@$fila) {
            $tableValues .= "<td>$valor</td>\n";
        }
        $tableValues .= "</tr>";
    }
}

# Cerrar el archivo CSV
close $fh;

# Imprimir el documento HTML con la tabla de resultados
print $cgi->header('text/html');
print <<HTML;
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Resultados Busqueda</title>
</head>
<body>
    <h1>Resultados de la Busqueda</h1>
    <table border="1">
        <tr>$tableKey</tr>
        $tableValues
    </table>
</body>
</html>
HTML