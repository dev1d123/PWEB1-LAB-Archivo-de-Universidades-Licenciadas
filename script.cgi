#!"C:/xampp/perl/bin/perl.exe"
use strict;
use warnings;
use CGI;
use Text::CSV;
my $cgi = CGI->new;
print $cgi->header("text/html");

# Parámetros del formulario
my $nombreUni = $cgi->param('nombreUniversidad');
my $periodoLic = $cgi->param('periodoLicenciamiento');
my $depLocal = $cgi->param('departamentoLocal');
my $denoProg = $cgi->param('denominacionPrograma');

#Abrir el archivo csv
my $archivo= 'C:\xampp\htdocs\ProgramasdeUniversidades.csv';  

#Creamos un objeto de la clase Text::CSV con el contructor, le indicamos los parametros correspondientes.
my $csv = Text::CSV->new({ binary => 1, sep_char => '|' });

# Abrir el archivo CSV en modo lectura (<), mediante el identificador $fh
open my $fh, '<', $archivo;

#El codigo CGI generara una tabla con todos los valores que cumplan con las condiciones indicadas por los parametros.
#Lo primero a hacer es crear los encabezados y en HTML los encabezados de tabla tienen la siguiente forma: <th>Valor</th>

my $tableKey = "";
if (my $fila = $csv->getline($fh)) {
    my $cadena = join(', ', @$fila);
    for my $valor (@$fila) {
        $tableKey .= "<th>$valor</th>\n";
    }
}

# Cerrar el archivo
close $fh;


