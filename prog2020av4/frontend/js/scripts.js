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

      for (var computador of computadores) {
        linha = `<tr id="linha_${computador.id}">
          <td>${computador.processador}</td>
          <td>${computador.ram}</td>
          <td>${computador.memoria}</td>
          <td>${computador.fonte}</td>
          <td>
            <a href="#" id="${computador.id}" class="excluir_computador">
              <svg xmlns="http://www.w3.org/2000/svg"
                width="32" height="32"
                fill="#F00"
                class="bi bi-x" viewBox="0 0 16 16">
                <path
                  fill-rule="evenodd"
                  d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"
                />
              </svg>
            </a>
          </td>
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

  $(document).on("click", ".excluir_computador", function() {
    var idComputador = $(this).attr("id");

    $.ajax({
      url: `http://localhost:5000/excluir_computador/${idComputador}`,
      type: "DELETE",
      dataType: 'json',
      success: excluirComputador,
      error: erroAoExcluir
    });

    function excluirComputador(retorno) {
      if (retorno.resultado === "ok") {
        $(`#linha_${idComputador}`).fadeOut();
      } else {
        alert(`ERROR: ${retorno.resultado}: ${retorno.detalhes}`);
      }
    }

    function erroAoExcluir(retorno) {
      alert("Erro no back-end");
    }
  });

  mostrarConteudo("conteudoInicial");

});