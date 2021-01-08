$(function() {
  $.ajax({
      url: 'http://localhost:5000/listar_computadores',
      method: 'GET',
      dataType: 'json',
      success: listarComputadores,
      error: function() {
          alert("Erro no backend!");
      }
  });

  function listarComputadores(computadores) {
      for (var computadore of computadores) {
          linha = `<tr>
            <td>${computadore.processador}</td>
            <td>${computadore.ram}</td>
            <td>${computadore.memoria}</td>
            <td>${computadore.fonte}</td>
            </tr>`;

          $('#corpoTabelaComputadores').append(linha);
      }
  }
});