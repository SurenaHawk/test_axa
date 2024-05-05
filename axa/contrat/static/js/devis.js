$(document).ready(function() {

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

    CKEDITOR.replace('operation_description');
});
