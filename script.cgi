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

# Leer e imprimir la primera fila del archivo CSV
while (my $fila = $csv->getline($fh)) {
    print @$fila, "\n";
    my $cadena = join(', ', @$fila);
}
# Cerrar el archivo
close $fh;


