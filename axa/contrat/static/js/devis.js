$(document).ready(function() {

    // Ajout du module wysimig
    CKEDITOR.replace('operation_description');

    // Cacher les champs au début
    $(".hidden_fields").hide();
    $("#validate_devis_form").hide();
    
    $("#continue_button").click(function() {
        let inputValue = $("#opportunity_number").val();
        if (inputValue.trim() !== '') {
            $(".hidden_fields").show();
            $("#validate_devis_form").show();
            $("#continue_button").hide();
        }
    });

    $(".inputs_number").on("input", function() {
        var new_input_without_characters = $(this).val().replace(/[^0-9]/g, '');
        $(this).val(new_input_without_characters);
    });

    calculateTotal()

    // Fonction pour calculer la somme et l'afficher dans la troisième colonne
    function calculateTotal() {
        var tableRows = document.querySelectorAll('#excel_table tbody tr');
        tableRows.forEach(function(row) {
            var columns = row.querySelectorAll('td');
            var itemValue = parseFloat(columns[0].innerText.trim()) || 0;
            var quantityValue = parseFloat(columns[1].innerText.trim()) || 0;
            var totalValue = itemValue + quantityValue;
            columns[2].innerText = totalValue.toFixed(2);
        });
    }

    // Appeler la fonction calculateTotal lorsque le contenu de la première ou de la deuxième colonne change
    document.getElementById('excel_table').addEventListener('input', calculateTotal);

    // Fonction pour sauvegarder les données
    $("#validate_devis_form").click(function (event){
        event.preventDefault();
        var form_data = new FormData();
        var opportunity_number = $("#opportunity_number").val();
        var reference = $("#reference").val();
        var siret_number = $("#siret_number").val();
        var siren_number = $("#siren_number").val();
        var affaire = $("#affaire").val();
        var client_name = $("#client_name").val();
        var intermediaire = $("#intermediaire").val();
        var short_description = $("#short_description").val();
        var image_description = $("#image_description")[0].files[0];
        var is_checked = $("#coassurance").prop("checked");
        var coassurance = is_checked ? true:false;
        var operation_adresse = $("#operation_adresse").val();
        var plan_operation = $("#plan_operation")[0].files;
        for (var i = 0; i < plan_operation.length; i++){
            form_data.append('plan_operation', plan_operation[i]);
        }
        var operation_description = $("#operation_description").val();
        var tarif = $("#excel_table tbody tr:last td:last").text().trim();
        form_data.append('opportunity_number', opportunity_number)
        form_data.append('reference', reference)
        form_data.append('siret_number', siret_number)
        form_data.append('siren_number', siren_number)
        form_data.append('affaire', affaire)
        form_data.append('client_name', client_name)
        form_data.append('intermediaire', intermediaire)
        form_data.append('short_description', short_description)
        form_data.append('image_description', image_description)
        form_data.append('coassurance', coassurance)
        form_data.append('operation_adresse', operation_adresse)
        form_data.append('plan_operation', plan_operation)
        form_data.append('operation_description', operation_description)
        form_data.append('tarif', tarif)
        $.ajax({
            url: '/devis/',
            type: 'POST',
            dataType: 'json',
            processData: false,  
            contentType: false,
            data: form_data,
            success: function(response) {

            },
        });
    });
});
