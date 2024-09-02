package com.test.springbdd;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import org.apache.tomcat.jni.Status;
import org.hamcrest.Matcher;
import org.hamcrest.Matchers;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultActions;
import org.springframework.http.MediaType;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import java.util.Scanner;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class changeRoomtypeStepDefinition extends StepDefinition{
    @Autowired
	private MockMvc mvc;
	
	ResultActions action;

    

    @When("the admin calls \\/changeRoomtype with type = {string}")
    public void the_admin_calls_changeRoomtype(String type) throws Exception{
        action = mvc.perform(get("/changeRoomtype")
        .param("type", type)
        .contentType(MediaType.APPLICATION_JSON));
    }

    @Then("prompt appears to change room type with status {int}")
    public void prompt(Integer status) throws Exception{
        action.andExpect(status().is(status));
    }

    @Then("he receives the room with type {string}")
    public void then_he_receives_room_with_type(String type2) throws Exception{
        action.andExpect(jsonPath("type").value(type2));
        ///action.andExpect(jsonPath("1", Matchers.is(type2)));
    }

}
