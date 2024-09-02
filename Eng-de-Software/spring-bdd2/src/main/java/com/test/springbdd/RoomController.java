package com.test.springbdd;

import java.util.HashMap;
import java.util.Map;

import javax.xml.crypto.Data;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;



@RestController
public class RoomController extends Database{
    Logger log = LoggerFactory.getLogger(this.getClass());
	

	@Autowired
	Environment env;
    Integer number =0;
    
    /**
	 * This method is added just to test the persistent shared storage for Azure app
	 * service by creating some files
	 * 
	 * @param type
	 * @return
	 * @throws Exception
	 */
    @GetMapping("/addRoom") /*Qual o método e a variavel associada */
    public ResponseEntity<Map<Integer, String>> addRoom(
        @RequestParam(value="type") String type, 
        @RequestParam(value="number") Integer number) throws Exception{
            log.info("called /addRoom");
            Database.rooms.put(number,type);
            return ResponseEntity.ok(Database.rooms);
    }
        
    @GetMapping("/getRoom")
    public ResponseEntity<Room> getRoom(@RequestParam(value = "type") String type) throws Exception{
        log.info("Received request for room type: {}", type);
        Database.rooms.put(1, type);
        Map.Entry<Integer, String> entry = Database.rooms.entrySet().iterator().next();
        Integer roomNumber = entry.getKey();
        String roomType = entry.getValue();
        Room room = new Room(roomNumber,roomType);
        return ResponseEntity.ok(room);
    }

    Map<Integer, String> roomMap= Map.of( 1,"individual", 2, "double", 3, "suite");

    @GetMapping("/changeRoomtype")
    public ResponseEntity<Room> changeRoomtype(
                        @RequestParam(value="type") String currentType
                        ,@RequestParam(value="type") String newType) throws Exception{
        log.info("Received request to change room type");
        getRoom(currentType);
        Database.rooms.put(1, newType);
        Map.Entry<Integer, String> entry = Database.rooms.entrySet().iterator().next();
        Integer roomNumber = entry.getKey();
        String roomType = entry.getValue();
        Room room = new Room(roomNumber,roomType);
        return ResponseEntity.ok(room);
    }

    
}
