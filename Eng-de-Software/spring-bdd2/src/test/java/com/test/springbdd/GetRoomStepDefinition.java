package com.test.springbdd;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import org.hamcrest.Matchers;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultActions;

import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class GetRoomStepDefinition extends StepDefinition{
    @Autowired
	private MockMvc mvc;
	
	ResultActions action;
    
	private static final Logger log = LoggerFactory.getLogger(GetRoomStepDefinition.class);

    @When("the client calls \\/getRoom with type = {string}")
	public void the_client_calls_getRoom(String type) throws Exception {
		action=mvc.perform(get("/getRoom")
			.param("type", type)
			.contentType(MediaType.APPLICATION_JSON));
	}

    @Then("the client receives status code of {int} for type")
    public void the_client_receives_status_code_of_for_type(Integer status) throws Exception {
		action.andExpect(status().is(status));
	}

    @Then("the client receives room with {string} type")
    public void the_client_receives_room_with_type(String type) throws Exception {
		log.info("Expecting room with type", type);
		action.andExpect(jsonPath("type").value(type));
	}
}
