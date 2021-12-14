//var startingAmount = starting gold amount
// sent in from flask

//var targetAmount = end of day gold amount
// sent in from flask

//var accumulatedChange = amount of todayys change that has already occurred.
// sent in from flask

//var secondsUntilUpdate = seconds until we should reach the targetAmount of gold
// sent in from flask
var currentGold;

if(changePerSecond <0){
    changePerSecond = 90000
}

//This script should determine how much gold should be displayed between those two and tick up if needed
let gold = document.getElementById("goldCounter");
gold.innerHTML = numberWithCommas(Math.round(startingAmount));
currentGold = startingAmount;

var interval = setInterval(countGold, 1000);


var bonds = document.getElementById("num-bonds");
var bondPrice = 5000000;

var twistedBows = document.getElementById("num-twisted-bows");
var twistedBowPrice = 940000000;

var robeTops = document.getElementById("num-robe-tops");
var robeTopPrice = 2147187090;

var prayerExp = document.getElementById("num-prayer-exp");
var prayerExpPrice = 15;

var vorkath = document.getElementById("num-vorkath-hours");
var vorkathGPH = 2400000;

var torags = document.getElementById("num-hammers");
var toragsPrice = 100000;

updateTrackers();

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function countGold(){
    let gold = document.getElementById("goldCounter");
    currentGold = currentGold + changePerSecond;
    gold.innerHTML = numberWithCommas(Math.round(currentGold));
    secondsUntilUpdate = secondsUntilUpdate -1;

    if(secondsUntilUpdate <= 0 ){
        secondsUntilUpdate = 86400 //There are 86,400 seconds in a day.
    }
    console.log(changePerSecond);


    updateTrackers()
}

//Update the trackers for Bonds/Twisted Bows/Prayer exp /Vorkath etc
function updateTrackers(){
    bonds.innerHTML = numberWithCommas(Math.round(startingAmount / bondPrice)) + " Old School Bonds";
    twistedBows.innerHTML = numberWithCommas(Math.round(startingAmount / twistedBowPrice) + " Twisted Bows");
    robeTops.innerHTML = numberWithCommas(Math.round(startingAmount / robeTopPrice) + " 3rd Age Druidic Robe Tops");
    prayerExp.innerHTML = numberWithCommas(Math.round(startingAmount / prayerExpPrice) + " Prayer Experience");
    vorkath.innerHTML = numberWithCommas(Math.round(startingAmount / vorkathGPH) + " Hours at Vorkath");
    torags.innerHTML = numberWithCommas(Math.round(startingAmount / toragsPrice) + " Torag's Hammers");


}