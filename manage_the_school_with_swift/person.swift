// Script that describes a Person based on input given by a main func

class Person {
  // super class for Person. init name and age
  var first_name: String
  var last_name: String
  var age: Int

  init(first_name: String, last_name: String, age: Int) {
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
  }

  // func that returns the full name of Person
  func fullName() -> String {
    return "\(self.first_name) \(self.last_name)"
  }
}

// protocol that classifies a Person as a student or mentor
protocol Classify {
  func isStudent() -> Bool
}

class Mentor: Person, Classify {
  // sub-class of Person to describe mentors
  // func that returns false because Person is not student
  func isStudent() -> Bool {
    return false
  }
}

class Student: Person, Classify {
  // sub-class of Person to describe students
  // func that returns true because Person is student
  func isStudent() -> Bool {
    return true
  }
}
