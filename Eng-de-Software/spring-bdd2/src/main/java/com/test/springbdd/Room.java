package com.test.springbdd;

public class Room {
    private String type;
    private Integer number;


    public Room(Integer number, String type){
        super();
        this.type = type;
        this.number = number;
    }

    public String getType(){
        return type;
    }

    public void setType(String type){
        this.type = type;
    }

    public Integer getNumber(){
        return number;
    }

    public void setNumber(Integer number){
        this.number = number;
    }

    public void AddRoom(Integer number,String type ){
        this.type = type;
        this.number = number;
    }

}
