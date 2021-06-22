# Created by aravindanathdm at 12/06/21
Feature: Verify student list
  # Enter feature description here

  Scenario:  Verify student list API
    Given the student app is running
    When we excute the student list api method
    Then student list is displayed


