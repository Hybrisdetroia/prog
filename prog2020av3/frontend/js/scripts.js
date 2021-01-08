$(function() {

  function exibirComputadores() {
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
      $("#corpoTabelaComputadores").empty();

      mostrarConteudo("tabelaComputadores");

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
  }


  function mostrarConteudo(conteudo) {
    $("#tabelaComputadores").addClass("d-none");
    $("#conteudoInicial").addClass("d-none");

    $(`#${conteudo}`).removeClass("d-none");
  }


  $(document).on("click", "#listarComputadores", function() {
    exibirComputadores();
  });


  $(document).on("click", "#inicio", function() {
    mostrarConteudo("conteudoInicial");
  });


  $(document).on("click", "#btIncluirComputador", function() {
    processador = $("#campoProcessador").val();
    ram = $("#campoRAM").val();
    memoria = $("#campoMemoria").val();
    fonte = $("#campoFonte").val();

    var dados = JSON.stringify({ processador, ram, memoria, fonte });

    $.ajax({
      url: 'http://localhost:5000/incluir_computador',
      type: 'POST',
      dataType: 'json',
      contentType: 'application/json',
      data: dados,
      success: incluirComputador,
      error: erroAoIncluir
    });


    function incluirComputador(retorno) {
      if (retorno.resultado === "ok") {
        alert("Computador incluído com sucesso!");

        $("#campoProcessador").val("");
        $("#campoRAM").val("");
        $("#campoMemoria").val("");
        $("#campoFonte").val("");
      } else {
        alert(`${retorno.resultado}: ${retorno.detalhes}`);
      }
    }


    function erroAoIncluir (retorno) {
      alert(`Erro! ${retorno.resultado}: ${retorno.detalhes}`);
    }
  });


  $('#modalIncluirComputadores').on('hide.bs.modal', function (e) {
    if (!$("#tabelaComputadores").hasClass('d-none')) {
      exibirComputadores();
    }
  });

  mostrarConteudo("conteudoInicial");

});