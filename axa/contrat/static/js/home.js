$(document).ready(function() {
    $('#projets_table').DataTable({
        language: {
            url: "https://cdn.datatables.net/plug-ins/1.12.0/i18n/fr-FR.json"
        }
    });

    $('table').on('click', '.download_icon', function(event) {
        event.preventDefault();
        var type = $(this).data('type');
        var opportunity_number = $(this).closest('tr').find('td:first').text();
        window.location.href = '/download_'+type+'/?opportunity_number=' + encodeURIComponent(opportunity_number);
    });
});
