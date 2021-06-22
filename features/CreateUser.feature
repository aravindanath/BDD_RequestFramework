# Created by aravindanathdm at 12/06/21
Feature: Create a user in go rest database
  # Enter feature description here

  @Sprint16
  Scenario: Create a User using valid data
  Given A user with valid access token
      And the user wants to create a record with first name as "John X"
      And the user record has a last name of "Rocket"
      And the gender is "male"
      And date of birth is "1962-08-12"
      And an email of "johnrocketx@yopmail.com"
      And a phone number of "+637832233"
      And a website of "https://bit.ly/IqT6zt"
      And the address is "Platform 3/4 end of rainbow street"
      And the user status is "active"
    When user submits the user data in "https://gorest.co.in/public-api/users"
      Then you should receive a "200" status code
      And first name "John X" should be in response body
      And last name "Rocket" should be in response body
      And gender "male" should be in response body
      And date of birth "1962-08-12" should be in response body
      And email "johnrocketx@yopmail.com" should be in response body
      And phone number "+637832233" should be in response body
      And website "https://bit.ly/IqT6zt" should be in response body
      And address "Platform 3/4 end of rainbow street" should be in response body
      And user status "active" should be in response body
    # Enter steps here
  #tanwir.zaki@gmail.com
