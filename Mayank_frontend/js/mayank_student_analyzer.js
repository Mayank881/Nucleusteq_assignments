// add the data structure for the program calculation.
const students = [
    {
        name: "Lalit",
        marks: [
            { subject: "Math", score: 78 },
            { subject: "English", score: 82 },
            { subject: "Science", score: 74 },
            { subject: "History", score: 69 },
            { subject: "Computer", score: 88 }
        ],
        attendance: 82
    },
    {
        name: "Rahul",
        marks: [
            { subject: "Math", score: 90 },
            { subject: "English", score: 85 },
            { subject: "Science", score: 80 },
            { subject: "History", score: 76 },
            { subject: "Computer", score: 92 }
        ],
        attendance: 91
    },
    {
        name: "Aman",
        marks: [
            { subject: "Math", score: 50 },
            { subject: "English", score: 55 },
            { subject: "Science", score: 60 },
            { subject: "History", score: 58 },
            { subject: "Computer", score: 62 }
        ],
        attendance: 70
    }
];

// This function calculates total marks of a student by looping through subjects

function getTotalMarks(student) {
  let total = 0;

  for (let i = 0; i < student.marks.length; i++) {
      total += student.marks[i].score;
  }

  return total;
}

console.log("Total Marks:");
students.forEach(s => {
  console.log(`${s.name} Total Marks: ${getTotalMarks(s)}`);
});
//
// Printing total marks for each student 
function getAverageMarks(student) {
  let total = getTotalMarks(student);
  return total / student.marks.length;
}

// I reused total marks function to calculate average marks by dividing total marks by number of subjects.
function getAverageMarks(student) {
  let total = getTotalMarks(student);
  return total / student.marks.length;
}
console.log("\nAverage Marks:");
// Printing average marks
students.forEach(s => {
  console.log(s.name + " Average:", getAverageMarks(s).toFixed(2));
});


console.log(" \nHighest Scorers in each Subject:");
// This function finds highest scorer in each subject
function getHighestBySubject() {
  let subjects = ["Math", "English", "Science", "History", "Computer"];

  for (let sub of subjects) {
    let maxScore = 0;
    let topper = "";

    for (let student of students) {
      for (let mark of student.marks) {
        if (mark.subject === sub && mark.score > maxScore) {
          maxScore = mark.score;
          topper = student.name;
        }
      }
    }

    console.log(`Highest in ${sub}: ${topper} (${maxScore})`);
  }
}

getHighestBySubject();