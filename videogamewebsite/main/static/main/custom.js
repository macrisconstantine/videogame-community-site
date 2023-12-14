$(document).ready(function () {
    // Attach a click event to each star
    $('.star').on('click', function () {
        var rating = $(this).data('value');
        var gameId = $(this).data('game-id');
        console.log("hello");

        // Make an AJAX request to your rate_game view
        $.ajax({
            type: 'GET',
            url: `/rate_game/${gameId}/${rating}/`,
            success: function (data) {
                // Update the display with the new average rating
                $('p#average-rating').text(`Average Rating: ${data.average_rating}`);
                $('p#total-ratings').text(`Total Ratings: ${data.total_ratings}`);
                updateStars(clickedStar);
                location.reload();

                // Update the clicked star and previous stars
            },
            error: function () {
                console.error('Failed to rate the game.');
            }
        });

        
    });

     // Function to update stars based on the clicked star
    function updateStars(clickedStar) {
        // Reset all stars to default state
        $('.star').removeClass('fas').addClass('far');
        console.log("hello");
        // Set the clicked star and previous stars to filled
        clickedStar.prevAll('.star').addBack().removeClass('far').addClass('fas');
    }
});