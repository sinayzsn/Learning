// SPDX-License-Identifier: MIT

pragma solidity >=0.7.0 <0.9.0;

import "./SimpleStorage.sol"; 

contract StorageFactory {
    // Identifier not found or not unique.
    // This need to be fixed, what has to be done here?
    // When I have imported the "SimpleStorage.sol" I did not changed the contract name the contract
    //  name is what is being mapped to the SimpleStorage array.
    SimpleStorage[] public simpleStorageArray;
    
    function createSimpleStorageContract() public {
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);
    }

    // This function would call the store function from SimpleStorage file
    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        simpleStorage.store(_simpleStorageNumber);
        // You
    }

    function sfGet(uint256 _simpleStorageIndex) public view returns (uint256) {
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        return simpleStorage.getnumber();
    }
}