const questions = [
    {
        question: "Q1",
        answers: [
            { text: "O1"},
            { text: "O2"},
            { text: "O3"},
        ]
    },
    
    {
        question: "Q2",
        answers: [
            { text: "O1"},
            { text: "O2"},
            { text: "O3"},
        ]
    },

    {
        question: "Q3",
        answers: [
            { text: "O1"},
            { text: "O2"},
            { text: "O3"},
        ]
    },

    {
        question: "Q4",
        answers: [
            { text: "O1"},
            { text: "O2"},
            { text: "O3"},
        ]
    },

    {
        question: "Q5",
        answers: [
            { text: "O1"},
            { text: "O2"},
            { text: "O3"},
        ]
    },

    {
        question: "Q6",
        answers: [
            { text: "O1"},
            { text: "O2"},
            { text: "O3"},
        ]
    },

    {
        question: "Q7",
        answers: [
            { text: "O1"},
            { text: "O2"},
            { text: "O3"},
        ]
    },
];

const questionElement = document.getElementById("question");
const answerButtons = document.getElementById("answer-buttons");
const nextButton = document.getElementById("next-btn");

let currentQuestionIndex = 0;
let score = 0;

function startQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    nextButton.innerHTML = "Next";
    showQuestion();
}

function showQuestion() {
    resetState();
    const currentQuestion = questions[currentQuestionIndex];
    questionElement.innerText = currentQuestion.question;

    currentQuestion.answers.forEach((answer) => {
        const button = document.createElement("button");
        button.innerText = answer.text;
        button.classList.add("btn");
        button.addEventListener("click", () => selectAnswer(answer));
        answerButtons.appendChild(button);
    });
}

function resetState() {
    while (answerButtons.firstChild) {
        answerButtons.removeChild(answerButtons.firstChild);
    }
}

function selectAnswer(answer) {
    if (answer.correct) {
        score++;
    }

    Array.from(answerButtons.children).forEach((button) => {
        button.disabled = true;
        if (answer.correct) {
            button.classList.add("correct");
        } else {
            button.classList.add("incorrect");
        }
    });

    const selectedButton = event.target;
    selectedButton.classList.add("selected");

    nextButton.style.display = "block";
}

function showScore() {
    resetState();
    questionElement.innerText = "Here is your itinerary";
    nextButton.innerText = "Try again";
    nextButton.style.display = "block";
}

function handleNextButton() {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        showQuestion();
    } else {
        showScore();
    }
}

nextButton.addEventListener("click", () => {
    if (currentQuestionIndex < questions.length) {
        handleNextButton();
    } else {
        startQuiz();
    }
});

startQuiz();
