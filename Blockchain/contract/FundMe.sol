// SPDX-License-Identifier: MIT

pragma solidity >=0.7.0 <0.9.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
// import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

contract FundMe {

    mapping(address => uint256) public address_to_amount_funded;

    address public owner;

    address[] public funders;

    constructor() public {
        owner = msg.sender;
    }

    function fund() public payable {
        // The line below would say that you cannot fund below 5 USD
        uint256 minUsd = 1 * 10 ** 18;

        // This line would cancel the transaction if the minimum requirments
        // are not met
        require (getConversionRate(msg.value) >= minUsd, "You need to spend more ETH!");
        address_to_amount_funded[msg.sender] += msg.value;

        funders.push(msg.sender);
    }

    function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e);
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e);
        (,int256 answer,,,) = priceFeed.latestRoundData();
        return uint256(answer * 10000000000);
        // 1,588.24430000
    }

    function getConversionRate(uint256 ethAmount) public view returns(uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUsd;
    }

    modifier onlyOwner() {
        //is the message sender owner of the contract?
        require(msg.sender == owner);

        _;
    }

    function withdraw() payable onlyOwner public {
        require (msg.sender == owner);
        payable(msg.sender).transfer(address(this).balance);
        for (uint256 funderIndex=0; funderIndex < funders.length; funderIndex++){
            address funder = funders[funderIndex];
            address_to_amount_funded[funder] = 0;
        }
    }
}