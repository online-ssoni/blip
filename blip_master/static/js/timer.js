document.addEventListener("DOMContentLoaded", () => {
    const timerDivs = document.querySelectorAll(".timer p  span");

    const timeStamps = Array.from(timerDivs).map(timer => {
        timeStr = timer.innerText.trim()
        console.log(timeStr)
        times = new Date(timeStr).toString()
        console.log(times)
        timeDate = new Date(times).getTime()
        return timeDate
    })
    const x = setInterval(timer, 1000);
    function timer() {

        const allTimes = timeStamps.map(getEventTime)
        const timerObject = [...timerDivs].map((div,i) => {
            return { target:div, time:allTimes[i]}
        })
        timerObject.forEach(obj => {
            obj.target.innerText = obj.time;
            if(obj.time === "Live Now") {
                obj.target.parentElement.parentElement.classList.remove("timer")
                obj.target.parentElement.parentElement.classList.add("live")

            }

        })
    }

    function getEventTime(timeStamp) {
        let now = new Date().getTime();
        const countDownDate = timeStamp

        let distance = countDownDate - now;
        let days = Math.floor(distance / (1000 * 60 * 60 * 24));
        let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        let seconds = Math.floor((distance % (1000 * 60)) / 1000);
        let showTime = `Starts In : ${days} d ${hours} h ${minutes} m ${seconds} s`;
        if(distance < 0) {
            return "Live Now"
        }
        return showTime
    }
});