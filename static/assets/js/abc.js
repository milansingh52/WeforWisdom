// tutor home
$(document).ready(function () {
    // Define a mapping of categories to subjects
    const subjects = {
        choose: ['Choose Subject'],
        grade_1_to_5: ['Computers', 'English', 'General Knowledge', 'Health Education', 'Mathematics', 'Nepali', 'Social Studies', 'Optional Maths', 'Science'],
        grade_6_to_10: ['Computers', 'English', 'General Knowledge', 'Health Education', 'Mathematics', 'Nepali', 'Social Studies', 'Optional Maths', 'Science'],
        programming: ["Java", "Python", "C", "C++", "HTML", "CSS", "C#"],
        languages: ["English", "Spanish", "French", "German"],
        dancing: ["Ballet", "Ballroom", "Contemporary", "Hip Hop", "Folk Dance", "Cultural Dance"],
        yoga: ["Karma Yoga", "Bhakti Yoga", "Rāja Yoga", "Jñāna Yoga"],

    };

    // Function to populate the subject dropdown based on the selected category
    $("#category").change(function () {
        const selectedCategory = $(this).val();
        const subjectDropdown = $("#subject");

        // Clear previous options
        subjectDropdown.empty();

        // Populate options based on the selected category
        subjects[selectedCategory].forEach(function (subject) {
            subjectDropdown.append(`<option value="${subject}">${subject}</option>`);
        });
    });

    // Trigger the change event to populate the subject dropdown initially
    $("#category").trigger("change");
});

// ------------------------------------------------------------------------------------------------------

// Filter Tutor



// To access the stars
let stars = document.getElementsByClassName("star");
let output = document.getElementById("output");
let v = document.getElementById('value');

// Funtion to update rating
function gfg(n) {
    remove();
    for (let i = 0; i < n; i++) {
        if (n == 1) {
            cls = "one";
            v.value = 1;
        }
        else if (n == 2) {
            cls = "two";
            v.value = 2;
        }
        else if (n == 3) {
            cls = "three";
            v.value = 3;
        }
        else if (n == 4) {
            cls = "four";
            v.value = 4;
        }
        else if (n == 5) {
            cls = "five";
            v.value = 5;
        }
        stars[i].className = "star " + cls;
    }
    output.innerText = "Rating is: " + n + "/5";
}

// To remove the pre-applied styling
function remove() {
    let i = 0;
    while (i < 5) {
        stars[i].className = "star";
        i++;
    }
}