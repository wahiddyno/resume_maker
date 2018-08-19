console.log("linked");
var doc = new jsPDF();
$('#btn').click(function () {
    doc.fromHTML($('body').html(), 15, 15);
    doc.save('sample-file.pdf');
});
