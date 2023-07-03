// SPDX-License-Identifier: MIT

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 * @custom:dev-run-script ./scripts/deploy_with_ethers.ts
 */
contract SimpleStorage {

    uint256 number;

    function store( uint256 _num) public {
        number = _num;
    }

    function getnumber() public view returns(uint256){
        return number;
    }

    struct People {
        uint256 number;
        string name;
    }

    People[] public people;
    
    mapping (string => uint256) public nameToNumber;
    
    /** The 'memory' here is that would allow us to temporarily store it.
    *   If you want to permenetly store you must use 'storage for it'.
    */ 
    function addPerson(string memory _name, uint256 _number) public{
        people.push(People(_number, _name));
        nameToNumber[_name] = _number;
    }

}