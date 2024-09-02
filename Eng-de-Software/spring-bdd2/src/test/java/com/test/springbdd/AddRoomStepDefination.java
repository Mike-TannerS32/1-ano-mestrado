package com.test.springbdd;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import java.util.Map;
import java.util.Scanner;

import org.assertj.core.annotations.NonNull;
import org.hamcrest.Matchers;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultActions;
import org.springframework.http.MediaType;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import java.util.Scanner;




public class AddRoomStepDefination extends StepDefinition{
    @Autowired
	private MockMvc mvc;
	
	ResultActions action;

    

    @When("the admin calls \\/addRoom with type = {string}") /*método e mapear para a variavel */
    public void the_admin_calls_addRoom(String type) throws Exception{
        action = mvc.perform(get("/addRoom")
        .param("type", type)
        .param("number", "1")
        .contentType(MediaType.APPLICATION_JSON));
    }

    @Then("he receives status code of 200")
    public void receives_confirm() throws Exception{
        action.andExpect(status().is(200));
    }

    @And("receives the room with the {string} characteristic")
    public void return_room(String type) throws Exception{
        action.andExpect(jsonPath("1", Matchers.is(type)));
    }

    /*@When("the admin calls \\/addDualRoom") *//*método e mapear para a variavel */
    /*public void the_admin_calls_addDualRoom() throws Exception{
        action = mvc.perform(get("/addDualRoom")
        .param("type", "dual")
        .param("number", "2")
        .contentType(MediaType.APPLICATION_JSON));
    }

    @Then("he receives status code of 200")
    public void receives_confirm2() throws Exception{
        action.andExpect(status().is(200));
    }

    @And("receives the room with the dual characteristic")
    public void return_room2() throws Exception{
        action.andExpect(jsonPath("2", Matchers.is("dual")));
    }*/
}
